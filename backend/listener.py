from interpreter.ConnectITListener import ConnectITListener

class GlobalScope:
    def __init__(self):
        self.variables = {}

    def declare(self, name, value):
        self.variables[name] = value

    def get(self, name):
        return self.variables.get(name)

    def __contains__(self, name):
        return name in self.variables

class CustomListener(ConnectITListener):
    def __init__(self, scope):
        self.scope = scope

    def enterUnitDeclaration(self, ctx):
        for unit_assignment_ctx in ctx.unitAssigmentList().unitAssignment():
            name = unit_assignment_ctx.ID().getText()
            if name in self.scope:
                line = ctx.start.line
                raise Exception(f"Redeclaration of '{name}' at line {line}")
            self.scope[name] = 'UNIT'

    def enterLayerDeclaration(self, ctx):
        # Register layer names
        pass

    # Add more enterXYZ methods if needed
