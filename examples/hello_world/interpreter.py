from antlr4 import *
from ConnectITLexer import ConnectITLexer
from ConnectITParser import ConnectITParser
from ConnectITVisitor import ConnectITVisitor

from data_types import *

# Visitor-based Interpreter
class EvalVisitor(ConnectITVisitor):
    def __init__(self):
        self.variables = {}

    def visitUnitDeclaration(self, ctx):
        name: str = self.visit(ctx.ID())
        value: str = self.visit(ctx.unitExpr())
        
        u: Unit = Unit(name, value)

        self.variables[name] = u
        return None

    def visitUnitExpr(self, ctx: ConnectITParser.UnitExprContext):
        if ctx.COLOR():
            return ctx.COLOR().getText()  # Return color as a string
        elif ctx.PATTERN():
            return ctx.PATTERN().getText()  # Return pattern as a string
        return None  # Empty unit initialization

def evaluate_expression(expression):
    input_stream = InputStream(expression)
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.expr()

    visitor = EvalVisitor()
    return visitor.visit(tree)

# Running the Interpreter
if __name__ == "__main__":
    while True:
        expr = input("Enter expression (or 'exit' to quit): ")
        if expr.lower() == "exit":
            break
        try:
            result = evaluate_expression(expr)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
