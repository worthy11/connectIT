from antlr4 import *
from interpreter.ConnectITParser import ConnectITParser
from interpreter.ConnectITVisitor import ConnectITVisitor

from data_types import *
from utils import *

class CustomVisitor(ConnectITVisitor):
    def __init__(self, scope):
        self.scope = scope
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
        if ctx.getChildCount() > 1 and ctx.getChild(0).getText() == "?":
            return None
        if ctx.declarationList():
            return self.visit(ctx.declarationList())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.showStatement():
            return self.visit(ctx.showStatement())
        else:
            raise Exception("Invalid statement")
        
    def visitDeclarationList(self, ctx):
        for dec in ctx.declaration():
            if dec.assignment():
                self.visit(dec.assignment())

        return None

    def visitAssignment(self, ctx):
        token = ctx.ID().getSymbol()
        line = token.line
        column = token.column
        name = token.text
        expected_type = self.scope.get_type(name)
        value, received_type = self.visit(ctx.expression())
        if expected_type != received_type:
            raise Exception(f"Type Error: Types {types[expected_type]} and {types[received_type]} don't match at line {line}, column {column}")
        self.scope.fill(name, value)

        return None

    def visitExpression(self, ctx):
        value, type = self.visit(ctx.logicExpr(0))
        if ctx.arrowOperator():
            match type:
                case 1:
                    value = self.createLayer(ctx)
                    type += 1
                case 2:
                    value = self.createShape(ctx)
                    type += 1
                case 3:
                    value = self.createModel(ctx)
                    type += 1
                case _:
                    raise Exception(f"Type Error: Cannot use connectors with type {types[type]}")
        return value, type

    def createLayer(self, ctx):
        value, _ = self.visit(ctx.logicExpr(0))
        first = value.extract_units()
        closed = ctx.getChildCount() % 2 == 0
        result = Layer(units=first, closed=closed)

        for i in range(1, len(ctx.logicExpr())):
            next_value, next_type = self.visit(ctx.logicExpr(i))
            op = ctx.getChild(2*i-1)
            if next_type != 1:
                raise Exception(f"Type Error: Can only apply '<->' connector to multiples of UNITs, not {types[next_type]}")
            if op.getText() != "<->":
                raise Exception(f"Type Error: Cannot use '{op.getText()}' connector when creating a LAYER")
            next_units = next_value.extract_units()
            for u in next_units:
                result.add_unit(u)
                
        return result

    def createShape(self, ctx):
        first, _ = self.visit(ctx.logicExpr(0))
        result = Shape(layers=[first])

        for i in range(1, len(ctx.logicExpr())):
            next_value, next_type = self.visit(ctx.logicExpr(i))
            op = ctx.getChild(2*i-1)
            if next_type != 2:
                raise Exception(f"Type Error: Cannot connect types LAYER and {types[next_type]}")

            type = 1
            shift = 0
            if "<<" in op.getText():
                type = 1
            if op.expression():
                shift_value, shift_type = self.visit(op.expression())
                if shift_type != 5:
                    raise Exception(f"Type Error: Shift can only be a NUMBER, not {types[shift_type]}")
                shift = shift_value
            result.add_layer(l=next_value, c={"type": type, "shift": shift})
            
        return result

    def createModel(self, ctx):
        first, _ = self.visit(ctx.logicExpr(0))
        result = Model(shapes=[first])

        for i in range(1, len(ctx.logicExpr())):
            next_value, next_type = self.visit(ctx.logicExpr(i))
            op = ctx.getChild(2*i-1)
            if next_type != 3:
                raise Exception(f"Type Error: Cannot connect types SHAPE and {types[next_type]}")

            type = 1
            shift = 0
            if "<<" in op.getText():
                type = 1
            if op.expression():
                shift_value, shift_type = self.visit(op.expression())
                if shift_type != 5:
                    raise Exception(f"Type Error: Shift can only be a NUMBER, not {types[shift_type]}")
                shift = shift_value
            result.add_shape(s=next_value, c={"type": type, "shift": shift})

        return result

    def visitLogicExpr(self, ctx):
        value, type = self.visit(ctx.andExpr(0))
        # TODO: Complete the visitor
        return value, type

    def visitAndExpr(self, ctx):
        value, type = self.visit(ctx.compExpr(0))
        # TODO: Complete the visitor
        return value, type

    def visitCompExpr(self, ctx):
        value, type = self.visit(ctx.numExpr(0))
        # TODO: Complete the visitor
        # TODO: Only accept NUMBER 
        return value, type

    def visitNumExpr(self, ctx):
        value, type = self.visit(ctx.mulExpr(0))
        # TODO: Complete the visitor
        # Only accept NUMBER and NUMBER
        return value, type

    def visitMulExpr(self, ctx):
        value, type = self.visit(ctx.invExpr(0))
        for i in range(1, len(ctx.invExpr())):
            next_value, next_type = self.visit(ctx.invExpr(i))
            # TODO: Get operator type
            # TODO: For types NUMBER and NUMBER, just do normal int math
            # TODO: For types NUMBER and UNIT (or UNIT and NUMBER) change type to MULTI_UNIT
            # and change value to a new MultiUnit object
        return value, type

    def visitInvExpr(self, ctx):
        value, type = self.visit(ctx.baseExpr())
        if ctx.NOT():
            if type != 6:
                raise Exception(f"Type Error: Cannot apply '{ctx.NOT().getText()}' operator to type {type}")
            value = not value
        elif ctx.MINUS():
            if type != 5:
                raise Exception(f"Type Error: Cannot apply '{ctx.MINUS().getText()}' operator to type {type}")
            value = -value
        return value, type
    
    def visitBaseExpr(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            value, type = self.scope.get_value(name), self.scope.get_type(name)
        elif ctx.unitExpr():
            value, type = self.visit(ctx.unitExpr()), 0
        elif ctx.NUMBER():
            value, type = int(ctx.NUMBER().getText()), 5
        elif ctx.BOOLEAN():
            value, type = ctx.BOOLEAN().getText() == "TRUE", 6
        elif ctx.expression():
            value, type = self.visit(ctx.expression())
            if ctx.getChild(0).getText() == '[':
                if type > 3:
                    raise Exception(f"Type Error: Cannot cast type {types[type]} to another type")
                match type:
                    case 0:
                        value = MultiUnit(u=value)
                    case 1:
                        value = Layer(units=value.extract_units())
                    case 2:
                        value = Shape(layers=[value])
                    case 3:
                        value = Model(shapes=[value])
                type += 1
        return value, type
    
    def visitUnitExpr(self, ctx):
        color, pattern = None, None
        if ctx.COLOR():
            color = ctx.COLOR().getText()[1:-1]
        if ctx.PATTERN():
            pattern = ctx.PATTERN().getText()[1:-1]
        return Unit(color=color, pattern=pattern)

    def visitBendStatement(self, ctx):
        shape = ctx.ID().getText()
        # TODO: Check if shape has type SHAPE

    def visitShowStatement(self, ctx):
        if ctx.getChildCount() == 2:
            shape_name = ctx.ID().getText()

            if shape_name not in self.scope:
                print(f"Error: '{shape_name}' is not defined.")
                return

            # TODO: Check if value is initialized 
            structure = self.scope.get_value(shape_name)
            if isinstance(structure, Structure):
                return show_figure(self.fig, structure)
            else:
                print(f"SHOW only supports STRUCTUREs, not {type(structure)}.")

        else:
            raise Exception("Invalid instruction")