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


    # Visit a parse tree produced by ConnectITParser#dataType.
    def visitDataType(self, ctx:ConnectITParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#arrowOperator.
    def visitArrowOperator(self, ctx:ConnectITParser.ArrowOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#expression.
    def visitExpression(self, ctx:ConnectITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#logicExpr.
    def visitLogicExpr(self, ctx:ConnectITParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#andExpr.
    def visitAndExpr(self, ctx:ConnectITParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#compExpr.
    def visitCompExpr(self, ctx:ConnectITParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#numExpr.
    def visitNumExpr(self, ctx:ConnectITParser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#mulExpr.
    def visitMulExpr(self, ctx:ConnectITParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#invExpr.
    def visitInvExpr(self, ctx:ConnectITParser.InvExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#baseExpr.
    def visitBaseExpr(self, ctx:ConnectITParser.BaseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#unitExpr.
    def visitUnitExpr(self, ctx:ConnectITParser.UnitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConnectITParser#bendStatement.
    def visitBendStatement(self, ctx:ConnectITParser.BendStatementContext):
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



del ConnectITParser