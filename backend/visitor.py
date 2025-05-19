from antlr4 import *
from interpreter.ConnectITParser import ConnectITParser
from interpreter.ConnectITVisitor import ConnectITVisitor

from data_types import *
from utils import *

class CustomVisitor(ConnectITVisitor):
    def __init__(self, scopes):
        self.scopes = scopes
        self.current_scope = None
        self.call_stack = CallStack()
        self.call_stack.push(ActivationRecord("global", "program", 1))
        self.assigning = False
        self.declaring = False
        self.render = []
        self.fig = go.Figure()

    def format_scopes(self, scopes):
        output = []
        for ctx, scope in scopes.items():
            ctx_type = type(ctx).__name__
            scope_str = str(scope)
            output.append(f"{ctx_type}:\n{scope_str}\n")
        return "\n".join(output)

    def get_scope_for_ctx(self, ctx):
        while ctx is not None:
            if ctx in self.scopes:
                return self.scopes[ctx]
            ctx = ctx.parentCtx

    def visitProgram(self, ctx):
        self.current_scope = self.get_scope_for_ctx(ctx)
        output = None
        for i in range(ctx.getChildCount()):
            statement_output = self.visit(ctx.getChild(i))
            if isinstance(statement_output, str):
                if statement_output[0] == "{":
                    print(output)
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
        if ctx.showStmt():
            return self.visit(ctx.showStmt())
        if ctx.outStmt():
            return self.visit(ctx.outStmt())
        if ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        if ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        if ctx.forStmt():
            return self.visit(ctx.forStmt())
        if ctx.funcDec():
            return self.visit(ctx.funcDec())
        if ctx.funcCall():
            return self.visit(ctx.funcCall())
        if ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        else:
            line = ctx.start.line
            column = ctx.start.column
            return {
                "type": "error",
                "message": f"Invalid statement at line {line}, column {column}."
            }
        
    def visitDeclarationList(self, ctx):
        self.declaring = True
        for dec in ctx.declaration():
            if dec.assignment():
                self.visit(dec.assignment())
            else:
                name = dec.ID().getText()
                self.call_stack.peek().set(name, None)
        self.declaring = False
        return None

    def visitAssignment(self, ctx):
        scope = self.get_scope_for_ctx(ctx)
        line = ctx.start.line
        column = ctx.start.column

        self.assigning = True
        lvalue, _ = self.visit(ctx.expression(0))
        self.assigning = False

        if self.declaring:
            self.call_stack.peek().set(lvalue, None)

        expected_type = scope.get_type(lvalue)

        rvalue, rtype = self.visit(ctx.expression(1))
        if rtype != expected_type:
            raise Exception(f"Type Error: Cannot assign {rtype} to {expected_type} at line {line}, column {column}.")
        for ar in reversed(self.call_stack.records):
            if lvalue in ar.members:
                ar.set(lvalue, rvalue)
                return None
        raise Exception(f"Error: Cannot assign value to undeclared variable {lvalue} at line {line}, column {column}")
    
    def visitExtension(self, ctx):
        line = ctx.start.line
        column = ctx.start.column

        self.assigning = True
        name, expected_type = self.visit(ctx.expression(0))
        self.assigning = False
        e, op = ctx.expression(1), ctx.extensionOperator()
        if expected_type not in ["LAYER", "SHAPE", "MODEL", "NUMBER"]:            
            raise Exception(f"Type Error: Cannot add new values to type {expected_type} at line {line}, column {column}.")
            
        # TODO: Do zmiany

        for ar in reversed(self.call_stack.records):
            if name in ar.members:
                value = ar.get(name)
                match expected_type:
                    case "LAYER":
                        new_value = self.extendLayer(value, e, op)
                    case "SHAPE":
                        new_value = self.extendShape(value, e, op)
                    case "MODEL":
                        new_value = self.extendModel(value, e, op)
                    case "NUMBER":
                        new_value = self.extendNumber(value, e, op)
                ar.set(name, new_value)
                return None
        raise Exception(f"Error: Cannot apply {op} operator to undeclared variable {name} at line {line}, column {column}")

    def extendLayer(self, value, e, op):
        received_value, received_type = self.visit(e)
        line = op.start.line
        column = op.start.column

        if op.getText() not in ['<+->']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Layer at line {line}, column {column}.")
            
        if received_type not in ["UNIT", "MULTI_UNIT"]:  
            raise Exception(f"Cannot add value of type '{received_type}' to a Layer at line {line}, column {column}.")
            
        
        if received_type == "UNIT":
            value.add_unit(received_value)
        elif received_type == "MULTI_UNIT":
            value.add_multi_unit(received_value)
        return value
    
    def extendShape(self, value, e, op):
        line = op.start.line
        column = op.start.column
        received_value, received_type = self.visit(e)

        if op.getText() in ['+=', '<+->']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Shape at line {line}, column {column}.")
            
        if received_type != "LAYER": 
            raise Exception(f"Type Error: Cannot add value of type '{received_type}' to a Shape. Only LAYER can be added at line {line}, column {column}.")
            
        
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
            
        if received_type != "SHAPE": 
            raise Exception(f"Cannot add value of type '{received_type}' to a Model. Only SHAPE can be added at line {line}, column {column}.")
                
        c = self.get_connection(op)
        value.add_shape(received_value, c)
        return value
    
    def extendNumber(self, value, e, op):
        line = op.start.line
        column = op.start.column
        if op.getText() not in ['+=', '-=', '*=', '/=']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a NUMBER at line {line}, column {column}.")
            
        received_value, received_type = self.visit(e)
        if received_type != "NUMBER": 
            if op.getText() == '+=':
                raise Exception(f"Cannot add value of type '{received_type}' to a NUMBER at line {line}, column {column}.")
            elif op.getText() == '-=':
                raise Exception(f"Cannot subtract value of type '{received_type}' from a NUMBER at line {line}, column {column}.")
            elif op.getText() == '*=':
                raise Exception(f"Cannot multiply value of type '{received_type}' to a NUMBER at line {line}, column {column}.")
            elif op.getText() == '/=':
                raise Exception(f"Cannot divide value of type '{received_type}' from a NUMBER at line {line}, column {column}.")
            
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
                raise Exception(f"Shift value must be of type NUMBER, not '{shift_type}' at line {line}, column {column}.")
                
            shift = shift_val
        return {"type": type, "shift": shift}

    def visitExpression(self, ctx):
        value, type = self.visit(ctx.logicExpr(0))
        if ctx.getChildCount() % 2 == 0:
            # TODO: Do zmiany
            if type == "LAYER":
                if self.assigning:
                    raise Exception(f"Error: Cannot set a layer to CLOSED in a non-evaluating context at line {line}, column {column}.")
                value.set_closed(True)
            else:
                line = ctx.start.line
                column = ctx.start.column
                raise Exception(f"Cannot use CLOSED keyword with type {type} at line {line}, column {column}.")
        if ctx.arrowOperator():
            print(f"ctx: {ctx.getText()}")
            print(f"Result value={value}, type={type}")
            if self.assigning:
                raise Exception(f"Error: Cannot connect elements in a non-evaluating context at line {line}, column {column}.")
            line = ctx.start.line
            column = ctx.start.column
            match type:
                case "MULTI_UNIT":
                    value = self.createLayer(ctx)
                    type = "LAYER"
                case "LAYER":
                    value = self.createShape(ctx)
                    type = "SHAPE"
                case "SHAPE":
                    value = self.createModel(ctx)
                    type = "MODEL"
                case _:
                    print(f"Current_scope: {self.current_scope.name}")
                    raise Exception(f"Cannot use connectors with type '{type}' at line {line}, column {column}.")
                    
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
            if next_type != "MULTI_UNIT":
                raise Exception(f"Type Error: Can only apply '<->' connector to multiples of UNITs, not {next_type} at line {line}, column {column}.")
                
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
            if next_type != "LAYER":
                raise Exception(f"Type Error: Cannot connect types LAYER and {next_type} at line {line}, column {column}.")
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
            
            if next_type != "SHAPE":
                return {
                        "type": "error",
                        "message": f"Type Error: Cannot connect types SHAPE and {next_type} at line {line}, column {column}."
                    }

            c = self.get_connection(op)

            result.add_shape(s=next_value, c=c)

        return result

    def visitLogicExpr(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        value, type = self.visit(ctx.andExpr(0))
        for i in range(1, len(ctx.andExpr())):
            if self.assigning:
                raise Exception(f"Error: Cannot apply logical operator in a non-evaluating context at line {line}, column {column}.")
            next_value, next_type = self.visit(ctx.andExpr(i))
            if next_type != "BOOLEAN":
                raise Exception(f"Type Error: Logical operations can only be applied to BOOLEAN, not {next_type} at line {line}, column {column}.")
            value = value or next_value

        return value, type

    def visitAndExpr(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        value, type = self.visit(ctx.compExpr(0))
        for i in range(1, len(ctx.compExpr())):
            if self.assigning:
                raise Exception(f"Error: Cannot apply logical operator in a non-evaluating context at line {line}, column {column}.")
            next_value, next_type = self.visit(ctx.compExpr(i))
            if next_type != "BOOLEAN":
                raise Exception(f"Type Error: Logical operations can only be applied to BOOLEAN, not {next_type} at line {line}, column {column}.")
            value = value and next_value

        return value, type

    def visitCompExpr(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        value, type = self.visit(ctx.numExpr(0))

        if ctx.COMPARATOR():
            if self.assigning:
                raise Exception(f"Error: Cannot apply comparator in a non-evaluating context at line {line}, column {column}.")
            comparator = ctx.COMPARATOR().getText()
            next_value, next_type = self.visit(ctx.numExpr(1))
            if type != next_type or type not in ["NUMBER", "BOOLEAN"]:
                raise Exception(f"Type Error: Comparisons can only be applied to NUMBER or BOOLEAN, not {next_type} at line {line}, column {column}.")

            match comparator:
                case "<":
                    if type == "NUMBER":
                        value = value < next_value
                    else:
                        raise Exception(f"Type Error: Cannot apply '<' operator to types {type} and {next_type} at line {line}, column {column}.")
                case "<=":
                    if type == "NUMBER":
                        value = value <= next_value
                    else:
                        raise Exception(f"Type Error: Cannot apply '<=' operator to types {type} and {next_type} at line {line}, column {column}.")
                case ">":
                    if type == "NUMBER":
                        value = value > next_value
                    else:
                        raise Exception(f"Type Error: Cannot apply '>' operator to types {type} and {next_type} at line {line}, column {column}.")
                case ">=":
                    if type == "NUMBER":
                        value = value >= next_value
                    else:
                        raise Exception(f"Type Error: Cannot apply '>=' operator to types {type} and {next_type} at line {line}, column {column}.")
                case "==":
                    value = value == next_value
                case "!=":
                    value = value != next_value
                case _:
                    raise Exception(f"Unknown comparator: {comparator} at line {line}, column {column}.")

            return value, "BOOLEAN"

        return value, type

    def visitNumExpr(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        value, type = self.visit(ctx.mulExpr(0))

        for i in range(1, len(ctx.mulExpr())):
            if self.assigning:
                raise Exception(f"Error: Cannot apply mathematical operator in a non-evaluating context at line {line}, column {column}.")
            next_value, next_type = self.visit(ctx.mulExpr(i))
            if next_type != "NUMBER":
                raise Exception(f"Type Error: Arithmetic operations can only be applied to NUMBER, not {next_type} at line {line}, column {column}.")
            
            if ctx.PLUS():
                value += next_value
            elif ctx.MINUS():
                value -= next_value
                
        return value, type

    def visitMulExpr(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        value, type = self.visit(ctx.signExpr(0))

        for i in range(1, len(ctx.signExpr())):
            if self.assigning:
                raise Exception(f"Error: Cannot apply mathematical operator in a non-evaluating context at line {line}, column {column}.")

            next_value, next_type = self.visit(ctx.signExpr(i))
            if ctx.MUL():
                if type == "NUMBER" and next_type == "NUMBER":
                    value *= next_value
                elif (type == "NUMBER" and next_type == "UNIT") or (type == "UNIT" and next_type == "NUMBER"):
                    unit = value if type == "UNIT" else next_value
                    number = value if type == "NUMBER" else next_value
                    if number <= 0:
                        raise Exception(f"Value Error: Cannot multiply UNIT by non-positive number at line {line}, column {column}.")
                    value = MultiUnit(unit, number)
                    type = "MULTI_UNIT"
                else:
                    raise Exception(f"Type Error: Cannot apply '*' operator to types {type} and {next_type} at line {line}, column {column}.")

            elif ctx.DIV():
                if type == "NUMBER" and next_type == "NUMBER":
                    if next_value == 0:
                        raise Exception(f"Value Error: Division by zero error at line {line}, column {column}.")
                    value //= next_value
                else:
                    raise Exception(f"Type Error: Cannot apply '/' operator to types {type} and {next_type} at line {line}, column {column}.")
        return value, type

    def visitSignExpr(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        value, type = self.visit(ctx.negExpr())

        if ctx.MINUS():
            if self.assigning:
                raise Exception(f"Error: Cannot apply mathematical operator in a non-evaluating context at line {line}, column {column}.")
            count_minus = sum(1 for token in ctx.getChildren() if token.getText() == '-')
            if type != "NUMBER":
                raise Exception(f"Type Error: Cannot apply '{ctx.MINUS().getText()}' operator to type {type} at line {line}, column {column}.")
            if count_minus % 2 == 1:
                value = -value
        return value, type

    def visitNegExpr(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        value, type = self.visit(ctx.baseExpr())

        if ctx.NOT():
            if self.assigning:
                raise Exception(f"Error: Cannot apply negation operator in a non-evaluating context at line {line}, column {column}.")
            count_not = sum(1 for token in ctx.getChildren() if token.getText() == 'NOT')
            if type != "BOOLEAN":
                raise Exception(f"Type Error: Cannot apply '{ctx.NOT().getText()}' operator to type {type} at line {line}, column {column}.")
            if count_not % 2 == 1:
                value = not value
        return value, type
    
    def visitBaseExpr(self, ctx):
        scope = self.get_scope_for_ctx(ctx)
        line = ctx.start.line
        column = ctx.start.column
        
        if ctx.ID():
            name = ctx.ID().getText()
            up_scopes = sum(1 for token in ctx.getChildren() if token.getText() == '^')
            value, type = None, None

            for _ in range(up_scopes):
                if scope.parent:
                    scope = scope.parent

            for i, ar in enumerate(reversed(self.call_stack.records)):
                if name in ar.members:
                    value, type = self.call_stack.peek(i+up_scopes).get(name), scope.get_type(name)
                    break

            if not self.assigning and value is None:
                raise Exception(f"Type Error: {name} has no value at line {line}, column {column}.")
            elif self.assigning:
                value = name

        elif ctx.unitExpr():
            value, type = self.visit(ctx.unitExpr()), "UNIT"
        elif ctx.NUMBER():
            value, type = int(ctx.NUMBER().getText()), "NUMBER"
        elif ctx.BOOLEAN():
            value, type = ctx.BOOLEAN().getText() == "TRUE", "BOOLEAN"
        elif ctx.funcCall():
            value, type = self.visit(ctx.funcCall())
        elif ctx.expression():
            value, type = self.visit(ctx.expression())
            if ctx.getChild(0).getText() == '[':
                if self.assigning:
                    raise Exception(f"Error: Cannot cast in a non-evaluating context at line {line}, column {column}.")
                if type not in ["UNIT", "MULTI_UNIT", "LAYER", "SHAPE"]:
                    raise Exception(f"Type Error: Cannot cast type {type} to another type at line {line}, column {column}.")
                match type:
                    case "UNIT":
                        value = MultiUnit(u=value)
                        type = "MULTI_UNIT"
                    case "MULTI_UNIT":
                        value = Layer(units=value.extract_units())
                        type = "LAYER"
                    case "LAYER":
                        value = Shape(layers=[value])
                        type = "SHAPE"
                    case "SHAPE":
                        value = Model(shapes=[value])
                        type = "MODEL"
        return value, type
    
    def visitUnitExpr(self, ctx):
        color, pattern = None, None
        if ctx.COLOR():
            color = ctx.COLOR().getText()[1:-1]
        if ctx.PATTERN():
            pattern = ctx.PATTERN().getText()[1:-1]
        return Unit(color=color, pattern=pattern)

    def visitBendStmt(self, ctx):
        shape = ctx.ID().getText()

    def visitShowStmt(self, ctx):
        structure, type = self.visit(ctx.expression())
        line = ctx.start.line
        column = ctx.start.column

        if type in ["UNIT", "MULTI_UNIT", "LAYER", "SHAPE", "MODEL"]:
            return show_figure(self.fig, structure)
        else:
            return {
                "type": "error",
                "message": f"SHOW only supports STRUCTUREs, not {type} at line {line}, column {column}."
            }
        
    def visitOutStmt(self, ctx):
        value, type = self.visit(ctx.expression())
        line = ctx.start.line
        column = ctx.start.column
        if type in ["NUMBER", "BOOLEAN"]:
            print(str(value))
            return None
        else:
            return {
                "type": "error",
                "message": f"OUTPUT only supports NUMBERs and BOOLEANs, not {type} at line {line}, column {column}."
            }

    def visitIfStmt(self, ctx):
        condition_value, condition_type = self.visit(ctx.logicExpr(0))
        line = ctx.start.line
        column = ctx.start.column
        if condition_type != "BOOLEAN": 
            raise Exception(f"Type Error: IF condition must be BOOLEAN, not {condition_type} at line {line}, column {column}.")

        if condition_value:
            return self.visit(ctx.stmtBlock(0))
        else:
            for i in range(1, len(ctx.logicExpr())):
                condition_value, condition_type = self.visit(ctx.logicExpr(i))
                elseLine = ctx.logicExpr(i).start.line
                elseColumn = ctx.logicExpr(i).start.column
                if condition_type != "BOOLEAN":
                    raise Exception(f"Type Error: ELSE IF condition must be BOOLEAN, not {condition_type} at line {elseLine}, column {elseColumn}.")
                if condition_value:
                    return self.visit(ctx.stmtBlock(i))

            if len(ctx.stmtBlock()) > len(ctx.logicExpr()):
                return self.visit(ctx.stmtBlock(len(ctx.stmtBlock()) - 1))
            
    def visitWhileStmt(self, ctx):
        condition_value, condition_type = self.visit(ctx.logicExpr())
        line = ctx.start.line
        column = ctx.start.column
        if condition_type != "BOOLEAN": 
            raise Exception(f"Type Error: WHILE condition must be BOOLEAN, not {condition_type} at line {line}, column {column}.")
        while condition_value:
            self.visit(ctx.stmtBlock())
            condition_value, condition_type = self.visit(ctx.logicExpr())
            line = ctx.start.line
            column = ctx.start.column
            if condition_type != "BOOLEAN": 
                raise Exception(f"Type Error: WHILE condition must be BOOLEAN, not {condition_type} at line {line}, column {column}.")
            
    def visitForStmt(self, ctx):
        number, type = self.visit(ctx.numExpr())
        line = ctx.start.line
        column = ctx.start.column

        if type != "NUMBER":
            raise Exception(f"Type Error: FOR loop must iterate over a NUMBER, not {type} at line {line}, column {column}.")

        if number < 0:
            raise Exception(f"Value Error: FOR loop cannot iterate a negative number of times at line {line}, column {column}.")

        for i in range(number):
            self.visit(ctx.stmtBlock())
            line = ctx.start.line
            column = ctx.start.column
    
    def visitStmtBlock(self, ctx):
        self.call_stack.push(ActivationRecord("block", "block", 2))
        output = None
        for statement in ctx.statement():
            statement_output = self.visit(statement)
            if isinstance(statement_output, str):
                if statement_output[0] == "{":
                    output = statement_output
        self.call_stack.pop()
        return output
    
    def visitFuncDec(self, ctx):
        func_name = ctx.ID().getText()
        return_type = ctx.dataType().getText()
        params = []

        if ctx.paramList():
            for i in range(0, len(ctx.paramList().ID())):
                param_name = ctx.paramList().ID(i).getText()
                param_type = ctx.paramList().dataType(i).getText()
                params.append((param_type, param_name))

        self.call_stack.peek().set(func_name, {
            "params": params,
            "return_type": return_type,
            "body": ctx.stmtBlock()
        })
        return None
    
    def visitFuncCall(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        func_name = ctx.ID().getText()
        func_def = None
        for i, ar in enumerate(reversed(self.call_stack.records)):
            if func_name in ar.members:
                func_def = self.call_stack.peek(i).get(func_name)

        if func_def is None:
            raise Exception(f"Unknown function: {func_name}")

        scope = self.current_scope.get_child(func_name).get_child("block")

        params = func_def["params"]
        return_type = func_def["return_type"]
        body = func_def["body"]
        args = ctx.argList().expression()

        if len(args) != len(params):
            raise Exception(f"Function {func_name} expects {len(params)} arguments, {len(args)} were given at line {line}, column {column}")

        ar = ActivationRecord(func_name, "FUNCTION", self.call_stack.peek().nesting_level + 1)

        for i, (param_type, param_name) in enumerate(params):
            value, val_type = self.visit(args[i])
            # TODO: Check for redeclaration
            scope.declare(param_name, param_type, body.start.line)  
            # TODO: Check if types match
            ar.set(param_name, value)

        self.call_stack.push(ar)

        try:
            self.current_scope = scope
            self.visit(body)
            self.current_scope = scope.parent.parent
        except Exception as e:
            if isinstance(e.args, tuple) and e.args[0] == "return":
                value, _type = e.args[1]
                self.call_stack.pop()
                return value, _type
            else:
                raise e

        self.call_stack.pop()
        return None, None


    def visitReturnStmt(self, ctx):
        value, type = self.visit(ctx.expression())
        raise Exception("return", (value, type))