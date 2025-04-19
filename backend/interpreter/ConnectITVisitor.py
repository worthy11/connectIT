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


    # Visit a parse tree produced by ConnectITParser#declarationList.
    def visitDeclarationList(self, ctx:ConnectITParser.DeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#declaration.
    def visitDeclaration(self, ctx:ConnectITParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#assignment.
    def visitAssignment(self, ctx:ConnectITParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#extension.
    def visitExtension(self, ctx:ConnectITParser.ExtensionContext):
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


    # Visit a parse tree produced by ConnectITParser#layerTerm.
    def visitLayerTerm(self, ctx:ConnectITParser.LayerTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeExpr.
    def visitShapeExpr(self, ctx:ConnectITParser.ShapeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeTerm.
    def visitShapeTerm(self, ctx:ConnectITParser.ShapeTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#shapeConnector.
    def visitShapeConnector(self, ctx:ConnectITParser.ShapeConnectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelExpr.
    def visitModelExpr(self, ctx:ConnectITParser.ModelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelTerm.
    def visitModelTerm(self, ctx:ConnectITParser.ModelTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#modelConnector.
    def visitModelConnector(self, ctx:ConnectITParser.ModelConnectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#idCast.
    def visitIdCast(self, ctx:ConnectITParser.IdCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#numericExpr.
    def visitNumericExpr(self, ctx:ConnectITParser.NumericExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#booleanExpr.
    def visitBooleanExpr(self, ctx:ConnectITParser.BooleanExprContext):
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


    # Visit a parse tree produced by ConnectITParser#dataType.
    def visitDataType(self, ctx:ConnectITParser.DataTypeContext):
        return self.visitChildren(ctx)



del ConnectITParser