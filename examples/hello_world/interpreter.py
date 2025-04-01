from antlr4 import *
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
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
        for unit_assignment_ctx in ctx.unitAssigmentList().unitAssignment():
            # print(f"UnitAssignment: {unit_assignment_ctx.getText()}")
            unit_name = unit_assignment_ctx.ID().getText()
            unit_color = None
            unit_pattern = None

            if unit_assignment_ctx.unitExpr():
                unit_expr_result = self.visit(unit_assignment_ctx.unitExpr())
                
                if unit_expr_result is not None:
                    if unit_expr_result.startswith('*') and unit_expr_result.endswith('*'):
                        if unit_expr_result[1:-1] in ['red', 'blue', 'green', 'white', 'black']:
                            unit_color = unit_expr_result[1:-1]
                            unit_pattern = None
                        elif unit_expr_result[1:-1] in ['striped', 'dotted', 'gradient']:
                            unit_color = None
                            unit_pattern = unit_expr_result[1:-1]
                        else:
                            raise Exception(f"Invalid unit expression: {unit_expr_result}")
                    else:
                        raise Exception(f"Invalid unit expression format: {unit_expr_result}")

            self.variables[unit_name] = Unit(name=unit_name, color=unit_color, pattern=unit_pattern)

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
        for layer_assignment_ctx in ctx.layerAssigmentList().layerAssignment():
            # print(f"LayerAssignment: {layer_assignment_ctx.getText()}")
            layer_name = layer_assignment_ctx.ID().getText()
            layer_closed = layer_assignment_ctx.getChildCount() > 3 and layer_assignment_ctx.getChild(3).getText() == "CLOSED"

            if layer_assignment_ctx.layerExpr():
                layer_units = self.visit(layer_assignment_ctx.layerExpr())
            else:
                layer_units = [], False

            self.variables[layer_name] = Layer(name=layer_name, units=layer_units, closed=layer_closed)

        return None

    def visitLayerExpr(self, ctx):
        # print(f"LayerExpr: {ctx.getText()}")

        if ctx.getChild(1).getText() == '*':
            name = ctx.ID().getText()
            unit: Unit = self.variables[name]
            length: str = ctx.NUMBER().getText()

            return [unit] * int(length)
        
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '+':
            units_left = self.visit(ctx.layerExpr(0))
            units_right = self.visit(ctx.layerExpr(1))
            return units_left + units_right

        elif ctx.getChildCount() == 0:
            return []

        else:
            raise Exception("Invalid layerExpr")

    def visitStandardAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        # print(f"Assigned {value} to {var_name}")
        return None

    def visitShapeAssignment(self, ctx):
        # print(f"ShapeAssignment: {ctx.getText()}")

        layer_chain, connections = self.visit(ctx.layerChain())
        shape_name = ctx.ID().getText()
        if shape_name in self.variables:
            shape = self.variables[shape_name]
            if not isinstance(shape, Shape):
                raise Exception(f"Variable '{shape_name}' is not a Shape.")
            shape.update(layers=layer_chain, connections=connections)
            # print(f"Updated shape '{shape_name}' with layers: {[l.name for l in layer_chain]} and connections: {connections}")
        else:
            raise Exception(f"Shape '{shape_name}' not defined. Try SHAPE {shape_name}")
        return None

    def visitModelAssignment(self, ctx):
        shape_chain = self.visit(ctx.shapeChain())
        model_name = ctx.ID().getText()

        if model_name in self.variables:
            model = self.variables[model_name]
            if not isinstance(model, Model):
                raise Exception(f"Variable '{model_name}' is not a Model.")
            model.shapes.extend(shape_chain)
            # print(f"Updated model '{model_name}' with shapes: {[sh.name for sh in shape_chain]}")
        else:
            raise Exception(f"Model '{model_name}' not defined. Try MODEL {model_name}")
        return None

    def visitShapeDeclaration(self, ctx):
        # print(f"ShapeDeclaration: {ctx.getText()}")

        for shape_id_ctx in ctx.idList().ID():
            # print(f"ShapeID: {shape_id_ctx.getText()}")
            shape_name = shape_id_ctx.getText()

            if shape_name in self.variables:
                print(f"Warning: Shape '{shape_name}' is already defined.")
            else:
                new_shape = Shape(name=shape_name, layers=[], connections=[])
                self.variables[shape_name] = new_shape
        return None

    def visitShapeDef(self, ctx):
        # print(f"ShapeDef: {ctx.getText()}")

        layers, connections = self.visit(ctx.layerChain())
        shape_name = ctx.ID().getText()
        is_new_shape = ctx.getChildCount() == 4 and ctx.getChild(2).getText() == 'SHAPE'

        if is_new_shape:
            if shape_name in self.variables:
                raise Exception(f"Shape '{shape_name}' is already defined.")

            new_shape = Shape(name=shape_name, layers=layers, connections=connections)
            self.variables[shape_name] = new_shape
            # print(f"New shape '{shape_name}' defined with layers: {[l.name for l in layers]} and connections: {connections}")

        else:
            if shape_name not in self.variables:
                raise Exception(f"Shape '{shape_name}' is not defined.")

            existing_shape = self.variables[shape_name]
            if not isinstance(existing_shape, Shape):
                raise Exception(f"Variable '{shape_name}' is not a shape.")
                
            existing_shape.layers.extend(layers)
            # print(f"Shape '{shape_name}' updated with additional layers: {layers.name}")

        return None

    def visitLayerChain(self, ctx):
        # TODO: Dodać implementację SHAPE <- LAYER --> SHAPE 
        # print(f"LayerChain: {ctx.getText()}")

        # Recursive case: layerChain with '<-' or '<<-' or '<-' NUMBER '-'
        if ctx.layerChain():
            if ctx.layerExpr():
                left = [Layer(self.visit(ctx.layerExpr()))]
            else:
                left = [self.variables[ctx.ID().getText()]]

            right, connections = self.visit(ctx.layerChain())

            if ctx.getChild(1).getText() == '<-':
                if ctx.NUMBER():
                    return left + right, [{"type": 1, "shift": int(ctx.NUMBER().getText())}] + connections
                return left + right, [{"type": 1, "shift": 0}]  + connections

            elif ctx.getChild(1).getText() == '<<-':
                if ctx.NUMBER():
                    return left + right, [{"type": 0, "shift": int(ctx.NUMBER().getText())}]  + connections
                return left + right, [{"type": 0, "shift": 0}]  + connections

        # Base case: Single layerExpr or ID
        else:
            if ctx.layerExpr():
                units = self.visit(ctx.layerExpr())
                return [Layer("none", units)], []

            elif ctx.ID():
                layer_id = ctx.ID().getText()
                if layer_id in self.variables:
                    layer = self.variables[layer_id]
                    if isinstance(layer, Layer):
                        return [layer], []
                    else:
                        raise Exception(f"Variable '{layer_id}' is not a Layer.")
                else:
                    raise Exception(f"Undefined variable: {layer_id}")

        raise Exception("Invalid LayerChain")

    def visitShowStatement(self, ctx):
        # print(f"ShowStatement: {ctx.getText()}")
        if ctx.getChildCount() == 2:
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

    class SyntaxErrorListener(ErrorListener):
        def __init__(self):
            super().__init__()
            self.has_error = False
            self.errors = []

        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            self.has_error = True
            error_token = offendingSymbol.text if offendingSymbol else "<EOF>"

            if "mismatched input" in msg:
                self.errors.append(f"Syntax Error: Unexpected token '{error_token}' at line {line}, column {column}.")
            elif "no viable alternative" in msg:
                self.errors.append(f"Syntax Error: Invalid syntax at line {line}, column {column}, near '{"<EOL>" if error_token == '\n' else error_token}'.")
            elif "extraneous input" in msg:
                self.errors.append(f"Syntax Error: Extraneous token '{error_token}' at line {line}, column {column}.")
            elif "missing" in msg:
                self.errors.append(f"Syntax Error: Missing token at line {line}, column {column}, near '{"<EOL>" if error_token == '\n' else error_token}'.")
            else:
                self.errors.append(f"Syntax Error: {msg} at line {line}, column {column}.")

    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()  # Remove default error listener
    parser.addErrorListener(error_listener)

    try:
        tree = parser.program()
    except Exception as e:
        return f"Parsing Error: {str(e)}"

    if error_listener.has_error:
        return "\n".join(error_listener.errors)

    try:
        visitor = EvalVisitor()
        return visitor.visit(tree)
    except Exception as e:
        return f"Runtime Error: {str(e)}"

if __name__ == "__main__":
    with open('programs/hello_world.txt', 'r') as f:
        program = f.read()
    try:
        result = evaluate_expression(program)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
