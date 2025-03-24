from antlr4 import *
from ConnectITLexer import ConnectITLexer
from ConnectITParser import ConnectITParser
from ConnectITVisitor import ConnectITVisitor

from data_types import *

class EvalVisitor(ConnectITVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx):
        output = []
        for i in range(ctx.getChildCount()):
            statement_output = self.visit(ctx.getChild(i))
            if statement_output is not None:
                output.append(statement_output)
        if len(output) == 0:
            return "No output"
        return "\n".join(output)
    
    def visitStatement(self, ctx):
        # print(f"Statement: {ctx.getText()}")
        if ctx.declaration():
            return self.visit(ctx.declaration())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.shapeDef():
            return self.visit(ctx.shapeDef())
        if ctx.modelDef():
            return self.visit(ctx.modelDef())
        if ctx.showStatement():
            return self.visit(ctx.showStatement())
        else:
            raise Exception("Invalid statement")

    def visitUnitDeclaration(self, ctx):
        # print(f"UnitDeclaration: {ctx.getText()}")
        name: str = ctx.ID().getText()
        value: str = self.visit(ctx.unitExpr())
        unit: Unit = Unit(name, value, value)

        self.variables[name] = unit
        return None

    def visitUnitExpr(self, ctx):
        # print(f"UnitExpr: {ctx.getText()}")
        if ctx.COLOR():
            return ctx.COLOR().getText()
        elif ctx.PATTERN():
            return ctx.PATTERN().getText()
        return None
    
    def visitLayerDeclaration(self, ctx):
        # print(f"LayerDeclaration: {ctx.getText()}")
        name: str = ctx.ID().getText()
        units: list = self.visit(ctx.layerExpr())
        layer: Layer = Layer(name, units)

        self.variables[name] = layer
        return None

    def visitLayerExpr(self, ctx):
        # print(f"LayerExpr: {ctx.getText()}")
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '*':
            name = ctx.ID().getText()
            unit: Unit = self.variables[name]
            length = ctx.NUMBER().getText()

            return [unit] * int(length)
        
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '+':
            units_left: list = self.visit(ctx.layerExpr(0))
            units_right: list = self.visit(ctx.layerExpr(1))
            return units_left + units_right

        elif ctx.getChildCount() == 0:
            return []

        else:
            raise Exception("Invalid layerExpr")
        
    def visitShowStatement(self, ctx):
        # print(f"ShowStatement: {ctx.getText()}")
        if ctx.getChildCount() == 2:
            name: str = ctx.ID().getText()
            var: Structure = self.variables[name]
            return(str(var))

        else:
            raise Exception("Invalid instruction")

def evaluate_expression(expression):
    input_stream = InputStream(expression)
    lexer = ConnectITLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ConnectITParser(token_stream)
    tree = parser.program()

    visitor = EvalVisitor()
    return visitor.visit(tree)

if __name__ == "__main__":
    with open('programs/hello_world.txt', 'r') as f:
        program = f.read()
    try:
        result = evaluate_expression(program)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
