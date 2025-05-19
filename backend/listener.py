from interpreter.ConnectITListener import ConnectITListener
from utils import *

class CustomListener(ConnectITListener):
    def __init__(self):
        self.global_scope = Scope("global")
        self.current_scope = self.global_scope
        self.scopes = {}

    def enterProgram(self, ctx):
        self.scopes[ctx] = self.current_scope

    def enterDeclarationList(self, ctx):
        type = ctx.dataType().getText()
        line = ctx.start.line
        for dec in ctx.declaration():
            if dec.assignment():
                name = dec.assignment().getChild(0).getText()
            else:
                name = dec.ID().getText()
            if name in self.current_scope.variables:
                declared_in = self.current_scope.get_line(name)
                raise Exception(f"Redeclaration of '{name}' at line {line} (first declared in line {declared_in})")
            
            self.current_scope.declare(name=name, type=type, line=line)

    def enterFuncDec(self, ctx):
        name = ctx.ID().getText()
        line = ctx.start.line
        if name in self.current_scope.variables:
            declared_in = self.current_scope.get_line(name)
            raise Exception(f"Redeclaration of '{name}' at line {line} (first declared in line {declared_in})")
        scope = Scope(name, parent=self.current_scope)
        self.current_scope.declare(name, "FUNCTION", line)
        self.current_scope.children.append(scope)

        self.scopes[ctx] = scope
        self.current_scope = scope

    def exitFuncDec(self, ctx):
        self.current_scope = self.current_scope.parent

    def enterStmtBlock(self, ctx):
        scope = Scope("block", parent=self.current_scope)
        self.current_scope.children.append(scope)
        self.scopes[ctx] = scope
        self.current_scope = scope

    def exitStmtBlock(self, ctx):
        self.current_scope = self.current_scope.parent