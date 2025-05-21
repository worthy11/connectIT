from antlr4 import *
from antlr4 import CommonTokenStream, InputStream
from visitor import CustomVisitor
from antlr4.error.ErrorListener import ErrorListener
from interpreter.ConnectITLexer import ConnectITLexer
from interpreter.ConnectITParser import ConnectITParser
from listener import *
import argparse

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        error_token = offendingSymbol.text if offendingSymbol else "<EOF>"
        error_token = "<EOL>" if error_token == '\n' else error_token

        if "mismatched input" in msg:
            self.errors.append(f"Unexpected token '{error_token}' at line {line}, column {column}. Did you mistype one of the keywords?")
        elif "extraneous input" in msg:
            self.errors.append(f"Extraneous token '{error_token}' at line {line}, column {column}. Did some extra characters slip in by accident?")
        elif "missing" in msg:
            self.errors.append(f"Missing token at line {line}, column {column}, near '{error_token}'. Did you forget to finish an instruction?")
        elif "no viable alternative" in msg:
            self.errors.append(f"Invalid syntax at line {line}, column {column}, near '{error_token}'. Did you get an instruction mixed up?")
        else:
            self.errors.append(f"{msg} at line {line}, column {column}.")

class LexerErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        error_token = offendingSymbol.text if offendingSymbol else "<EOF>"
        error_token = "<EOL>" if error_token == '\n' else error_token
        self.errors.append(f"Invalid {msg} - line {line}, column {column}.")

def evaluate_expression(expression):
    input_stream = InputStream(expression)
    lexer = ConnectITLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ConnectITParser(tokens)

    lexer_error_listener = LexerErrorListener()
    lexer.removeErrorListeners()  
    lexer.addErrorListener(lexer_error_listener)

    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    if lexer_error_listener.has_error:
        print(lexer_error_listener.errors)
        return {
            "type": "error",
            "message": "\n".join(lexer_error_listener.errors)
        }

    if error_listener.has_error:
        print(error_listener.errors)
        return {
            "type": "error",
            "message": "\n".join(error_listener.errors)
        }
    

    listener = CustomListener()
    walker = ParseTreeWalker()

    try:
        walker.walk(listener, tree)
    except Exception as e:
        print(str(e))
        return {
            "type": "error",
            "message": str(e)
        }

    try:
        visitor = CustomVisitor(listener.scopes)
        result = visitor.visit(tree)

    except Exception as e:
        return {
            "type": "error",
            "message": f"{str(e)}"
        }
    
    if result is None:
        return {
            "type": "error",
            "message": "No output: You need to use SHOW statement to display your model."
        }

    return result

def parse_args():
    parser = argparse.ArgumentParser(description="Process a file with a custom extension.")
    parser.add_argument('filename', type=str, help='The path to the file to be processed')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    with open(f"programs/{args.filename}", 'r') as f:
        program = f.read()
    result = evaluate_expression(program)
    if result is not None:
        if isinstance(result, str):
            if result[0] == "{":
                print("Generated figure successfully")
        else:
            print(result)
