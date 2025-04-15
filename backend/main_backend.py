from antlr4 import *
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from interpreter.ConnectITLexer import ConnectITLexer
from interpreter.ConnectITParser import ConnectITParser
from interpreter.ConnectITVisitor import ConnectITVisitor

from data_types import *
from utils import *

class EvalVisitor(ConnectITVisitor):
    def __init__(self):
        self.variables = {}
        self.render = []
        self.fig = go.Figure()

    def visitProgram(self, ctx):
        output = None
        for i in range(ctx.getChildCount()):
            statement_output = self.visit(ctx.getChild(i))
            if statement_output is not None:
                output = statement_output
        if output is None:
            return "No output"
        return output
    
    def visitStatement(self, ctx):
        # print(f"Statement: {ctx.getText()}")
        if ctx.declaration():
            return self.visit(ctx.declaration())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.showStatement():
            return self.visit(ctx.showStatement())
        # elif ctx.whileStmt():
        #     return self.visit(ctx.whileStmt())
        # elif ctx.forStmt():
        #     return self.visit(ctx.forStmt())
        # elif ctx.ifStmt():
        #     return self.visit(ctx.ifStmt())
        # elif ctx.functionDeclaration():
        #     return self.visit(ctx.functionDeclaration())
        # elif ctx.returnExpr():
        #     return self.visit(ctx.returnExpr())
        else:
            raise Exception("Invalid statement")

    def visitDeclaration(self, ctx):
        # print(f"Declaration: {ctx.getText()}")
        if ctx.newUnit():
            return self.visit(ctx.newUnit())
        elif ctx.newLayer():
            return self.visit(ctx.newLayer())
        elif ctx.newShape():
            return self.visit(ctx.newShape())
        elif ctx.newModel():
            return self.visit(ctx.newModel())
        elif ctx.newNumber():
            return self.visit(ctx.newNumber())
        elif ctx.newBoolean():
            return self.visit(ctx.newBoolean())
        return None

    def visitNewUnit(self, ctx):
        print(f"NewUnit: {ctx.getText()}")
        for unit in ctx.unitDeclarationList().unitDeclaration():
            print(f"UnitDeclaration: {unit.getText()}")
            id_ = unit.ID(0).getText()
            color, pattern = None, None
            if unit.getChildCount() > 2 and unit.getChild(1).getText() == '=':
                if unit.unitExpr():
                    color, pattern = self.visit(unit.unitExpr())
                elif unit.ID(1):
                    source_id = unit.ID(1).getText()
                    if source_id not in self.variables or not isinstance(self.variables[source_id], Unit):
                        raise Exception(f"'{source_id}' is not a defined Unit.")
                    source_unit = self.variables[source_id]
                    color, pattern = source_unit.color, source_unit.pattern
            else:
                raise Exception("Invalid unit declaration")
            
            self.variables[id_] = Unit(color=color, pattern=pattern)
        return None

    def visitUnitExpr(self, ctx):
        # print(f"UnitExpr: {ctx.getText()}")
        color, pattern = None, None
        if ctx.COLOR():
            color = ctx.COLOR().getText()[1:-1]
        elif ctx.PATTERN():
            pattern = ctx.PATTERN().getText()[1:-1]
        return color, pattern
    
    def visitNewLayer(self, ctx):
        # print(f"NewLayer: {ctx.getText()}")
        for layer in ctx.layerDeclarationList().layerDeclaration():
            print(f"LayerDeclaration: {layer.getText()}")
            layer_name = layer.ID(0).getText()
            units = []
            closed = False

            if layer.getChildCount() > 2 and layer.getChild(layer.getChildCount() - 1).getText() == "CLOSED":
                closed = True

            if layer.getChildCount() > 2 and layer.getChild(1).getText() == '=':
                if layer.layerExpr():
                    units = self.visitLayerExpr(layer.layerExpr())
                elif layer.ID(1):
                    source_id = layer.ID(1).getText()
                    if source_id not in self.variables or not isinstance(self.variables[source_id], Layer):
                        raise Exception(f"'{source_id}' is not a defined Layer.")
                    source_layer = self.variables[source_id]
                    units = source_layer.units
                    closed = source_layer.closed
            else:
                raise Exception("Invalid layer declaration")

            if layer_name in self.variables:
                raise Exception(f"Layer '{layer_name}' is already defined.")

            new_layer = Layer(units=units, closed=closed)
            self.variables[layer_name] = new_layer
        return None
        
    def visitLayerExpr(self, ctx):
        # print(f"LayerExpr: {ctx.getText()}")
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '*':
            id_ = ctx.ID(0).getText()
            if id_ not in self.variables or not isinstance(self.variables[id_], Unit):
                raise Exception(f"'{id_}' is not a defined Unit.")
            unit = self.variables[id_]
            if ctx.NUMBER():
                length = int(ctx.NUMBER().getText())
            elif ctx.ID(1):
                length_id = ctx.ID(1).getText()
                if length_id not in self.variables or not isinstance(self.variables[length_id], int):
                    raise Exception(f"'{length_id}' is not a defined Number.")
                length = self.variables[length_id]
            else:
                raise Exception("Invalid multiplier for Unit.")
            return [unit] * length

        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '+':
            left_units = self.visit(ctx.layerExpr(0))
            right_units = self.visit(ctx.layerExpr(1))
            return left_units + right_units

        else:
            raise Exception("Invalid layerExpr")       

    def visitNewShape(self, ctx):
        # print(f"NewShape: {ctx.getText()}")
        for shape in ctx.shapeDeclarationList().shapeDeclaration():
            print(f"ShapeDeclaration: {shape.getText()}")
            shape_name = shape.ID(0).getText()
            layers = []
            connections = []

            if shape.shapeExpr() and shape.getChild(1).getText() == '<--':
                layers, connections = self.visitShapeExpr(shape.shapeExpr())
            elif shape.getChildCount() == 3 and shape.getChild(1).getText() == '=':
                source_id = shape.getChild(2).getText()
                if source_id not in self.variables or not isinstance(self.variables[source_id], Shape):
                    raise Exception(f"'{source_id}' is not a defined Shape.")
                source_shape = self.variables[source_id]
                layers = source_shape.layers
                connections = source_shape.connections

            if shape_name in self.variables:
                existing_shape = self.variables[shape_name]
                if not isinstance(existing_shape, Shape):
                    raise Exception(f"Variable '{shape_name}' is not a Shape.")
                existing_shape.layers.extend(layers)
                existing_shape.connections.extend(connections)
            else:
                new_shape = Shape(layers=layers, connections=connections)
                self.variables[shape_name] = new_shape
        return None

    def visitShapeExpr(self, ctx):
        # TODO: Dodać implementację SHAPE <- LAYER --> SHAPE 
        print(f"LayerChain: {ctx.getText()}")

        # Recursive case: layerChain with '<-' or '<<-' or '<-' NUMBER '-'
        if ctx.getChildCount() > 1:
            if ctx.layerExpr():
                left = [Layer("none", self.visit(ctx.layerExpr()))]
            else:
                left = [self.variables[ctx.ID(0).getText()]]

            right, connections = self.visit(ctx.shapeExpr())

            if ctx.getChild(1).getText() == '<-':
                if ctx.NUMBER():
                    return left + right, [{"type": 1, "shift": int(ctx.NUMBER().getText())}] + connections
                return left + right, [{"type": 1, "shift": self.variables[ctx.ID(1).getText()]}]  + connections

            elif ctx.getChild(1).getText() == '<<-':
                if ctx.NUMBER():
                    return left + right, [{"type": 0, "shift": int(ctx.NUMBER().getText())}]  + connections
                return left + right, [{"type": 0, "shift": self.variables[ctx.ID(1).getText()]}]  + connections

        # Base case: Single layerExpr or ID
        else:
            if ctx.layerExpr():
                return [Layer("none", self.visit(ctx.layerExpr()))], []

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

        raise Exception("Invalid Shape Expression")

    def visitNewNumber(self, ctx):
        # print(f"NumberDeclaration: {ctx.getText()}")
        for number in ctx.numberDeclarationList().numberDeclaration():
            print(f"NumberID: {number.getText()}")
            number_name = number.ID(0).getText()
            if number.getChildCount() > 2 and number.getChild(1).getText() == '=':
                if number.NUMBER():
                    number_value = int(number.NUMBER().getText())
                elif number.ID(1):
                    source_id = number.ID(1).getText()
                    if source_id not in self.variables or not isinstance(self.variables[source_id], int):
                        raise Exception(f"'{source_id}' is not a defined Number.")
                    number_value = self.variables[source_id]
                else:
                    raise Exception("Invalid number declaration")
            elif number.getChildCount() == 1:
                number_value = 0

            if number_name in self.variables and isinstance(self.variables[number_name], int):
                raise Exception(f"Warning: Number '{number_name}' is already defined.")
            elif number_name in self.variables:
                raise Exception(f"Variable '{number_name}' is not a Number.")
            # print(f"Creating new Number '{number_name}' with value {number_value}.")
            self.variables[number_name] = number_value
        return None
    
    def visitNewBoolean(self, ctx):
        # print(f"BooleanDeclaration: {ctx.getText()}")
        for boolean in ctx.booleanDeclarationList().booleanDeclaration():
            print(f"BooleanID: {boolean.getText()}")
            boolean_name = boolean.ID(0).getText()
            print(1)
            if boolean.getChildCount() > 2 and boolean.getChild(1).getText() == '=':
                print(2)
                print(boolean.getChild(2).getText())
                if boolean.BOOLEAN():
                    print(3)
                    boolean_value = boolean.BOOLEAN().getText() == ("TRUE" or "1")
                    print(boolean_value)
                elif boolean.ID(1):
                    source_id = boolean.ID(1).getText()
                    if source_id not in self.variables or not isinstance(self.variables[source_id], bool):
                        raise Exception(f"'{source_id}' is not a defined Boolean.")
                    boolean_value = self.variables[source_id]
                else:
                    raise Exception("Invalid boolean declaration")
            elif boolean.getChildCount() == 1:
                boolean_value = False

            if boolean_name in self.variables:
                raise Exception(f"Warning: Boolean '{boolean_name}' is already defined.")
            elif boolean_name in self.variables and isinstance(self.variables[boolean_name], bool):
                raise Exception(f"Variable '{boolean_name}' is not a Boolean.")
            # print(f"Creating new Boolean '{boolean_name}' with value {boolean_value}.")
            self.variables[boolean_name] = boolean_value
        return None
    
    # TODO: zrobix
    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        # print(f"Assigned {value} to {var_name}")
        return None
    

    def visitShowStatement(self, ctx):
        # print(f"ShowStatement: {ctx.getText()}")
        print(self.variables)
        if ctx.getChildCount() == 2:
            shape_name = ctx.ID().getText()

            if shape_name not in self.variables:
                print(f"Error: '{shape_name}' is not defined.")
                return

            structure = self.variables[shape_name]
            if isinstance(structure, Structure):
                return show_figure(self.fig, structure)
            else:
                print(f"SHOW only supports STRUCTUREs, not {type(structure)}.")

        else:
            raise Exception("Invalid instruction")

    def evaluate_expression(self, expression):
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
                # elif "no viable alternative" in msg:
                    # self.errors.append(f"Syntax Error: Invalid syntax at line {line}, column {column}, near '{"<EOL>" if error_token == '\n' else error_token}'.")
                # elif "extraneous input" in msg:
                #     self.errors.append(f"Syntax Error: Extraneous token '{error_token}' at line {line}, column {column}.")
                # elif "missing" in msg:
                #     self.errors.append(f"Syntax Error: Missing token at line {line}, column {column}, near '{"<EOL>" if error_token == '\n' else error_token}'.")
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

    def sample_render(self):
        with open('programs/playground.txt', 'r') as f:
            program = f.read()
        try:
            result = self.evaluate_expression(program)
            return result
        except Exception as e:
            print(f"Error: {e}")

    def interpret(self, program: str):
        try:
            result = self.evaluate_expression(program)
            return result
        except Exception as e:
            print(f"Error: {e}")
