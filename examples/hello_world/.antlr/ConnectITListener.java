// Generated from c:/Users/koteke/Desktop/connectIT/connectIT/examples/hello_world/ConnectIT.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ConnectITParser}.
 */
public interface ConnectITListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ConnectITParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ConnectITParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ConnectITParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ConnectITParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unitDeclaration}
	 * labeled alternative in {@link ConnectITParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterUnitDeclaration(ConnectITParser.UnitDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unitDeclaration}
	 * labeled alternative in {@link ConnectITParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitUnitDeclaration(ConnectITParser.UnitDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code layerDeclaration}
	 * labeled alternative in {@link ConnectITParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterLayerDeclaration(ConnectITParser.LayerDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code layerDeclaration}
	 * labeled alternative in {@link ConnectITParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitLayerDeclaration(ConnectITParser.LayerDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code shapeDeclaration}
	 * labeled alternative in {@link ConnectITParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterShapeDeclaration(ConnectITParser.ShapeDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code shapeDeclaration}
	 * labeled alternative in {@link ConnectITParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitShapeDeclaration(ConnectITParser.ShapeDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code modelDeclaration}
	 * labeled alternative in {@link ConnectITParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterModelDeclaration(ConnectITParser.ModelDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code modelDeclaration}
	 * labeled alternative in {@link ConnectITParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitModelDeclaration(ConnectITParser.ModelDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#unitAssigmentList}.
	 * @param ctx the parse tree
	 */
	void enterUnitAssigmentList(ConnectITParser.UnitAssigmentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#unitAssigmentList}.
	 * @param ctx the parse tree
	 */
	void exitUnitAssigmentList(ConnectITParser.UnitAssigmentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#unitAssignment}.
	 * @param ctx the parse tree
	 */
	void enterUnitAssignment(ConnectITParser.UnitAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#unitAssignment}.
	 * @param ctx the parse tree
	 */
	void exitUnitAssignment(ConnectITParser.UnitAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#layerAssigmentList}.
	 * @param ctx the parse tree
	 */
	void enterLayerAssigmentList(ConnectITParser.LayerAssigmentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#layerAssigmentList}.
	 * @param ctx the parse tree
	 */
	void exitLayerAssigmentList(ConnectITParser.LayerAssigmentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#layerAssignment}.
	 * @param ctx the parse tree
	 */
	void enterLayerAssignment(ConnectITParser.LayerAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#layerAssignment}.
	 * @param ctx the parse tree
	 */
	void exitLayerAssignment(ConnectITParser.LayerAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#idList}.
	 * @param ctx the parse tree
	 */
	void enterIdList(ConnectITParser.IdListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#idList}.
	 * @param ctx the parse tree
	 */
	void exitIdList(ConnectITParser.IdListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ConnectITParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ConnectITParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ConnectITParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ConnectITParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#unitExpr}.
	 * @param ctx the parse tree
	 */
	void enterUnitExpr(ConnectITParser.UnitExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#unitExpr}.
	 * @param ctx the parse tree
	 */
	void exitUnitExpr(ConnectITParser.UnitExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#layerExpr}.
	 * @param ctx the parse tree
	 */
	void enterLayerExpr(ConnectITParser.LayerExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#layerExpr}.
	 * @param ctx the parse tree
	 */
	void exitLayerExpr(ConnectITParser.LayerExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#shapeDef}.
	 * @param ctx the parse tree
	 */
	void enterShapeDef(ConnectITParser.ShapeDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#shapeDef}.
	 * @param ctx the parse tree
	 */
	void exitShapeDef(ConnectITParser.ShapeDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#layerChain}.
	 * @param ctx the parse tree
	 */
	void enterLayerChain(ConnectITParser.LayerChainContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#layerChain}.
	 * @param ctx the parse tree
	 */
	void exitLayerChain(ConnectITParser.LayerChainContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#modelDef}.
	 * @param ctx the parse tree
	 */
	void enterModelDef(ConnectITParser.ModelDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#modelDef}.
	 * @param ctx the parse tree
	 */
	void exitModelDef(ConnectITParser.ModelDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#shapeChain}.
	 * @param ctx the parse tree
	 */
	void enterShapeChain(ConnectITParser.ShapeChainContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#shapeChain}.
	 * @param ctx the parse tree
	 */
	void exitShapeChain(ConnectITParser.ShapeChainContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowStatement(ConnectITParser.ShowStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowStatement(ConnectITParser.ShowStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(ConnectITParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(ConnectITParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(ConnectITParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(ConnectITParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(ConnectITParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(ConnectITParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#statementBlock}.
	 * @param ctx the parse tree
	 */
	void enterStatementBlock(ConnectITParser.StatementBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#statementBlock}.
	 * @param ctx the parse tree
	 */
	void exitStatementBlock(ConnectITParser.StatementBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(ConnectITParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(ConnectITParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#functionDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDeclaration(ConnectITParser.FunctionDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#functionDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDeclaration(ConnectITParser.FunctionDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#returnExpr}.
	 * @param ctx the parse tree
	 */
	void enterReturnExpr(ConnectITParser.ReturnExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#returnExpr}.
	 * @param ctx the parse tree
	 */
	void exitReturnExpr(ConnectITParser.ReturnExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConnectITParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(ConnectITParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConnectITParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(ConnectITParser.TypeContext ctx);
}