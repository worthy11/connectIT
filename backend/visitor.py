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
        return output
    
    def visitStatement(self, ctx):
        if ctx.getChildCount() > 1 and ctx.getChild(0).getText() == "?":
            return None
        if ctx.declarationList():
            return self.visit(ctx.declarationList())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.extension():
            return self.visit(ctx.extension())
        if ctx.showStatement():
            return self.visit(ctx.showStatement())
        if ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        else:
            line = ctx.start.line
            column = ctx.start.column
            return {
                "type": "error",
                "message": f"Invalid statement at line {line}, column {column}."
            }
        
    def visitDeclarationList(self, ctx):
        default = None
        match ctx.dataType().getText():
            case "UNIT":
                default = Unit()
            case "LAYER":
                default = Layer()
            case "SHAPE":
                default = Shape()
            case "MODEL":
                default = Model()
            case "NUMBER":
                default = 0
            case "BOOLEAN":
                default = False
        for dec in ctx.declaration():
            if dec.assignment():
                self.visit(dec.assignment())
            else:
                name = dec.ID().getText()
                self.scope.fill(name, default)
        return None

    def visitAssignment(self, ctx):
        token = ctx.ID().getSymbol()
        line = token.line
        column = token.column
        name = token.text
            
        expected_type = self.scope.get_type(name)
        value, received_type = self.visit(ctx.expression())
        if expected_type != received_type:
            raise Exception(f"Type Error: Cannot assign {types[received_type]} to {types[expected_type]} at line {line}, column {column}.")

        self.scope.fill(name, value)
        return None
    

    def visitExtension(self, ctx):
        token = ctx.ID().getSymbol()
        line = token.line
        column = token.column
        name = token.text

        value, expected_type = self.scope.get_value(name), self.scope.get_type(name)
        e, op = ctx.expression(), ctx.extensionOperator()
        if expected_type not in [2, 3, 4, 5]:            
            raise Exception(f"Type Error: Cannot add new values to type {types[expected_type]} at line {line}, column {column}.")
            
        match expected_type:
            case 2:
                new_value = self.extendLayer(value, e, op)
            case 3:
                new_value = self.extendShape(value, e, op)
            case 4:
                new_value = self.extendModel(value, e, op)
            case 5:
                new_value = self.extendNumber(value, e, op)
        self.scope.fill(name, new_value)

        return None

    def extendLayer(self, value, e, op):
        received_value, received_type = self.visit(e)
        line = op.start.line
        column = op.start.column

        if op.getText() not in ['<+->']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Layer at line {line}, column {column}.")
            
        if received_type not in [0, 1]:  
            raise Exception(f"Cannot add value of type '{types[received_type]}' to a Layer at line {line}, column {column}.")
            
        
        if received_type == 0:
            value.add_unit(received_value)
        elif received_type == 1:
            value.add_multi_unit(received_value)
        return value
    
    def extendShape(self, value, e, op):
        line = op.start.line
        column = op.start.column
        received_value, received_type = self.visit(e)

        if op.getText() in ['+=', '<+->']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Shape at line {line}, column {column}.")
            
        if received_type != 2: 
            raise Exception(f"Type Error: Cannot add value of type '{types[received_type]}' to a Shape. Only LAYER can be added at line {line}, column {column}.")
            
        
        c = self.get_connection(op)
 
        # TODO: If shape is closed, make sure the new layer is also closed
        # TODO: If shape is closed, make sure the new layer is the same length as previous ones
        # TODO: Make sure shift does not exceed the previous layer length


        shape_closed = any(layer.is_closed() for layer in value.layers)

        if shape_closed:
            if not received_value.is_closed():
                raise Exception(f"Type Error: Cannot add an open layer to a closed shape at line {line}, column {column}.")

            if len(received_value) != len(value.layers[0]):
                raise Exception(f"Type Error: New layer must have {len(value.layers[0])} units (same as existing layers) because the shape is closed at line {line}, column {column}.")

        if not shape_closed:
            if received_value.is_closed():
                raise Exception(f"Type Error: Cannot add a closed layer to an open shape at line {line}, column {column}.")

        value.add_layer(received_value, c)
        return value
        
    
    def extendModel(self, value, e, op):
        line = op.start.line
        column = op.start.column
        received_value, received_type = self.visit(e)

        if op.getText() not in ['+=', '<+->']:               
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Model at line {line}, column {column}.")
            
        if received_type != 3: 
            raise Exception(f"Cannot add value of type '{types[received_type]}' to a Model. Only SHAPE can be added at line {line}, column {column}.")
                
        c = self.get_connection(op)
        value.add_shape(received_value, c)
        return value
    
    def extendNumber(self, value, e, op):
        line = op.start.line
        column = op.start.column
        if op.getText() not in ['+=', '-=', '*=', '/=']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a NUMBER at line {line}, column {column}.")
            
        received_value, received_type = self.visit(e)
        if received_type != 5: 
            if op.getText() == '+=':
                raise Exception(f"Cannot add value of type '{types[received_type]}' to a NUMBER at line {line}, column {column}.")
            elif op.getText() == '-=':
                raise Exception(f"Cannot subtract value of type '{types[received_type]}' from a NUMBER at line {line}, column {column}.")
            elif op.getText() == '*=':
                raise Exception(f"Cannot multiply value of type '{types[received_type]}' to a NUMBER at line {line}, column {column}.")
            elif op.getText() == '/=':
                raise Exception(f"Cannot divide value of type '{types[received_type]}' from a NUMBER at line {line}, column {column}.")
            
        if op.getText() == '+=':
            value += received_value
        elif op.getText() == '-=':
            value -= received_value
        elif op.getText() == '*=':
            value *= received_value
        elif op.getText() == '/=':
            if received_value == 0:
                raise Exception(f"Value Error: Division by zero error at line {line}, column {column}.")
            value //= received_value
        return value
    
    def get_connection(self, operator):
        type = 1
        shift = 0
        if "<<" in operator.getText():
            type = 0
        if operator.expression():
            line = operator.start.line
            column = operator.start.column
            shift_val, shift_type = self.visit(operator.expression())
            if shift_type != 5: 
                raise Exception(f"Shift value must be of type NUMBER, not '{types[shift_type]}' at line {line}, column {column}.")
                
            shift = shift_val
        return {"type": type, "shift": shift}

    def visitExpression(self, ctx):
        value, type = self.visit(ctx.logicExpr(0))
        if ctx.getChildCount() % 2 == 0:
            if type == 2:
                value.set_closed(True)
            else:
                line = ctx.start.line
                column = ctx.start.column
                raise Exception(f"Cannot use CLOSED keyword with type {types[type]} at line {line}, column {column}.")
        if ctx.arrowOperator():
            line = ctx.start.line
            column = ctx.start.column
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
                    raise Exception(f"Cannot use connectors with type '{types[type]}' at line {line}, column {column}.")
                    
        return value, type

    def createLayer(self, ctx):
        value, _ = self.visit(ctx.logicExpr(0))
        first = value.extract_units()
        closed = ctx.getChildCount() % 2 == 0
        result = Layer(units=first, closed=closed)
    
        for i in range(1, len(ctx.logicExpr())):
            next_value, next_type = self.visit(ctx.logicExpr(i))
            
            op = ctx.getChild(2*i-1)
            line = op.start.line
            column = op.start.column
            if next_type != 1:
                raise Exception(f"Type Error: Can only apply '<->' connector to multiples of UNITs, not {types[next_type]} at line {line}, column {column}.")
                
            if op.getText() != "<->":
                raise Exception(f"Type Error: Cannot use '{op.getText()}' connector when creating a LAYER at line {line}, column {column}.")
                
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
            line = op.start.line
            column = op.start.column
            if next_type != 2:
                raise Exception(f"Type Error: Cannot connect types LAYER and {types[next_type]} at line {line}, column {column}.")
            c = self.get_connection(op)
            # TODO: If shape is closed, make sure the new layer is also closed
            # TODO: If shape is closed, make sure the new layer is the same length as previous ones
            # TODO: Make sure shift does not exceed the previous layer length

            shape_closed = any(layer.is_closed() for layer in result.layers)

            if shape_closed:
                if not next_value.is_closed():
                    raise Exception(f"Type Error: Cannot add an open layer to a closed shape at line {line}, column {column}.")

                if len(next_value) != len(result.layers[0]):
                    raise Exception(f"Type Error: New layer must have the same number of units as existing layers in the shape at line {line}, column {column}.")

            if not shape_closed:
                if next_value.is_closed():
                    raise Exception(f"Type Error: Cannot add a closed layer to an open shape at line {line}, column {column}.")
            
            result.add_layer(l=next_value, c = c)
            
        return result

    def createModel(self, ctx):
        first, _ = self.visit(ctx.logicExpr(0))
        result = Model(shapes=[first])

        for i in range(1, len(ctx.logicExpr())):
            next_value, next_type = self.visit(ctx.logicExpr(i))
            op = ctx.getChild(2*i-1)
            line = op.start.line
            column = op.start.column
            
            if next_type != 3:
                return {
                        "type": "error",
                        "message": f"Type Error: Cannot connect types SHAPE and {types[next_type]} at line {line}, column {column}."
                    }

            c = self.get_connection(op)

            result.add_shape(s=next_value, c=c)

        return result

    def visitLogicExpr(self, ctx):
        value, type = self.visit(ctx.andExpr(0))
        for i in range(1, len(ctx.andExpr())):
            next_value, next_type = self.visit(ctx.andExpr(i))
            line = ctx.start.line
            column = ctx.start.column
            if next_type != 6:
                raise Exception(f"Type Error: Logical operations can only be applied to BOOLEAN, not {types[next_type]} at line {line}, column {column}.")
            value = value or next_value

        return value, type

    def visitAndExpr(self, ctx):
        value, type = self.visit(ctx.compExpr(0))
        for i in range(1, len(ctx.compExpr())):
            next_value, next_type = self.visit(ctx.compExpr(i))
            line = ctx.start.line
            column = ctx.start.column
            if next_type != 6:
                raise Exception(f"Type Error: Logical operations can only be applied to BOOLEAN, not {types[next_type]} at line {line}, column {column}.")
            value = value and next_value

        return value, type

    def visitCompExpr(self, ctx):
        value, type = self.visit(ctx.numExpr(0))
        if ctx.COMPARATOR():
            comparator = ctx.COMPARATOR().getText()
            next_value, next_type = self.visit(ctx.numExpr(1))
            line = ctx.COMPARATOR().getSymbol().line
            column = ctx.COMPARATOR().getSymbol().column
            if type != next_type or type not in [5, 6]:
                raise Exception(f"Type Error: Comparisons can only be applied to NUMBER or BOOLEAN, not {types[next_type]} at line {line}, column {column}.")

            match comparator:
                case "<":
                    if type == 5:
                        value = value < next_value
                    else:
                        raise Exception(f"Type Error: Cannot apply '<' operator to types {types[type]} and {types[next_type]} at line {line}, column {column}.")
                case "<=":
                    if type == 5:
                        value = value <= next_value
                    else:
                        raise Exception(f"Type Error: Cannot apply '<=' operator to types {types[type]} and {types[next_type]} at line {line}, column {column}.")
                case ">":
                    if type == 5:
                        value = value > next_value
                    else:
                        raise Exception(f"Type Error: Cannot apply '>' operator to types {types[type]} and {types[next_type]} at line {line}, column {column}.")
                case ">=":
                    if type == 5:
                        value = value >= next_value
                    else:
                        raise Exception(f"Type Error: Cannot apply '>=' operator to types {types[type]} and {types[next_type]} at line {line}, column {column}.")
                case "==":
                    value = value == next_value
                case "!=":
                    value = value != next_value
                case _:
                    raise Exception(f"Unknown comparator: {comparator} at line {line}, column {column}.")

            return value, 6

        return value, type

    def visitNumExpr(self, ctx):
        value, type = self.visit(ctx.mulExpr(0))
        for i in range(1, len(ctx.mulExpr())):
            next_value, next_type = self.visit(ctx.mulExpr(i))
            line = ctx.start.line
            column = ctx.start.column
            if next_type != 5:
                raise Exception(f"Type Error: Arithmetic operations can only be applied to NUMBER, not {types[next_type]} at line {line}, column {column}.")
            
            if ctx.PLUS():
                value += next_value
            elif ctx.MINUS():
                value -= next_value
                
        return value, type

    def visitMulExpr(self, ctx):
        value, type = self.visit(ctx.invExpr(0))
        for i in range(1, len(ctx.invExpr())):
            next_value, next_type = self.visit(ctx.invExpr(i))
            line = ctx.start.line
            column = ctx.start.column
            if ctx.MUL():
                if type == 5 and next_type == 5:
                    value *= next_value
                elif (type == 5 and next_type == 0) or (type == 0 and next_type == 5):
                    unit = value if type == 0 else next_value
                    number = value if type == 5 else next_value
                    if number <= 0:
                        raise Exception(f"Value Error: Cannot multiply UNIT by non-positive number at line {line}, column {column}.")
                    value = MultiUnit(unit, number)
                    type = 1
                else:
                    raise Exception(f"Type Error: Cannot apply '*' operator to types {types[type]} and {types[next_type]} at line {line}, column {column}.")
            elif ctx.DIV():
                if type == 5 and next_type == 5:
                    if next_value == 0:
                        raise Exception(f"Value Error: Division by zero error at line {line}, column {column}.")
                    value //= next_value
                else:
                    raise Exception(f"Type Error: Cannot apply '/' operator to types {types[type]} and {types[next_type]} at line {line}, column {column}.")
        return value, type

    def visitInvExpr(self, ctx):
        value, type = self.visit(ctx.baseExpr())
        if ctx.NOT():
            line = ctx.NOT().getSymbol().line
            column = ctx.NOT().getSymbol().column
            if type != 6:
                raise Exception(f"Type Error: Cannot apply '{ctx.NOT().getText()}' operator to type {types[type]} at line {line}, column {column}.")
            value = not value
        elif ctx.MINUS():
            line = ctx.MINUS().getSymbol().line
            column = ctx.MINUS().getSymbol().column
            if type != 5:
                raise Exception(f"Type Error: Cannot apply '{ctx.MINUS().getText()}' operator to type {types[type]} at line {line}, column {column}.")
            value = -value
        return value, type
    
    def visitBaseExpr(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            line = ctx.ID().getSymbol().line
            column = ctx.ID().getSymbol().column
            if not self.scope.__contains__(name):
                raise Exception(f"Type Error: {name} is not defined at line {line}, column {column}.")
            value, type = self.scope.get_value(name).__copy__(), self.scope.get_type(name)
            if value is None:
                raise Exception(f"Type Error: {name} has no value at line {line}, column {column}.")
        elif ctx.unitExpr():
            value, type = self.visit(ctx.unitExpr()), 0
        elif ctx.NUMBER():
            value, type = int(ctx.NUMBER().getText()), 5
        elif ctx.BOOLEAN():
            value, type = ctx.BOOLEAN().getText() == "TRUE", 6
        elif ctx.expression():
            value, type = self.visit(ctx.expression())
            if ctx.getChild(0).getText() == '[':
                line = ctx.start.line
                column = ctx.start.column
                if type > 3:
                    raise Exception(f"Type Error: Cannot cast type {types[type]} to another type at line {line}, column {column}.")
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

    def visitShowStatement(self, ctx):
        if ctx.getChildCount() == 2:
            shape_name = ctx.ID().getText()
            line = ctx.ID().getSymbol().line
            column = ctx.ID().getSymbol().column

            if shape_name not in self.scope:
                return {
                    "type": "error",
                    "message": f"Structure '{shape_name}' is not defined at line {line}, column {column}."
                }

            structure = self.scope.get_value(shape_name)

            if isinstance(structure, dict) and structure.get("type") == "error":
                return structure
            
            if isinstance(structure, Structure):
                return show_figure(self.fig, structure)
            else:
                return {
                    "type": "error",
                    "message": f"SHOW only supports STRUCTUREs, not {type(structure)} at line {line}, column {column}."
                }

    def visitIfStmt(self, ctx):
        condition_value, condition_type = self.visit(ctx.logicExpr(0))
        line = ctx.start.line
        column = ctx.start.column
        if condition_type != 6: 
            raise Exception(f"Type Error: IF condition must be BOOLEAN, not {types[condition_type]} at line {line}, column {column}.")

        if condition_value:
            return self.visit(ctx.statementBlock(0))
        else:
            for i in range(1, len(ctx.logicExpr())):
                condition_value, condition_type = self.visit(ctx.logicExpr(i))
                elseLine = ctx.logicExpr(i).start.line
                elseColumn = ctx.logicExpr(i).start.column
                if condition_type != 6:
                    raise Exception(f"Type Error: ELSE IF condition must be BOOLEAN, not {types[condition_type]} at line {elseLine}, column {elseColumn}.")
                if condition_value:
                    return self.visit(ctx.statementBlock(i))

            if len(ctx.statementBlock()) > len(ctx.logicExpr()):
                return self.visit(ctx.statementBlock(len(ctx.statementBlock()) - 1))
    
    def visitStatementBlock(self, ctx):
        output = None
        for statement in ctx.statement():
            statement_output = self.visit(statement)
            if statement_output is not None:
                output = statement_output
        return output