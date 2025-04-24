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

    def visitAssignment(self, ctx):
        token = ctx.ID().getSymbol()
        line = token.line
        column = token.column
        name = token.text
        expected_type = self.scope.get_type(name)
        value, received_type = self.visit(ctx.expression())
        if expected_type != received_type:
            raise Exception(f"Error: Types {types[expected_type]} and {types[received_type]} don't match at line {line}, column {column}")
        value = self.visit(ctx.expression())
        self.scope.fill(name, value)

    def visitExpression(self, ctx):
        term, type = self.visit(ctx.logicExpr(0))
        terms = [term]
        connections = []

        for i in range(1, len(ctx.logicExpr())):
            operator = ctx.arrowOperator(i - 1).getText()
            next, next_type = self.visit(ctx.logicExpr(i))
            
            if next_type != type:
                raise Exception(f"Type Error: Cannot connect types {type} and {next_type}")

            if operator == "<->":
                if type != "MULTI_UNIT" or next_type != "MULTI_UNIT":
                    raise Exception(f"Type Error: Cannot connect type {type} using the '<->' connector")
            else:
                if type not in ["LAYER", "SHAPE"]:
                    raise Exception(f"Type Error: Cannot connect type {type} using the {operator.getText()} connector")
                shift = 0
                if operator.expression():
                    shift, type = self.visit(operator.expression())
                    if type != "NUMBER":
                        raise Exception(f"Type Error: Shift can only be a NUMBER, not {type}")
                if "<<" in operator.getText():
                    connections.append({"type": 0, "shift": shift})
                else:
                    connections.append({"type": 1, "shift": shift})
            terms.append(next)

        result = terms[0]
        match type:
            case "MULTI_UNIT":
                closed = ctx.getChildCount() % 2 == 0
                result = Layer(units=terms, closed=closed)
                type = "LAYER"
            case "LAYER":
                result = Shape(layers=terms, connections=connections)
                type = "SHAPE"
            case "SHAPE":
                result = Model(shapes=terms, connections=connections)
                type = "MODEL"
        return result, type

    def visitLogicExpr(self, ctx):
        value, type = self.visit(ctx.andExpr())
        # TODO: Complete the visitor
        return value, type

    def visitAndExpr(self, ctx):
        value, type = self.visit(ctx.compExpr())
        # TODO: Complete the visitor
        return value, type

    def visitCompExpr(self, ctx):
        value, type = self.visit(ctx.numExpr())
        # TODO: Complete the visitor
        return value, type

    def visitNumExpr(self, ctx):
        value, type = self.visit(ctx.mulExpr())
        # TODO: Complete the visitor
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
            if type != "BOOLEAN":
                raise Exception(f"Type Error: Cannot apply '{ctx.NOT().getText()}' operator to type {type}")
            value = not value
        elif ctx.MINUS():
            if type != "NUMBER":
                raise Exception(f"Type Error: Cannot apply '{ctx.MINUS().getText()}' operator to type {type}")
            value = -value
        return value, type
    
    def visitBaseExpr(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            value, type = self.scope.get_value(name), self.scope.get_type(name)
        elif ctx.unitExpr():
            value, type = self.visit(ctx.unitExpr()), "UNIT"
        elif ctx.NUMBER():
            value, type = int(ctx.NUMBER().getText()), "NUMBER"
        elif ctx.BOOLEAN():
            value, type = ctx.BOOLEAN().getText() == "TRUE", "BOOLEAN"
        elif ctx.expression():
            value, type = self.visit(ctx.expression())
            if ctx.getChild(0).getText() == '[':
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