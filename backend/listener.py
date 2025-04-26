from interpreter.ConnectITListener import ConnectITListener
types = {
    "UNIT": 0,
    "LAYER": 2,
    "SHAPE": 3,
    "MODEL": 4,
    "NUMBER": 5,
    "BOOLEAN": 6
}

class GlobalScope:
    def __init__(self):
        self.variables = {}

    def declare(self, name, type):
        self.variables[name] = {}
        self.variables[name]["type"] = type
        self.variables[name]["value"] = None

    def get_type(self, name):
        return self.variables[name]["type"]

    def get_value(self, name):
        return self.variables[name]["value"]

    def fill(self, name, value):
        self.variables[name]["value"] = value

    def __contains__(self, name):
        return name in self.variables

class CustomListener(ConnectITListener):
    def __init__(self, scope: GlobalScope):
        self.scope = scope

    def enterDeclarationList(self, ctx):
        type = types[ctx.dataType().getText()]
        for dec in ctx.declaration():
            if dec.assignment():
                name = dec.assignment().ID().getText()
            else:
                name = dec.ID().getText()
            if name in self.scope:
                line = ctx.start.line
                raise Exception(f"Redeclaration of '{name}' at line {line}")
            
            self.scope.declare(name=name, type=type)
