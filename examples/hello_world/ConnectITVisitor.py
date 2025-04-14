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


    # Visit a parse tree produced by ConnectITParser#unitDeclaration.
    def visitUnitDeclaration(self, ctx:ConnectITParser.UnitDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#layerDeclaration.
    def visitLayerDeclaration(self, ctx:ConnectITParser.LayerDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeDeclaration.
    def visitShapeDeclaration(self, ctx:ConnectITParser.ShapeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelDeclaration.
    def visitModelDeclaration(self, ctx:ConnectITParser.ModelDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#unitAssigmentList.
    def visitUnitAssigmentList(self, ctx:ConnectITParser.UnitAssigmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#unitAssignment.
    def visitUnitAssignment(self, ctx:ConnectITParser.UnitAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#layerAssigmentList.
    def visitLayerAssigmentList(self, ctx:ConnectITParser.LayerAssigmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#layerAssignment.
    def visitLayerAssignment(self, ctx:ConnectITParser.LayerAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#idList.
    def visitIdList(self, ctx:ConnectITParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#standardAssignment.
    def visitStandardAssignment(self, ctx:ConnectITParser.StandardAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeAssignment.
    def visitShapeAssignment(self, ctx:ConnectITParser.ShapeAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelAssignment.
    def visitModelAssignment(self, ctx:ConnectITParser.ModelAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#expression.
    def visitExpression(self, ctx:ConnectITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#unitExpr.
    def visitUnitExpr(self, ctx:ConnectITParser.UnitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#layerExpr.
    def visitLayerExpr(self, ctx:ConnectITParser.LayerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeDef.
    def visitShapeDef(self, ctx:ConnectITParser.ShapeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#layerChain.
    def visitLayerChain(self, ctx:ConnectITParser.LayerChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelDef.
    def visitModelDef(self, ctx:ConnectITParser.ModelDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeChain.
    def visitShapeChain(self, ctx:ConnectITParser.ShapeChainContext):
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