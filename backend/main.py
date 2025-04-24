from antlr4 import *
from antlr4 import CommonTokenStream, InputStream
from visitor import CustomVisitor
from antlr4.error.ErrorListener import ErrorListener
from interpreter.ConnectITLexer import ConnectITLexer
from interpreter.ConnectITParser import ConnectITParser
from listener import GlobalScope, CustomListener
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
            self.errors.append(f"\033[91mSyntax Error:\033[0m Unexpected token '{error_token}' at line {line}, column {column}. Did you mistype one of the keywords?")
        elif "extraneous input" in msg:
            self.errors.append(f"\033[91mSyntax Error:\033[0m Extraneous token '{error_token}' at line {line}, column {column}. Did some extra characters slip in by accident?")
        elif "missing" in msg:
            self.errors.append(f"\033[91mSyntax Error:\033[0m Missing token at line {line}, column {column}, near '{error_token}'. Did you forget to finish an instruction?")
        elif "no viable alternative" in msg:
            self.errors.append(f"\033[91mSyntax Error:\033[0m Invalid syntax at line {line}, column {column}, near '{error_token}'. Did you get an instruction mixed up?")
        else:
            self.errors.append(f"\033[91mSyntax Error:\033[0m {msg} at line {line}, column {column}.")

def evaluate_expression(expression):
    input_stream = InputStream(expression)
    lexer = ConnectITLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ConnectITParser(tokens)

    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    if error_listener.has_error:
        print("\n".join(error_listener.errors))
        return None

    global_scope = GlobalScope()
    listener = CustomListener(global_scope)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    try:
        visitor = CustomVisitor(global_scope)
        result = visitor.visit(tree)
        return result
    except Exception as e:
        return f"Runtime Error: {str(e)}"

def parse_args():
    parser = argparse.ArgumentParser(description="Process a file with a custom extension.")
    parser.add_argument('filename', type=str, help='The path to the file to be processed')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    try:
        with open(f"programs/{args.filename}", 'r') as f:
            program = f.read()
        result = evaluate_expression(program)
        if result is not None:
            if result[0] == "{":
                print("Generated figure successfully")
            else:
                print(result)
    except Exception as e:
        print(f"Error: {e}")


