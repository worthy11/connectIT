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
        # if ctx.assignment():
        #     return self.visit(ctx.assignment())
        if ctx.shapeDef():
            return self.visit(ctx.shapeDef())
        if ctx.modelDef():
            return self.visit(ctx.modelDef())
        if ctx.showStatement():
            return self.visit(ctx.showStatement())
        else:
            raise Exception("Invalid statement")

    def visitUnitDeclaration(self, ctx):
        print(f"UnitDeclaration: {ctx.getText()}")
        for unit_assignment_ctx in ctx.unitAssigmentList().unitAssignment():
            print(f"UnitAssignment: {unit_assignment_ctx.getText()}")
            unit_name = unit_assignment_ctx.ID().getText()

            if unit_assignment_ctx.unitExpr():
                unit_expr_result = self.visit(unit_assignment_ctx.unitExpr())
                
                if unit_expr_result.startswith('*') and unit_expr_result.endswith('*'):
                    if unit_expr_result[1:-1] in ['red', 'blue', 'green', 'white', 'black']:
                        unit_color = unit_expr_result
                        unit_pattern = None
                    elif unit_expr_result[1:-1] in ['striped', 'dotted', 'gradient']:
                        unit_color = None
                        unit_pattern = unit_expr_result
                    else:
                        raise Exception(f"Invalid unit expression: {unit_expr_result}")
                else:
                    raise Exception(f"Invalid unit expression format: {unit_expr_result}")
            else:
                unit_color = None
                unit_pattern = None

            self.variables[unit_name] = Unit(name=unit_name, color=unit_color, pattern=unit_pattern)

        return None

    def visitUnitExpr(self, ctx):
        print(f"UnitExpr: {ctx.getText()}")
        if ctx.COLOR():
            return ctx.COLOR().getText()
        elif ctx.PATTERN():
            return ctx.PATTERN().getText()
        return None
    
    def visitLayerDeclaration(self, ctx):
        print(f"LayerDeclaration: {ctx.getText()}")
        for layer_assignment_ctx in ctx.layerAssigmentList().layerAssignment():
            print(f"LayerAssignment: {layer_assignment_ctx.getText()}")
            layer_name = layer_assignment_ctx.ID().getText()

            if layer_assignment_ctx.layerExpr():
                layer_units = self.visit(layer_assignment_ctx.layerExpr())
            else:
                layer_units = []

            self.variables[layer_name] = Layer(name=layer_name, units=layer_units)

        return None

    def visitLayerExpr(self, ctx):
        print(f"LayerExpr: {ctx.getText()}")
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
        print(f"ShapeDeclaration: {ctx.getText()}")
        for shape_id_ctx in ctx.idList().ID():
            print(f"ShapeID: {shape_id_ctx.getText()}")
            shape_name = shape_id_ctx.getText()

            if shape_name in self.variables:
                print(f"Warning: Shape '{shape_name}' is already defined.")
            else:
                new_shape = Shape(name=shape_name, layers=[])
                self.variables[shape_name] = new_shape
        return None

    def visitShapeDef(self, ctx):
        print(f"ShapeDef: {ctx.getText()}")

        # Visit the layerChain to get the layers
        layers = self.visit(ctx.layerChain())
        print(type(layers))

        # Get the shape name (ID)
        shape_name = ctx.ID().getText()

        # Check if the 'SHAPE' keyword is present
        is_new_shape = ctx.getChildCount() == 4 and ctx.getChild(2).getText() == 'SHAPE'

        if is_new_shape:
            # Define a new shape
            if shape_name in self.variables:
                raise Exception(f"Shape '{shape_name}' is already defined.")
            new_shape = Shape(name=shape_name, layers=layers)
            self.variables[shape_name] = new_shape
            print(f"New shape '{shape_name}' defined with layers: {layers.name}")
        else:
            # Update an existing shape
            if shape_name not in self.variables:
                raise Exception(f"Shape '{shape_name}' is not defined.")
            existing_shape = self.variables[shape_name]
            if not isinstance(existing_shape, Shape):
                raise Exception(f"Variable '{shape_name}' is not a shape.")
            existing_shape.layers.extend(layers)
            print(f"Shape '{shape_name}' updated with additional layers: {layers.name}")

        return self.variables[shape_name]

    def visitLayerChain(self, ctx):
        print(f"LayerChain: {ctx.getText()}")

        # Base case: Single layerExpr or ID
        if ctx.layerExpr():
            return self.visit(ctx.layerExpr())
        elif ctx.ID():
            layer_id = ctx.ID().getText()
            if layer_id in self.variables:
                layer = self.variables[layer_id]
                if isinstance(layer, Layer):
                    return layer
                else:
                    raise Exception(f"Variable '{layer_id}' is not a Layer.")
            else:
                raise Exception(f"Undefined variable: {layer_id}")

        # Recursive case: layerChain with '<-' or '<<-' or '<-' NUMBER '-'
        if ctx.layerChain():
            left = self.visit(ctx.layerExpr() or ctx.ID())
            right = self.visit(ctx.layerChain())

            if ctx.getChild(1).getText() == '<-':
                # Combine chains for '<-' operator
                return right + left
            elif ctx.getChild(1).getText() == '<<-':
                # Combine chains for '<<-' operator
                return left + right
            elif ctx.NUMBER():
                # Handle '<-' NUMBER '-' layerChain
                number = int(ctx.NUMBER().getText())
                return [left] * number + right

        raise Exception("Invalid LayerChain")

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
