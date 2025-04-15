# Generated from ConnectIT.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ConnectITParser import ConnectITParser
else:
    from ConnectITParser import ConnectITParser

# This class defines a complete generic visitor for a parse tree produced by ConnectITParser.

class ConnectITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConnectITParser#program.
    def visitProgram(self, ctx:ConnectITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#statement.
    def visitStatement(self, ctx:ConnectITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#newUnit.
    def visitNewUnit(self, ctx:ConnectITParser.NewUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#newLayer.
    def visitNewLayer(self, ctx:ConnectITParser.NewLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#newShape.
    def visitNewShape(self, ctx:ConnectITParser.NewShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#newModel.
    def visitNewModel(self, ctx:ConnectITParser.NewModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#newNumber.
    def visitNewNumber(self, ctx:ConnectITParser.NewNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#newBoolean.
    def visitNewBoolean(self, ctx:ConnectITParser.NewBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#unitDeclarationList.
    def visitUnitDeclarationList(self, ctx:ConnectITParser.UnitDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#unitDeclaration.
    def visitUnitDeclaration(self, ctx:ConnectITParser.UnitDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#unitExpr.
    def visitUnitExpr(self, ctx:ConnectITParser.UnitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#layerDeclarationList.
    def visitLayerDeclarationList(self, ctx:ConnectITParser.LayerDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#layerDeclaration.
    def visitLayerDeclaration(self, ctx:ConnectITParser.LayerDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#layerExpr.
    def visitLayerExpr(self, ctx:ConnectITParser.LayerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeDeclarationList.
    def visitShapeDeclarationList(self, ctx:ConnectITParser.ShapeDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeDeclaration.
    def visitShapeDeclaration(self, ctx:ConnectITParser.ShapeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeExpr.
    def visitShapeExpr(self, ctx:ConnectITParser.ShapeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelDeclarationList.
    def visitModelDeclarationList(self, ctx:ConnectITParser.ModelDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelDeclaration.
    def visitModelDeclaration(self, ctx:ConnectITParser.ModelDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelExpr.
    def visitModelExpr(self, ctx:ConnectITParser.ModelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#numberDeclarationList.
    def visitNumberDeclarationList(self, ctx:ConnectITParser.NumberDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#numberDeclaration.
    def visitNumberDeclaration(self, ctx:ConnectITParser.NumberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#booleanDeclarationList.
    def visitBooleanDeclarationList(self, ctx:ConnectITParser.BooleanDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#booleanDeclaration.
    def visitBooleanDeclaration(self, ctx:ConnectITParser.BooleanDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#assignment.
    def visitAssignment(self, ctx:ConnectITParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#expression.
    def visitExpression(self, ctx:ConnectITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#showStatement.
    def visitShowStatement(self, ctx:ConnectITParser.ShowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#ifStmt.
    def visitIfStmt(self, ctx:ConnectITParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#whileStmt.
    def visitWhileStmt(self, ctx:ConnectITParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#condition.
    def visitCondition(self, ctx:ConnectITParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#statementBlock.
    def visitStatementBlock(self, ctx:ConnectITParser.StatementBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#forStmt.
    def visitForStmt(self, ctx:ConnectITParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:ConnectITParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#returnExpr.
    def visitReturnExpr(self, ctx:ConnectITParser.ReturnExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#type.
    def visitType(self, ctx:ConnectITParser.TypeContext):
        return self.visitChildren(ctx)



del ConnectITParser