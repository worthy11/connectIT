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
                
            if dec.getChild(0).getText() == "GLOBAL":
                target_scope = self.global_scope
            elif dec.getChild(0).getText() == "UP":
                up_scopes = sum(1 for token in dec.getChildren() if token.getText() == "UP")
                target_scope = self.current_scope
                for _ in range(up_scopes):
                    if target_scope.parent:
                        target_scope = target_scope.parent
            else:
                target_scope = self.current_scope

            if name in target_scope.variables:
                declared_in = target_scope.get_line(name)
                raise Exception(f"Redeclaration of '{name}' at line {line} (first declared in line {declared_in})")

            target_scope.declare(name=name, type=type, line=line)

    def enterStmtBlock(self, ctx):
        scope = Scope(f"block", parent=self.current_scope)
        self.current_scope.children.append(scope)
        self.scopes[ctx] = scope
        self.current_scope = scope

    def exitStmtBlock(self, ctx):
        self.current_scope = self.current_scope.parent

    def enterForStmt(self, ctx):
        scope = Scope("for", parent=self.current_scope)
        line = ctx.start.line

        counter = ctx.ID().getText()
        type = "NUMBER"
        scope.declare(counter, type, line)

        self.current_scope.children.append(scope)
        self.scopes[ctx] = scope
        self.current_scope = scope

    def exitForStmt(self, ctx):
        self.current_scope = self.current_scope.parent

    def enterFuncDec(self, ctx):
        name = ctx.ID().getText()
        scope = Scope(name, parent=self.current_scope)
        line = ctx.start.line
        return_type = ctx.dataType().getText()
        scope.return_type = return_type

        if name in self.current_scope.variables:
            declared_in = self.current_scope.get_line(name)
            raise Exception(f"Redeclaration of function '{name}' at line {line} (first declared in line {declared_in})")

        if ctx.paramList() is not None:
            for (type, id) in zip(ctx.paramList().dataType(), ctx.paramList().ID()):
                type = type.getText()
                id = id.getText()
                if id in scope.variables:
                    declared_in = scope.get_line(id)
                    raise Exception(f"Redeclaration of parameter '{id}' at line {line} (first declared in line {declared_in})")
                scope.declare(id, type, line)

        self.current_scope.declare(name, "FUNCTION", line)
        self.current_scope.children.append(scope)
        self.scopes[ctx] = scope
        self.current_scope = scope

    def exitFuncDec(self, ctx):
        self.current_scope = self.current_scope.parent
