from antlr4 import *
from ConnectITLexer import ConnectITLexer
from ConnectITParser import ConnectITParser
from ConnectITVisitor import ConnectITVisitor

from data_types import *
from utils import *

class EvalVisitor(ConnectITVisitor):
    def __init__(self):
        self.variables = {}
        self.fig = go.Figure()

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

    def visitShapeDeclaration(self, ctx):
        # print(f"ShapeDeclaration: {ctx.getText()}")
        name: str = ctx.ID().getText()
        layers: list = self.visit(ctx.shapeExpr())
        shape: Shape = Shape(name, layers)

        self.variables[name] = shape
        return None

    def visitShapeExpr(self, ctx):
        # print(f"ShapeExpr: {ctx.getText()}")

        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            if op == "*":
                if isinstance(left, Layer) and ctx.getChild(2).NUMBER():
                    return [left] * int(ctx.getChild(2).NUMBER().getText())
                else:
                    raise Exception("Invalid multiplication in shape expression")

            elif op == "+":
                if isinstance(left, list) and isinstance(right, list):
                    return left + right
                else:
                    raise Exception("Invalid addition in shape expression")

        elif ctx.ID():
            name = ctx.ID().getText()
            if name in self.variables and isinstance(self.variables[name], Layer):
                return [self.variables[name]]
            else:
                raise Exception(f"Shape expression refers to an undefined layer: {name}")

        else:
            raise Exception("Invalid shape expression")


    def visitShowStatement(self, ctx):
        # print(f"ShowStatement: {ctx.getText()}")
        if ctx.getChildCount() == 2:
            name: str = ctx.ID().getText()
            var: Structure = self.variables[name]
            # return(str(var))
            shape_name = ctx.ID().getText()

            if shape_name not in self.variables:
                print(f"Error: '{shape_name}' is not defined.")
                return

            structure = self.variables[shape_name]
            if isinstance(structure, Structure):
                show_figure(self.fig, structure)
            else:
                print(f"SHOW only supports STRUCTUREs, not {type(structure)}.")

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
    with open('examples/hello_world/programs/hello_world.txt', 'r') as f:
        program = f.read()
    try:
        result = evaluate_expression(program)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
