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
            return {
                "type": "error",
                "message": "Invalid statement"
            }
        
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
            raise Exception (f"Type Error: Cannot assign {types[received_type]} to {types[expected_type]} at line {line}, column {column}.")
        

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

        if op.getText() not in ['<+->']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Layer.")
            
        if received_type not in [0, 1]:  
            raise Exception(f"Cannot add value of type '{types[received_type]}' to a Layer.")
            
        
        if received_type == 0:
            value.add_unit(received_value)
        elif received_type == 1:
            value.add_multi_unit(received_value)
        return value
    
    def extendShape(self, value, e, op):

        if op.getText() in ['+=', '<+->']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Shape.")
            
        if received_type != 2: 
            raise Exception(f"Cannot add value of type '{types[received_type]}' to a Shape. Only LAYER can be added.")
            
        
        c = self.get_connection(op)
        received_value, received_type = self.visit(e)
        # TODO: If shape is closed, make sure the new layer is also closed
        # TODO: If shape is closed, make sure the new layer is the same length as previous ones
        # TODO: Make sure shift does not exceed the previous layer length
        value.add_layer(received_value, c)
        return value
    
    def extendModel(self, value, e, op):

        if op.getText() not in ['+=', '<+->']:               
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Model.")
            
        if received_type != 3: 
            raise Exception(f"Cannot add value of type '{types[received_type]}' to a Model. Only SHAPE can be added.")
                
        c = self.get_connection(op)
        received_value, received_type = self.visit(e)
        value.add_shape(received_value, c)
        return value
    
    def extendNumber(self, value, e, op):
        if op.getText() not in ['+=', '-=', '*=', '/=']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a NUMBER.")
            
        received_value, received_type = self.visit(e)
        if received_type != 5: 
            if op.getText() == '+=':
                raise Exception(f"Cannot add value of type '{types[received_type]}' to a NUMBER.")
            elif op.getText() == '-=':
                raise Exception(f"Cannot subtract value of type '{types[received_type]}' from a NUMBER.")
            elif op.getText() == '*=':
                raise Exception(f"Cannot multiply value of type '{types[received_type]}' to a NUMBER.")
            elif op.getText() == '/=':
                raise Exception(f"Cannot divide value of type '{types[received_type]}' from a NUMBER.")
            
        if op.getText() == '+=':
            value += received_value
        elif op.getText() == '-=':
            value -= received_value
        elif op.getText() == '*=':
            value *= received_value
        elif op.getText() == '/=':
            if received_value == 0:
                raise Exception("Value Error: Division by zero error.")
            value //= received_value
        return value
    
    def get_connection(self, operator):
        type = 1
        shift = 0
        if "<<" in operator.getText():
            type = 0
        if operator.expression():
            shift_val, shift_type = self.visit(operator.expression())
            if shift_type != 5: 
                raise Exception(f"Shift value must be of type NUMBER, not '{types[shift_type]}'.")
                
            shift = shift_val
        return {"type": type, "shift": shift}

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
                    raise Exception(f"Cannot use connectors with type '{types[type]}'.")
                    
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
                
                    raise Exception( f"Type Error: Cannot use '{op.getText()}' connector when creating a LAYER")
                
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
            c = self.get_connection(op)
            # TODO: If shape is closed, make sure the new layer is also closed
            # TODO: If shape is closed, make sure the new layer is the same length as previous ones
            # TODO: Make sure shift does not exceed the previous layer length
            
            result.add_layer(l=next_value, c = c)
            
        return result

    def createModel(self, ctx):
        first, _ = self.visit(ctx.logicExpr(0))
        result = Model(shapes=[first])

        for i in range(1, len(ctx.logicExpr())):
            next_value, next_type = self.visit(ctx.logicExpr(i))
            op = ctx.getChild(2*i-1)
            
            if next_type != 3:
                return {
                        "type": "error",
                        "message": f"Type Error: Cannot connect types SHAPE and {types[next_type]}"
                    }

            c = self.get_connection(op)

            result.add_shape(s=next_value, c=c)

        return result

    def visitLogicExpr(self, ctx):
        value, type = self.visit(ctx.andExpr(0))
        for i in range(1, len(ctx.andExpr())):
            next_value, next_type = self.visit(ctx.andExpr(i))
            if next_type != 6:
                raise Exception(f"Type Error: Logical operations can only be applied to BOOLEAN, not {types[next_type]}")
            value = value or next_value

        return value, type

    def visitAndExpr(self, ctx):
        value, type = self.visit(ctx.compExpr(0))
        for i in range(1, len(ctx.compExpr())):
            next_value, next_type = self.visit(ctx.compExpr(i))
            if next_type != 6:
                raise Exception(f"Type Error: Logical operations can only be applied to BOOLEAN, not {types[next_type]}")
            value = value and next_value

        return value, type

    def visitCompExpr(self, ctx):
        value, type = self.visit(ctx.numExpr(0))
        if ctx.COMPARATOR():
            comparator = ctx.COMPARATOR().getText()
            next_value, next_type = self.visit(ctx.numExpr(1))
            if next_type != 5:
                raise Exception(f"Type Error: Comparisons can only be applied to NUMBER, not {types[next_type]}")

            match comparator:
                case "<":
                    return_value = value < next_value
                case "<=":
                    return_value = value <= next_value
                case ">":
                    return_value = value > next_value
                case ">=":
                    return_value = value >= next_value
                case "==":
                    return_value = value == next_value
                case "!=":
                    return_value = value != next_value
                case _:
                    raise Exception(f"Unknown comparator: {comparator}")

            return return_value, 6

        return value, type

    def visitNumExpr(self, ctx):
        value, type = self.visit(ctx.mulExpr(0))
        for i in range(1, len(ctx.mulExpr())):
            next_value, next_type = self.visit(ctx.mulExpr(i))
            if next_type != 5:
                raise Exception(f"Type Error: Arithmetic operations can only be applied to NUMBER, not {types[next_type]}")
            
            if ctx.PLUS():
                value += next_value
            elif ctx.MINUS():
                value -= next_value

        return value, type

    def visitMulExpr(self, ctx):
        value, type = self.visit(ctx.invExpr(0))
        for i in range(1, len(ctx.invExpr())):
            next_value, next_type = self.visit(ctx.invExpr(i))
            if ctx.MUL():
                if type == 5 and next_type == 5:
                    value *= next_value
                elif (type == 5 and next_type == 0) or (type == 0 and next_type == 5):
                    unit = value if type == 0 else next_value
                    number = value if type == 5 else next_value
                    if number <= 0:
                        raise Exception("Value Error: Cannot multiply UNIT by negative number.")
                    value = MultiUnit(unit, number)
                    type = 1
                else:
                    raise Exception(f"Type Error: Cannot apply '*' operator to types {types[type]} and {types[next_type]}")
            elif ctx.DIV():
                if type == 5 and next_type == 5:
                    if next_value == 0:
                        raise Exception("Value Error: Division by zero error.")
                    value //= next_value
                else:
                    raise Exception(f"Type Error: Cannot apply '/' operator to types {types[type]} and {types[next_type]}")
        return value, type

    def visitInvExpr(self, ctx):
        value, type = self.visit(ctx.baseExpr())
        if ctx.NOT():
            if type != 6:
                raise Exception(f"Type Error: Cannot apply '{ctx.NOT().getText()}' operator to type {types[type]}")
            value = not value
        elif ctx.MINUS():
            if type != 5:
                raise Exception(f"Type Error: Cannot apply '{ctx.MINUS().getText()}' operator to type {types[type]}")
            value = -value
        return value, type
    
    def visitBaseExpr(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            if not self.scope.__contains__(name):
                raise Exception(f"Type Error: {name} is not defined")
            value, type = self.scope.get_value(name), self.scope.get_type(name)
            if value is None:
                raise Exception(f"Type Error: {name} has no value")
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
                        closed = ctx.getChildCount() % 2 == 0
                        value = Layer(units=value.extract_units(), closed=closed)
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

            if shape_name not in self.scope:
                return {
                    "type": "error",
                    "message": f"Structure '{shape_name}' is not defined."
                }

            structure = self.scope.get_value(shape_name)

            if isinstance(structure, dict) and structure.get("type") == "error":
                return structure
            
            if isinstance(structure, Structure):
                return show_figure(self.fig, structure)
            else:
                return {
                    "type": "error",
                    "message": f"SHOW only supports STRUCTUREs, not {type(structure)}."
                }

    def visitIfStmt(self, ctx):
        condition_value, condition_type = self.visit(ctx.logicExpr(0))
        if condition_type != 6:
            raise Exception(f"Type Error: IF condition must be BOOLEAN, not {types[condition_type]}.")
        
        if condition_value:
            return self.visit(ctx.statementBlock(0))
        
        for i in range(1, len(ctx.logicExpr())):
            condition_value, condition_type = self.visit(ctx.logicExpr(i))
            if condition_type != 6:
                raise Exception(f"Type Error: ELSE IF condition must be BOOLEAN, not {types[condition_type]}.")      
            if condition_value:
                return self.visit(ctx.statementBlock(i))
        
        if len(ctx.statementBlock()) > len(ctx.logicExpr()):
            return self.visit(ctx.statementBlock(len(ctx.statementBlock())))
    
    def visitStatementBlock(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)
        return None