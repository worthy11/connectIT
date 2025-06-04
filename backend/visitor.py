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
        self.assigning = False
        self.declaring = False
        self.render = []
        self.text = []
        self.show = False
        self.diagnostic_logs = []

    def add_diagnostic_log(self, message):
        self.diagnostic_logs.append(message)

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
        return None
    
    def get_ar_for_scope(self, scope):
        while scope is not None:
            for ar in reversed(self.call_stack.records):
                if ar.scope == scope:
                    return ar
            scope = scope.parent
        raise Exception("Error: No activation record matching scope")

    def format_variable_info(self):
        output = []
        
        scope_variables = {}
        
        for ar in self.call_stack.records:
            for var_path, value in ar.members.items():
                if ":" in var_path:
                    var_name, *scope_parts = var_path.split(":")
                    scope_str = ":".join(scope_parts)
                    
                    if scope_str not in scope_variables:
                        scope_variables[scope_str] = []
                    
                    scope_variables[scope_str].append((var_name, value))
        
        for scope_str, variables in scope_variables.items():
            if scope_str:
                output.append(f"  Scope: {scope_str}")
                for var_name, value in variables:
                    output.append(f"{var_name} = {value}")
        
        return "\n".join(output)

    def visitProgram(self, ctx):
        self.current_scope = self.get_scope_for_ctx(ctx)
        self.call_stack.push(ActivationRecord("global", "program", 1, self.current_scope))
        self.add_diagnostic_log(f"Starting program execution in global scope")
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return self.text, self.render, self.diagnostic_logs
    
    def visitStatement(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        if ctx.getChildCount() > 1 and ctx.getChild(0).getText() == "?":
            return None
        if ctx.declarationList():
            declarations = []
            for dec in ctx.declarationList().declaration():
                if dec.assignment():
                    name = dec.assignment().identifier().ID().getText()
                    expr = dec.assignment().expression().getText()
                    declarations.append(f"{name} = {expr}")
                else:
                    name = dec.ID().getText()
                    declarations.append(name)
            self.add_diagnostic_log(f"Line {line}: Processing declaration {', '.join(declarations)}")
            self.visit(ctx.declarationList())
            self.add_diagnostic_log(self.format_variable_info())
            return None
        if ctx.assignment():
            name = ctx.assignment().identifier().ID().getText()
            expr = ctx.assignment().expression().getText()
            self.add_diagnostic_log(f"Line {line}: Processing assignment {name} = {expr}")
            self.visit(ctx.assignment())
            self.add_diagnostic_log(self.format_variable_info())
            return None
        if ctx.expression():
            self.add_diagnostic_log(f"Line {line}: Processing expression")
            return self.visit(ctx.expression())
        if ctx.extension():
            return self.visit(ctx.extension())
        if ctx.showStmt():
            return self.visit(ctx.showStmt())
        if ctx.outStmt():
            return self.visit(ctx.outStmt())
        if ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        if ctx.elifStmt():
            raise Exception(f"Syntax Error: ELSE IF statement without previous IF at line {line}, column {column}. Please ensure it follows an IF statement.")
        if ctx.elseStmt():
            raise Exception(f"Syntax Error: ELSE statement without previous IF at line {line}, column {column}. Please ensure it follows an IF statement.")
        if ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        if ctx.forStmt():
            return self.visit(ctx.forStmt())
        if ctx.funcDec():
            return self.visit(ctx.funcDec())
        if ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        if ctx.stmtBlock():
            return self.visit(ctx.stmtBlock())
        else:
            line = ctx.start.line
            column = ctx.start.column
            return {
                "type": "error",
                "message": f"Invalid statement at line {line}, column {column}."
            }
        
    def visitDeclarationList(self, ctx):
        type = ctx.dataType().getText()
        line = ctx.start.line
        column = ctx.start.column
        for dec in ctx.declaration():
            is_global = dec.getChild(0).getText() == "GLOBAL"
            up_scopes = sum(1 for token in dec.getChildren() if token.getText() == "UP")
            scope = self.current_scope

            path = []
            while scope is not None:
                path.append(scope.name)
                scope = scope.parent
            path = ":".join(path)

            ar = self.get_ar_for_scope(self.current_scope)

            if dec.assignment():
                name = dec.assignment().identifier().ID().getText()
                name += ":" + path
                ar.set(name, None)
                self.visit(dec.assignment())
            else:
                name = dec.ID().getText()
                name += ":" + path
                ar.set(name, None)
                type = ctx.dataType().getText()
                match type:
                    case "UNIT":
                        default = Unit()
                    case "LAYER":
                        default = Layer([Unit()], False)
                    case "SHAPE":
                        default = Shape([Layer([Unit()])], [])
                    case "MODEL":
                        default = Model([Shape([Layer([Unit()])], [])], [])
                    case "NUMBER":
                        default = 0
                    case "BOOLEAN":
                        default = "FALSE"
                ar.set(name, default)
        return None

    def visitAssignment(self, ctx):
        line = ctx.start.line
        column = ctx.start.column

        name = ctx.identifier().ID().getText()
        scope = self.current_scope
        if ctx.identifier().getChild(0).getText() == "GLOBAL":
            while scope.parent:
                scope = scope.parent
        elif ctx.identifier().getChild(0).getText() == "UP":
            up_scopes = sum(1 for token in ctx.identifier().getChildren() if token.getText() == "UP")
            for _ in range(up_scopes):
                if scope.parent:
                    if scope.parent.name not in ["block", "global"]:
                        scope = scope.parent.parent
                    else:
                        scope = scope.parent

        while name not in scope.variables and scope.parent:
            scope = scope.parent

        expected_type = scope.get_type(name)
        ar = self.get_ar_for_scope(scope)

        path = []
        while scope is not None:
            path.append(scope.name)
            scope = scope.parent
        path = ":".join(path)

        value, received_type = self.visit(ctx.expression())
        if received_type != expected_type:
            if type_map[received_type].get(expected_type) is not None:
                value = type_map[received_type][expected_type](value)
            else:
                if received_type is None:
                    raise Exception(f"Error: Cannot assign undeclared variable value to {name} at line {line}, column {column}. Please ensure the variable is declared before assignment.")
                if expected_type is None:
                    raise Exception(f"Error: Cannot assign to undeclared variable {name} at line {line}, column {column}. Please ensure the variable is declared before assignment.")
                raise Exception(f"Type Error: Cannot assign {received_type} to {expected_type} at line {line}, column {column}. Did you mean to type {name} {expected_type}?")

        if name+":"+path in ar.members:
            ar.set(name+":"+path, value)
            return None

    def visitIdentifier(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        name = ctx.ID().getText()

        self.add_diagnostic_log(f"Line {line}: Accessing identifier '{name}'")
        scope = self.current_scope
        if ctx.getChild(0).getText() == "GLOBAL":
            while scope.parent:
                scope = scope.parent
        elif ctx.getChild(0).getText() == "UP":
            up_scopes = sum(1 for token in ctx.getChildren() if token.getText() == "UP")
            for _ in range(up_scopes):
                if scope.parent:
                    if scope.parent.name not in ["block", "global"]:
                        scope = scope.parent.parent
                    else:
                        scope = scope.parent

        while name not in scope.variables and scope.parent:
            scope = scope.parent

        type = scope.get_type(name)
        if type is None:
            raise Exception(f"Error: Use of undeclared variable {name} at line {line}, column {column}. Please ensure the variable is declared before use.")

        ar = self.get_ar_for_scope(scope)

        path = []
        while scope is not None:
            path.append(scope.name)
            scope = scope.parent
        path = ":".join(path)
        value = ar.get(name+":"+path)
        return value, type
    
    def visitExtension(self, ctx):
        line = ctx.start.line
        column = ctx.start.column

        name = ctx.identifier().ID().getText()
        self.add_diagnostic_log(f"Line {line}: Accessing identifier '{name}'")
        scope = self.current_scope
        if ctx.getChild(0).getText() == "GLOBAL":
            while scope.parent:
                scope = scope.parent
        elif ctx.getChild(0).getText() == "UP":
            up_scopes = sum(1 for token in ctx.getChildren() if token.getText() == "UP")
            for _ in range(up_scopes):
                if scope.parent:
                    if scope.parent.name not in ["block", "global"]:
                        scope = scope.parent.parent
                    else:
                        scope = scope.parent

        while name not in scope.variables and scope.parent:
            scope = scope.parent
        expected_type = scope.get_type(name)
        ar = self.get_ar_for_scope(scope)

        e, op = ctx.expression(), ctx.extensionOperator()
        if expected_type not in ["LAYER", "SHAPE", "MODEL", "NUMBER"]:            
            raise Exception(f"Type Error: Cannot add new values to type {expected_type} at line {line}, column {column}. Only LAYER, SHAPE, MODEL, and NUMBER can be extended.")

        path = []
        while scope is not None:
            path.append(scope.name)
            scope = scope.parent
        path = ":".join(path)

        value = ar.get(name+":"+path)

        if name+":"+path in ar.members:
            match expected_type:
                case "LAYER":
                    new_value = self.extendLayer(value, e, op)
                case "SHAPE":
                    new_value = self.extendShape(value, e, op)
                case "MODEL":
                    new_value = self.extendModel(value, e, op)
                case "NUMBER":
                    new_value = self.extendNumber(value, e, op)
            ar.set(name+":"+path, new_value)
            return
        raise Exception(f"Error: Cannot apply {op.getText()} operator to undeclared variable {name} at line {line}, column {column}")

    def extendLayer(self, value, e, op):
        received_value, received_type = self.visit(e)
        line = op.start.line
        column = op.start.column

        if op.getText() not in ['<+->']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Layer at line {line}, column {column}. Only '<+->' is allowed for extending a Layer.")
            
        if received_type not in ["UNIT", "MULTI_UNIT"]:
            raise Exception(f"Cannot add value of type '{received_type}' to a Layer at line {line}, column {column}. Only UNIT or MULTI_UNIT can be added to a Layer.")
        
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
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a Shape at line {line}, column {column}. Only '<+-' is allowed for extending a Shape.")
            
        if received_type != "LAYER":
            if type_map[received_type].get("LAYER") is not None:
                value = type_map[received_type]["LAYER"](value)
            else:
                raise Exception(f"Type Error: Cannot add value of type '{received_type}' to a SHAPE at line {line}, column {column}. Only LAYER can be added to a SHAPE.")
        
        c = self.get_connection(op)
        shape_closed = any(layer.is_closed() for layer in value.layers)

        if shape_closed:
            if not received_value.is_closed():
                raise Exception(f"Type Error: Cannot add an open layer to a closed shape at line {line}, column {column}. Close the layer first using CLOSED keyword.")

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
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a MODEL at line {line}, column {column}.")
            
        if received_type != "SHAPE":
            if type_map[received_type].get("SHAPE") is not None:
                value = type_map[received_type]["SHAPE"](value)
            else:
                raise Exception(f"Type Error: Cannot add value of type '{received_type}' to a MODEL at line {line}, column {column}.")
        
                
        c = self.get_connection(op)
        value.add_shape(received_value, c)
        return value
    
    def extendNumber(self, value, e, op):
        line = op.start.line
        column = op.start.column
        if op.getText() not in ['+=', '-=', '*=', '/=']:
            raise Exception(f"Operator '{op.getText()}' cannot be used to extend a NUMBER at line {line}, column {column}. Use arithmetic operators instead.")
            
        received_value, received_type = self.visit(e)
        if received_type != "NUMBER": 
            if op.getText() == '+=':
                raise Exception(f"Cannot add value of type '{received_type}' to a NUMBER at line {line}, column {column}. Only NUMBER can be added to a NUMBER.")
            elif op.getText() == '-=':
                raise Exception(f"Cannot subtract value of type '{received_type}' from a NUMBER at line {line}, column {column}. Only NUMBER can be subtracted from a NUMBER.")
            elif op.getText() == '*=':
                raise Exception(f"Cannot multiply value of type '{received_type}' to a NUMBER at line {line}, column {column}. Only NUMBER can be multiplied to a NUMBER.")
            elif op.getText() == '/=':
                raise Exception(f"Cannot divide value of type '{received_type}' from a NUMBER at line {line}, column {column}. Only NUMBER can be divided from a NUMBER.")
            
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
            if shift_type != "NUMBER": 
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
                    if type == 'UNIT':
                        raise Exception(f"Cannot use connectors with type '{type}' at line {line}, column {column}. Cast UNIT using [variable] syntax.")
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
                if type_map[next_type].get("MULTI_UNIT") is not None:
                    next_value = type_map[next_type]["MULTI_UNIT"](next_value)
                else:
                    raise Exception(f"Type Error: Can only apply '<->' connector to multiples of UNITs, not {next_type} at line {line}, column {column}. Change the type of variable to MULTI_UNIT or use a different connector.")
                
            if op.getText() != "<->":
                raise Exception(f"Type Error: Cannot use '{op.getText()}' connector when creating a LAYER at line {line}, column {column}. Change connector to <->.")
                
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
                if type_map[next_type].get("LAYER") is not None:
                    next_value = type_map[next_type]["LAYER"](next_value)
                else:
                    raise Exception(f"Type Error: Cannot connect types LAYER and {next_type} at line {line}, column {column}.")

            c = self.get_connection(op)
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
                if type_map[next_type].get("SHAPE") is not None:
                    next_value = type_map[next_type]["SHAPE"](next_value)
                else:
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
        line = ctx.start.line
        column = ctx.start.column
        
        if ctx.identifier():
            value, type = self.visit(ctx.identifier())
        elif ctx.unitExpr(): 
            value, type = self.visit(ctx.unitExpr()), "UNIT"
        elif ctx.NUMBER():
            value, type = int(ctx.NUMBER().getText()), "NUMBER"
        elif ctx.BOOLEAN():
            value, type = ctx.BOOLEAN().getText() == "TRUE", "BOOLEAN"
        elif ctx.funcCall():
            value, type = self.visit(ctx.funcCall())
            if type == "NOTHING":
                value = None 

        elif ctx.expression():
            value, type = self.visit(ctx.expression())
            if ctx.dataType():
                if cast_map[type].get(ctx.dataType().getText()) is not None:
                    value = cast_map[type][ctx.dataType().getText()](value)
                    type = ctx.dataType().getText()
                else:
                    raise Exception(f"Type Error: Cannot cast type {type} to {ctx.dataType().getText()} at line {line}, column {column}.")
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
            self.render = show_figure(go.Figure(), structure)
            self.show = True
        else:
            raise Exception(f"Type Error: SHOW statement only supports UNIT, MULTI_UNIT, LAYER, SHAPE, and MODEL, not {type} at line {line}, column {column}.")
        
    def visitOutStmt(self, ctx):
        value, type = self.visit(ctx.expression())
        line = ctx.start.line
        column = ctx.start.column
        if type in ["NUMBER", "BOOLEAN"]:
            print(str(value))
            self.text.append(str(value))
            return None
        else:
            return {
                "type": "error",
                "message": f"OUTPUT only supports NUMBERs and BOOLEANs, not {type} at line {line}, column {column}."
            }

    def visitIfStmt(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        condition_value, condition_type = self.visit(ctx.logicExpr())
        if condition_type != "BOOLEAN": 
            raise Exception(f"Type Error: IF condition must be BOOLEAN, not {condition_type} at line {line}, column {column}.")

        if condition_value:
            self.visit(ctx.stmtBlock())
        else:
            if ctx.elifStmt():
                for elseif in ctx.elifStmt():
                    if self.visit(elseif):
                        return
            if ctx.elseStmt():
                self.visit(ctx.elseStmt())
            else:
                return
        
    def visitElifStmt(self, ctx):
        line = ctx.start.line
        column = ctx.start.column
        condition_value, condition_type = self.visit(ctx.logicExpr())
        if condition_type != "BOOLEAN": 
            raise Exception(f"Type Error: ELSE IF condition must be BOOLEAN, not {condition_type} at line {line}, column {column}.")

        if condition_value:
            self.visit(ctx.stmtBlock())
            return True
        else:
            return False

    def visitElseStmt(self, ctx):
        self.visit(ctx.stmtBlock())
        return
            
    def visitWhileStmt(self, ctx):
        condition_value, condition_type = self.visit(ctx.logicExpr())
        line = ctx.start.line
        column = ctx.start.column

        if condition_type != "BOOLEAN": 
            raise Exception(f"Type Error: WHILE condition must be BOOLEAN, not {condition_type} at line {line}, column {column}.")

        counter = 0
        while condition_value:
            self.visit(ctx.stmtBlock())
            condition_value, condition_type = self.visit(ctx.logicExpr())
            line = ctx.start.line
            column = ctx.start.column
            if condition_type != "BOOLEAN": 
                raise Exception(f"Type Error: WHILE condition must be BOOLEAN, not {condition_type} at line {line}, column {column}.")
            counter += 1
            if counter > 500:
                raise Exception(f"Error: Infinite loop detected at line {line}, column {column}.")
            
    def visitForStmt(self, ctx):
        self.current_scope = self.scopes[ctx]
        count, count_type = self.visit(ctx.numExpr(0))
        line = ctx.start.line
        column = ctx.start.column

        if count_type != "NUMBER":
            raise Exception(f"Type Error: FOR loop must iterate over a NUMBER, not {count_type} at line {line}, column {column}.")

        counter_name = ctx.ID().getText()
        start = 0
        step = 1
        path = []
        scope = self.scopes[ctx]
        while scope is not None:
            path.append(scope.name)
            scope = scope.parent
        path = counter_name + ":" + ":".join(path)

        if ctx.getChildCount() > 4:
            for i in range(4, ctx.getChildCount()):
                if ctx.getChild(i).getText() == "START":
                    start_val, start_type = self.visit(ctx.numExpr(1))
                    if start_type != "NUMBER":
                        raise Exception(f"Type Error: START value must be NUMBER at line {line}, column {column}.")
                    start = start_val
                if ctx.getChild(i).getText() == "STEP":
                    idx = 2 if ctx.getText().count("START") and ctx.getText().count("STEP") else 1
                    step_val, step_type = self.visit(ctx.numExpr(idx))
                    if step_type != "NUMBER":
                        raise Exception(f"Type Error: STEP value must be NUMBER at line {line}, column {column}.")
                    step = step_val

        self.call_stack.peek().set(path, start)

        try:
            for i in range(count):
                self.call_stack.peek().set(path, start + i * step)
                self.visit(ctx.stmtBlock())
        finally:
            self.current_scope = self.current_scope.parent
    
    def visitStmtBlock(self, ctx):
        self.current_scope = self.scopes[ctx]
        try:
            for statement in ctx.statement():
                self.visit(statement)
        finally:
            self.current_scope = self.current_scope.parent
    
    def visitFuncDec(self, ctx):
        func_name = ctx.ID().getText()
        return_type = ctx.dataType().getText()
        self.add_diagnostic_log(f"Line {ctx.start.line}: Declaring function '{func_name}' with return type '{return_type}'")
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
        
        self.add_diagnostic_log(f"Line {line}: Calling function '{func_name}'")
        func_def = None

        for i, ar in enumerate(reversed(self.call_stack.records)):
            if func_name in ar.members:
                func_def = self.call_stack.peek(i).get(func_name)

        if func_def is None:
            raise Exception(f"Unknown function: {func_name} at line {line}, column {column}")

        scope = self.current_scope.get_child(func_name)
        curr_scope = scope
        path = []
        while scope is not None:
            path.append(scope.name)
            scope = scope.parent
        scope = curr_scope

        params = func_def["params"]
        return_type = func_def["return_type"]
        body = func_def["body"]
        args = ctx.argList().expression() if ctx.argList() else []
    
        if len(args) != len(params):
            raise Exception(f"Function {func_name} expects {len(params)} arguments, {len(args)} were given at line {line}, column {column}")

        if self.call_stack.peek().nesting_level + 1 > 20:
            raise Exception(f"Error: Maximum function call depth reached at line {line}, column {column}")
        
        ar = ActivationRecord(func_name, "FUNCTION", self.call_stack.peek().nesting_level + 1, scope)
        found = False
        while len(path) > 0 and not found:
            for i, (param_type, param_name) in enumerate(params):
                value, val_type = self.visit(args[i])
                if val_type != param_type:
                    raise Exception(f"Type Error: Function {func_name} expects {param_type}, got {val_type} at line {line}, column {column}")

                var_path = param_name + ":" + ":".join(path)
                ar.set(var_path, value)
                found = True
            path.pop(0)
        self.call_stack.push(ar)
        print(f"Call stack: {[r.members for r in self.call_stack.records]}")

        try:
            self.current_scope = scope
            self.visit(body)
        except Exception as e:
            if isinstance(e.args, tuple) and e.args[0] == "return":
                value, _type = e.args[1]

                if return_type == 'NOTHING' and _type is not None:
                    raise Exception(f"Void functions cannot return values. Did you mean to create function that returns {_type} at line {line}, column {column}?")
                if _type != return_type:
                    raise Exception(f"Return type mismatch in function '{func_name}': expected {return_type}, got {_type} at line {line}, column {column}")             

                return value, _type
            else:
                raise e
        finally:
            self.current_scope = scope.parent
            self.call_stack.pop()
        return None, None

    def visitReturnStmt(self, ctx):  
        value, type = self.visit(ctx.expression())
        raise Exception("return", (value, type))