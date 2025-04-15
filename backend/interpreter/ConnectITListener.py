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


    # Enter a parse tree produced by ConnectITParser#newUnit.
    def enterNewUnit(self, ctx:ConnectITParser.NewUnitContext):
        pass

    # Exit a parse tree produced by ConnectITParser#newUnit.
    def exitNewUnit(self, ctx:ConnectITParser.NewUnitContext):
        pass


    # Enter a parse tree produced by ConnectITParser#newLayer.
    def enterNewLayer(self, ctx:ConnectITParser.NewLayerContext):
        pass

    # Exit a parse tree produced by ConnectITParser#newLayer.
    def exitNewLayer(self, ctx:ConnectITParser.NewLayerContext):
        pass


    # Enter a parse tree produced by ConnectITParser#newShape.
    def enterNewShape(self, ctx:ConnectITParser.NewShapeContext):
        pass

    # Exit a parse tree produced by ConnectITParser#newShape.
    def exitNewShape(self, ctx:ConnectITParser.NewShapeContext):
        pass


    # Enter a parse tree produced by ConnectITParser#newModel.
    def enterNewModel(self, ctx:ConnectITParser.NewModelContext):
        pass

    # Exit a parse tree produced by ConnectITParser#newModel.
    def exitNewModel(self, ctx:ConnectITParser.NewModelContext):
        pass


    # Enter a parse tree produced by ConnectITParser#newNumber.
    def enterNewNumber(self, ctx:ConnectITParser.NewNumberContext):
        pass

    # Exit a parse tree produced by ConnectITParser#newNumber.
    def exitNewNumber(self, ctx:ConnectITParser.NewNumberContext):
        pass


    # Enter a parse tree produced by ConnectITParser#newBoolean.
    def enterNewBoolean(self, ctx:ConnectITParser.NewBooleanContext):
        pass

    # Exit a parse tree produced by ConnectITParser#newBoolean.
    def exitNewBoolean(self, ctx:ConnectITParser.NewBooleanContext):
        pass


    # Enter a parse tree produced by ConnectITParser#unitDeclarationList.
    def enterUnitDeclarationList(self, ctx:ConnectITParser.UnitDeclarationListContext):
        pass

    # Exit a parse tree produced by ConnectITParser#unitDeclarationList.
    def exitUnitDeclarationList(self, ctx:ConnectITParser.UnitDeclarationListContext):
        pass


    # Enter a parse tree produced by ConnectITParser#unitDeclaration.
    def enterUnitDeclaration(self, ctx:ConnectITParser.UnitDeclarationContext):
        pass

    # Exit a parse tree produced by ConnectITParser#unitDeclaration.
    def exitUnitDeclaration(self, ctx:ConnectITParser.UnitDeclarationContext):
        pass


    # Enter a parse tree produced by ConnectITParser#unitExpr.
    def enterUnitExpr(self, ctx:ConnectITParser.UnitExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#unitExpr.
    def exitUnitExpr(self, ctx:ConnectITParser.UnitExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#layerDeclarationList.
    def enterLayerDeclarationList(self, ctx:ConnectITParser.LayerDeclarationListContext):
        pass

    # Exit a parse tree produced by ConnectITParser#layerDeclarationList.
    def exitLayerDeclarationList(self, ctx:ConnectITParser.LayerDeclarationListContext):
        pass


    # Enter a parse tree produced by ConnectITParser#layerDeclaration.
    def enterLayerDeclaration(self, ctx:ConnectITParser.LayerDeclarationContext):
        pass

    # Exit a parse tree produced by ConnectITParser#layerDeclaration.
    def exitLayerDeclaration(self, ctx:ConnectITParser.LayerDeclarationContext):
        pass


    # Enter a parse tree produced by ConnectITParser#layerExpr.
    def enterLayerExpr(self, ctx:ConnectITParser.LayerExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#layerExpr.
    def exitLayerExpr(self, ctx:ConnectITParser.LayerExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#shapeDeclarationList.
    def enterShapeDeclarationList(self, ctx:ConnectITParser.ShapeDeclarationListContext):
        pass

    # Exit a parse tree produced by ConnectITParser#shapeDeclarationList.
    def exitShapeDeclarationList(self, ctx:ConnectITParser.ShapeDeclarationListContext):
        pass


    # Enter a parse tree produced by ConnectITParser#shapeDeclaration.
    def enterShapeDeclaration(self, ctx:ConnectITParser.ShapeDeclarationContext):
        pass

    # Exit a parse tree produced by ConnectITParser#shapeDeclaration.
    def exitShapeDeclaration(self, ctx:ConnectITParser.ShapeDeclarationContext):
        pass


    # Enter a parse tree produced by ConnectITParser#shapeExpr.
    def enterShapeExpr(self, ctx:ConnectITParser.ShapeExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#shapeExpr.
    def exitShapeExpr(self, ctx:ConnectITParser.ShapeExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#modelDeclarationList.
    def enterModelDeclarationList(self, ctx:ConnectITParser.ModelDeclarationListContext):
        pass

    # Exit a parse tree produced by ConnectITParser#modelDeclarationList.
    def exitModelDeclarationList(self, ctx:ConnectITParser.ModelDeclarationListContext):
        pass


    # Enter a parse tree produced by ConnectITParser#modelDeclaration.
    def enterModelDeclaration(self, ctx:ConnectITParser.ModelDeclarationContext):
        pass

    # Exit a parse tree produced by ConnectITParser#modelDeclaration.
    def exitModelDeclaration(self, ctx:ConnectITParser.ModelDeclarationContext):
        pass


    # Enter a parse tree produced by ConnectITParser#modelExpr.
    def enterModelExpr(self, ctx:ConnectITParser.ModelExprContext):
        pass

    # Exit a parse tree produced by ConnectITParser#modelExpr.
    def exitModelExpr(self, ctx:ConnectITParser.ModelExprContext):
        pass


    # Enter a parse tree produced by ConnectITParser#numberDeclarationList.
    def enterNumberDeclarationList(self, ctx:ConnectITParser.NumberDeclarationListContext):
        pass

    # Exit a parse tree produced by ConnectITParser#numberDeclarationList.
    def exitNumberDeclarationList(self, ctx:ConnectITParser.NumberDeclarationListContext):
        pass


    # Enter a parse tree produced by ConnectITParser#numberDeclaration.
    def enterNumberDeclaration(self, ctx:ConnectITParser.NumberDeclarationContext):
        pass

    # Exit a parse tree produced by ConnectITParser#numberDeclaration.
    def exitNumberDeclaration(self, ctx:ConnectITParser.NumberDeclarationContext):
        pass


    # Enter a parse tree produced by ConnectITParser#booleanDeclarationList.
    def enterBooleanDeclarationList(self, ctx:ConnectITParser.BooleanDeclarationListContext):
        pass

    # Exit a parse tree produced by ConnectITParser#booleanDeclarationList.
    def exitBooleanDeclarationList(self, ctx:ConnectITParser.BooleanDeclarationListContext):
        pass


    # Enter a parse tree produced by ConnectITParser#booleanDeclaration.
    def enterBooleanDeclaration(self, ctx:ConnectITParser.BooleanDeclarationContext):
        pass

    # Exit a parse tree produced by ConnectITParser#booleanDeclaration.
    def exitBooleanDeclaration(self, ctx:ConnectITParser.BooleanDeclarationContext):
        pass


    # Enter a parse tree produced by ConnectITParser#assignment.
    def enterAssignment(self, ctx:ConnectITParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ConnectITParser#assignment.
    def exitAssignment(self, ctx:ConnectITParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ConnectITParser#expression.
    def enterExpression(self, ctx:ConnectITParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ConnectITParser#expression.
    def exitExpression(self, ctx:ConnectITParser.ExpressionContext):
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


    # Enter a parse tree produced by ConnectITParser#type.
    def enterType(self, ctx:ConnectITParser.TypeContext):
        pass

    # Exit a parse tree produced by ConnectITParser#type.
    def exitType(self, ctx:ConnectITParser.TypeContext):
        pass



del ConnectITParser