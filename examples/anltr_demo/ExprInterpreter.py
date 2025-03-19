from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

# Visitor-based Interpreter
class EvalVisitor(ExprVisitor):

    def visitAddSub(self, ctx):
        # print('AddSub')
        # print(ctx.getText())

        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())

        if ctx.getChild(1).getText() == '+':
            return left + right
        else:
            return left - right

    def visitMulDiv(self, ctx):
        # print('MulDiv')
        # print(ctx.getText())

        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())

        if ctx.getChild(1).getText() == '*':
            return left * right
        else:
            return left / right

    def visitNumber(self, ctx):
        # print('Number')
        # print(ctx.getText())

        return int(ctx.getText())

    def visitParens(self, ctx):
        # print('Parens')
        # print(ctx.getText())

        return self.visit(ctx.expr())

    def visitSingleTerm(self, ctx):
        # print('Term')
        # print(ctx.getText())

        return self.visit(ctx.term())

    def visitSingleFactor(self, ctx):
        # print('Factor')
        # print(ctx.getText())
        
        return self.visit(ctx.factor())

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
