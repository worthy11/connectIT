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
        received_type = self.getExpressionType(ctx.expression())
        # TODO: Raise exception if types don't match
        if expected_type != received_type:
            raise Exception(f"Error: Types {types[expected_type]} and {types[received_type]} don't match at line {line}, column {column}")
        value = self.visit(ctx.expression())
        self.scope.fill(name, value)

    def getExpressionType(self, e):
        if e.idCast():
            return self.getCastType(e.idCast())[1]
        elif e.unitExpr():
            return 0
        elif e.layerExpr():
            return 1
        elif e.shapeExpr():
            return 2
        elif e.modelExpr():
            return 3
        elif e.numericExpr():
            return 4
        elif e.booleanExpr():
            return 5
        
    def getCastType(self, cast):
        base_type = 0
        cast_type = 0
        if cast.idCast():
            result = self.getCastType(cast.idCast())
            base_type = result[0]
            cast_type = result[1] + 1
        else:
            base_type = self.scope.get_type(cast.ID().getText())
            cast_type = base_type
            if base_type > 2:
                raise Exception(f"Error: Cannot cast {types[base_type]} to another type")
        if cast_type > 3:
            raise Exception(f"Error: Cannot cast {types[base_type]} to a type other than LAYER, SHAPE, or MODEL")
        return base_type, cast_type
        
    def visitExpression(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitIdCast(self, ctx):
        base_type, cast_type = self.getCastType(ctx)
        if ctx.idCast():
            value = self.visit(ctx.idCast())
            match base_type:
                case 2:
                    return Model()
                case 1:
                    if cast_type == 2:
                        return Shape(layers=[value], connections=[])
                    return Model()
                case 0:
                    if cast_type == 1:
                        return Layer(units=[value], closed=False)
                    elif cast_type == 2:
                        return Shape(layers=[Layer(units=[value], closed=False)], connections=[])
                    return Model()
        # TODO: Check if value is initialized
        return self.scope.get_value(ctx.ID().getText())

    def visitUnitExpr(self, ctx):
        color, pattern = None, None
        if ctx.COLOR():
            color = ctx.COLOR().getText()[1:-1]
        if ctx.PATTERN():
            pattern = ctx.PATTERN().getText()[1:-1]
        return Unit(color=color, pattern=pattern)
    
    def visitLayerExpr(self, ctx):
        units = []
        closed = ctx.getChildCount() % 2 == 0
        for term in ctx.layerTerm():
            units.extend(self.visit(term))
        return Layer(units=units, closed=closed)
    
    def visitLayerTerm(self, ctx):
        units = []
        number = 1
        if ctx.getChildCount() == 1:
            unit = self.visit(ctx.idCast())
        else:
            if ctx.numericExpr():
                if ctx.idCast():
                    unit = self.visit(ctx.idCast())
                else:
                    unit = self.visit(ctx.unitExpr())
                number = self.visit(ctx.numericExpr())
            else:
                unit = self.visit(ctx.unitExpr())
        # TODO: Check if unit is of type UNIT
        # TODO: Check if number is positive
        units.extend([unit] * number)
        return units

    def visitShapeExpr(self, ctx):
        layers = []
        connections = []
        layers.append(self.visit(ctx.shapeTerm()))
        for con in ctx.shapeConnector():
            layer, connection = self.visit(con)
            layers.append(layer)
            connections.append(connection)
        # TODO: Raise exception if only some layers are closed
        # TODO: Raise exception if layer length varies if all layers are closed
        # TODO: Raise exception if shift is larger than the length of the previous layer
        return Shape(layers=layers, connections=connections)
    
    def visitShapeConnector(self, ctx):
        layer = self.visit(ctx.shapeTerm())
        shift = 0
        if ctx.numericExpr():
            shift = self.visit(ctx.numericExpr())
        if ctx.getChild(0).getText() == "<-":
            type = 1
        else:
            type = 0
        connection = {"type": type, "shift": shift}
        return layer, connection
    
    def visitShapeTerm(self, ctx):
        if ctx.idCast():
            layer = self.visit(ctx.idCast())
        else:
            layer = self.visit(ctx.layerExpr())
        # TODO: Check if layer is of type LAYER
        return layer

    def visitModelExpr(self, ctx):
        pass
    def visitModelConnector(self, ctx):
        pass

    def visitModelTerm(self, ctx):
        if ctx.idCast():
            shape = self.visit(ctx.idCast())
        else:
            shape = self.visit(ctx.shapeExpr())
        # TODO: Check if shape is of type SHAPE
        return shape

    def visitNumericExpr(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            # TODO: Raise exception if name is not defined
            type = self.scope.get_type(name)
            # TODO: Raise exception if name is not of type NUMBER
            # TODO: Check if value is initialized 
            value = self.scope.get_value(name)
            return value
        else:
            return int(ctx.NUMBER().getText())

    def visitBooleanExpr(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            # TODO: Raise exception if name is not defined
            type = self.scope.get_type(name)
            # TODO: Raise exception if name is not of type BOOLEAN
            # TODO: Check if value is initialized 
            value = self.scope.get_value(name)
            return value
        else:
            value: str = ctx.BOOLEAN().getText()
            if value.isdigit():
                return int(value)
            elif value == "TRUE":
                return 1
            else:
                return 0

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