from antlr4 import *
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from interpreter.ConnectITLexer import ConnectITLexer
from interpreter.ConnectITParser import ConnectITParser
from interpreter.ConnectITVisitor import ConnectITVisitor

from data_types import *
from utils import *

class CustomVisitor(ConnectITVisitor):
    def __init__(self, scope):
        self.scope = scope
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
        if ctx.declaration():
            return self.visit(ctx.declaration())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.showStatement():
            return self.visit(ctx.showStatement())
        else:
            raise Exception("Invalid statement")

    def visitNewUnits(self, ctx):
        for unit in ctx.unitDeclarationList().unitDeclaration():
            name = unit.getChild(0).getText()
            color, pattern = None, None
            if unit.unitExpr():
                color, pattern = self.visit(unit.unitExpr())
            else:
                source = unit.getChild(2).getText()
                # TODO: Raise exception if name is not defined or not of type UNIT
                source = self.variables[source]
                color, pattern = source.color, source.pattern
            self.scope[name] = Unit(color=color, pattern=pattern)
            print(color, pattern)
        return None

    def visitUnitExpr(self, ctx):
        color, pattern = None, None
        if ctx.COLOR():
            color = ctx.COLOR().getText()[1:-1]
        if ctx.PATTERN():
            pattern = ctx.PATTERN().getText()[1:-1]
        return color, pattern
    
    def visitNewLayers(self, ctx):
        for layer in ctx.layerDeclarationList().layerDeclaration():
            name = layer.getChild(0).getText()
            units = []
            closed = (
                layer.getChildCount() == 2 and layer.getChild(1).getText() == "CLOSED"
                or layer.getChildCount() == 4 and layer.getChild(3).getText() == "CLOSED"
            )
            if layer.layerExpr():
                units = self.visit(layer.layerExpr())
            else:
                source = layer.getChild(2).getText()
                # TODO: Raise exception if name is not defined or not of type UNIT or LAYER
                source = self.scope[source]
                if source["type"] == "UNIT":
                    units = [source["value"]]
                else:
                    units, closed = source["value"].units, source["value"].closed
            self.scope[name] = Layer(units=units, closed=closed)
        return None

    def visitLayerExpr(self, ctx):
        if ctx.getChild(1).getText() == '*':
            name = ctx.ID().getText()
            unit: Unit = self.variables[name]
            length: str = ctx.NUMBER().getText()
            return [unit] * int(length)
        
        else:
            units_left = self.visit(ctx.layerExpr(0))
            units_right = self.visit(ctx.layerExpr(1))
            return units_left + units_right

    def visitNewShapes(self, ctx):
        for shape in ctx.shapeDeclarationList().shapeDeclaration():
            name = shape.getChild(0).getText()
            layers, connections = [], {}
            if shape.shapeExpr():
                layers, connections = self.visit(shape.shapeExpr())
            else:
                source = shape.getChild(2).getText()
                # TODO: Raise exception if name is not defined or not of type UNIT, LAYER, or SHAPE
                source = self.variables[source]
                if source["type"] == "UNIT":
                    layers = [Layer([source["value"], False])]
                elif source["type"] == "LAYER":
                    layers = [source["value"]]
                else:
                    layers, connections = source["value"].layers, source["value"].connections
            self.scope[name] = Shape(layers=layers, connections=connections)
        return None

    def visitShapeExpr(self, ctx):
        if ctx.shapeExpr():
            if ctx.layerExpr():
                left = [Layer(self.visit(ctx.layerExpr()))]
            else:
                source = ctx.ID().getText()
                # TODO: Raise exception if name is not defined or not of type LAYER
                source = self.scope[source]
                left = [source["value"]]
            right, connections = self.visit(ctx.shapeExpr())

            if ctx.getChild(1).getText() == '<-':
                if ctx.NUMBER():
                    return left + right, [{"type": 1, "shift": int(ctx.NUMBER().getText())}] + connections
                return left + right, [{"type": 1, "shift": 0}]  + connections

            elif ctx.getChild(1).getText() == '<<-':
                if ctx.NUMBER():
                    return left + right, [{"type": 0, "shift": int(ctx.NUMBER().getText())}]  + connections
                return left + right, [{"type": 0, "shift": 0}]  + connections

        else:
            if ctx.layerExpr():
                return [Layer(self.visit(ctx.layerExpr()))], []
            else:
                source = ctx.ID().getText()
                # TODO: Raise exception if name is not defined or not of type LAYER
                source = self.variables[source]
                return [source["value"]], []

    def visitNewModels(self, ctx):
        for model in ctx.modelDeclarationList().modelDeclaration():
            name = model.getChild(0).getText()
            layers, connections = [], {}
            if model.modelExpr():
                layers, connections = self.visit(model.modelExpr())
            else:
                source = model.getChild(2).getText()
                # TODO: Raise exception if name is not defined or not of type UNIT, LAYER, or SHAPE
                source = self.variables[source]
                if source["type"] == "UNIT":
                    layers = [Layer([source["value"], False])]
                elif source["type"] == "LAYER":
                    layers = [source["value"]]
                else:
                    layers, connections = source["value"].layers, source["value"].connections
            self.scope[name] = Shape(layers=layers, connections=connections)
        return None

    def visitModelExpr(self, ctx):
        if ctx.shapeExpr():
            if ctx.layerExpr():
                left = [Layer(self.visit(ctx.layerExpr()))]
            else:
                source = ctx.ID().getText()
                # TODO: Raise exception if name is not defined or not of type LAYER
                source = self.scope[source]
                left = [source["value"]]
            right, connections = self.visit(ctx.shapeExpr())

            if ctx.getChild(1).getText() == '<-':
                if ctx.NUMBER():
                    return left + right, [{"type": 1, "shift": int(ctx.NUMBER().getText())}] + connections
                return left + right, [{"type": 1, "shift": 0}]  + connections

            elif ctx.getChild(1).getText() == '<<-':
                if ctx.NUMBER():
                    return left + right, [{"type": 0, "shift": int(ctx.NUMBER().getText())}]  + connections
                return left + right, [{"type": 0, "shift": 0}]  + connections

        else:
            if ctx.layerExpr():
                return [Layer(self.visit(ctx.layerExpr()))], []
            else:
                source = ctx.ID().getText()
                # TODO: Raise exception if name is not defined or not of type LAYER
                source = self.variables[source]
                return [source["value"]], []

    def visitShowStatement(self, ctx):
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