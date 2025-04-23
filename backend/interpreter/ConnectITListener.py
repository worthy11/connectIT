# Generated from ConnectIT.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ConnectITParser import ConnectITParser
else:
    from ConnectITParser import ConnectITParser

# This class defines a complete listener for a parse tree produced by ConnectITParser.
class ConnectITListener(ParseTreeListener):

    # Enter a parse tree produced by ConnectITParser#program.
    def enterProgram(self, ctx:ConnectITParser.ProgramContext):
        pass

    # Exit a parse tree produced by ConnectITParser#program.
    def exitProgram(self, ctx:ConnectITParser.ProgramContext):
        pass


    # Enter a parse tree produced by ConnectITParser#statement.
    def enterStatement(self, ctx:ConnectITParser.StatementContext):
        pass

    # Exit a parse tree produced by ConnectITParser#statement.
    def exitStatement(self, ctx:ConnectITParser.StatementContext):
        pass


    # Enter a parse tree produced by ConnectITParser#declarationList.
    def enterDeclarationList(self, ctx:ConnectITParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by ConnectITParser#declarationList.
    def exitDeclarationList(self, ctx:ConnectITParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by ConnectITParser#declaration.
    def enterDeclaration(self, ctx:ConnectITParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ConnectITParser#declaration.
    def exitDeclaration(self, ctx:ConnectITParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ConnectITParser#assignment.
    def enterAssignment(self, ctx:ConnectITParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ConnectITParser#assignment.
    def exitAssignment(self, ctx:ConnectITParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ConnectITParser#extension.
    def enterExtension(self, ctx:ConnectITParser.ExtensionContext):
        pass

    # Exit a parse tree produced by ConnectITParser#extension.
    def exitExtension(self, ctx:ConnectITParser.ExtensionContext):
        pass


    # Enter a parse tree produced by ConnectITParser#expression.
    def enterExpression(self, ctx:ConnectITParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ConnectITParser#expression.
    def exitExpression(self, ctx:ConnectITParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ConnectITParser#arrowOperator.
    def enterArrowOperator(self, ctx:ConnectITParser.ArrowOperatorContext):
        pass

    # Exit a parse tree produced by ConnectITParser#arrowOperator.
    def exitArrowOperator(self, ctx:ConnectITParser.ArrowOperatorContext):
        pass


    # Enter a parse tree produced by ConnectITParser#unitExpr.
    def enterUnitExpr(self, ctx:ConnectITParser.UnitExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#unitExpr.
    def exitUnitExpr(self, ctx:ConnectITParser.UnitExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#numericExpr.
    def enterNumericExpr(self, ctx:ConnectITParser.NumericExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#numericExpr.
    def exitNumericExpr(self, ctx:ConnectITParser.NumericExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#booleanExpr.
    def enterBooleanExpr(self, ctx:ConnectITParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#booleanExpr.
    def exitBooleanExpr(self, ctx:ConnectITParser.BooleanExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#castExpr.
    def enterCastExpr(self, ctx:ConnectITParser.CastExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#castExpr.
    def exitCastExpr(self, ctx:ConnectITParser.CastExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#bendStatement.
    def enterBendStatement(self, ctx:ConnectITParser.BendStatementContext):
        pass

    # Exit a parse tree produced by ConnectITParser#bendStatement.
    def exitBendStatement(self, ctx:ConnectITParser.BendStatementContext):
        pass


    # Enter a parse tree produced by ConnectITParser#showStatement.
    def enterShowStatement(self, ctx:ConnectITParser.ShowStatementContext):
        pass

    # Exit a parse tree produced by ConnectITParser#showStatement.
    def exitShowStatement(self, ctx:ConnectITParser.ShowStatementContext):
        pass


    # Enter a parse tree produced by ConnectITParser#ifStmt.
    def enterIfStmt(self, ctx:ConnectITParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ConnectITParser#ifStmt.
    def exitIfStmt(self, ctx:ConnectITParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ConnectITParser#whileStmt.
    def enterWhileStmt(self, ctx:ConnectITParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ConnectITParser#whileStmt.
    def exitWhileStmt(self, ctx:ConnectITParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ConnectITParser#condition.
    def enterCondition(self, ctx:ConnectITParser.ConditionContext):
        pass

    # Exit a parse tree produced by ConnectITParser#condition.
    def exitCondition(self, ctx:ConnectITParser.ConditionContext):
        pass


    # Enter a parse tree produced by ConnectITParser#statementBlock.
    def enterStatementBlock(self, ctx:ConnectITParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by ConnectITParser#statementBlock.
    def exitStatementBlock(self, ctx:ConnectITParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by ConnectITParser#forStmt.
    def enterForStmt(self, ctx:ConnectITParser.ForStmtContext):
        pass

    # Exit a parse tree produced by ConnectITParser#forStmt.
    def exitForStmt(self, ctx:ConnectITParser.ForStmtContext):
        pass


    # Enter a parse tree produced by ConnectITParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:ConnectITParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by ConnectITParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:ConnectITParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by ConnectITParser#returnExpr.
    def enterReturnExpr(self, ctx:ConnectITParser.ReturnExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#returnExpr.
    def exitReturnExpr(self, ctx:ConnectITParser.ReturnExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#dataType.
    def enterDataType(self, ctx:ConnectITParser.DataTypeContext):
        pass

    # Exit a parse tree produced by ConnectITParser#dataType.
    def exitDataType(self, ctx:ConnectITParser.DataTypeContext):
        pass



del ConnectITParser