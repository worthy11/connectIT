// Generated from c:/Users/koteke/Desktop/connectIT/connectIT/examples/hello_world/ConnectIT.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ConnectITParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, ID=34, NUMBER=35, COLOR=36, PATTERN=37, WS=38, NEWLINE=39;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_declaration = 2, RULE_unitAssigmentList = 3, 
		RULE_unitAssignment = 4, RULE_layerAssigmentList = 5, RULE_layerAssignment = 6, 
		RULE_idList = 7, RULE_assignment = 8, RULE_expression = 9, RULE_unitExpr = 10, 
		RULE_layerExpr = 11, RULE_shapeDef = 12, RULE_layerChain = 13, RULE_modelDef = 14, 
		RULE_shapeChain = 15, RULE_showStatement = 16, RULE_ifStmt = 17, RULE_whileStmt = 18, 
		RULE_condition = 19, RULE_statementBlock = 20, RULE_forStmt = 21, RULE_functionDeclaration = 22, 
		RULE_returnExpr = 23, RULE_type = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "declaration", "unitAssigmentList", "unitAssignment", 
			"layerAssigmentList", "layerAssignment", "idList", "assignment", "expression", 
			"unitExpr", "layerExpr", "shapeDef", "layerChain", "modelDef", "shapeChain", 
			"showStatement", "ifStmt", "whileStmt", "condition", "statementBlock", 
			"forStmt", "functionDeclaration", "returnExpr", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'UNIT'", "'LAYER'", "'SHAPE'", "'MODEL'", "','", "'='", "'-->'", 
			"'*'", "'+'", "'<-'", "'<<-'", "'-'", "'SHOW'", "'IF'", "'['", "']'", 
			"'ELSE IF'", "'ELSE'", "'REPEAT WHILE'", "'<'", "'<='", "'>'", "'>='", 
			"'=='", "'!='", "'REPEAT'", "'TIMES'", "'METHOD'", "'('", "')'", "'RETURNS'", 
			"'RETURN'", "'NUMBER'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, "ID", "NUMBER", 
			"COLOR", "PATTERN", "WS", "NEWLINE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ConnectIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ConnectITParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ConnectITParser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(ConnectITParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ConnectITParser.NEWLINE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(50);
					match(NEWLINE);
					}
					} 
				}
				setState(55);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(70);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(56);
					statement();
					setState(65);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
					while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
						if ( _alt==1 ) {
							{
							{
							setState(58); 
							_errHandler.sync(this);
							_alt = 1;
							do {
								switch (_alt) {
								case 1:
									{
									{
									setState(57);
									match(NEWLINE);
									}
									}
									break;
								default:
									throw new NoViableAltException(this);
								}
								setState(60); 
								_errHandler.sync(this);
								_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
							} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
							setState(62);
							statement();
							}
							} 
						}
						setState(67);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
					}
					}
					} 
				}
				setState(72);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(73);
				match(NEWLINE);
				}
				}
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(79);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ShapeDefContext shapeDef() {
			return getRuleContext(ShapeDefContext.class,0);
		}
		public ModelDefContext modelDef() {
			return getRuleContext(ModelDefContext.class,0);
		}
		public ShowStatementContext showStatement() {
			return getRuleContext(ShowStatementContext.class,0);
		}
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public ForStmtContext forStmt() {
			return getRuleContext(ForStmtContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public FunctionDeclarationContext functionDeclaration() {
			return getRuleContext(FunctionDeclarationContext.class,0);
		}
		public ReturnExprContext returnExpr() {
			return getRuleContext(ReturnExprContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(91);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(82);
				assignment();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(83);
				shapeDef();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(84);
				modelDef();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(85);
				showStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(86);
				whileStmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(87);
				forStmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(88);
				ifStmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(89);
				functionDeclaration();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(90);
				returnExpr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	 
		public DeclarationContext() { }
		public void copyFrom(DeclarationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ShapeDeclarationContext extends DeclarationContext {
		public IdListContext idList() {
			return getRuleContext(IdListContext.class,0);
		}
		public ShapeDeclarationContext(DeclarationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModelDeclarationContext extends DeclarationContext {
		public IdListContext idList() {
			return getRuleContext(IdListContext.class,0);
		}
		public ModelDeclarationContext(DeclarationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LayerDeclarationContext extends DeclarationContext {
		public LayerAssigmentListContext layerAssigmentList() {
			return getRuleContext(LayerAssigmentListContext.class,0);
		}
		public LayerDeclarationContext(DeclarationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnitDeclarationContext extends DeclarationContext {
		public UnitAssigmentListContext unitAssigmentList() {
			return getRuleContext(UnitAssigmentListContext.class,0);
		}
		public UnitDeclarationContext(DeclarationContext ctx) { copyFrom(ctx); }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaration);
		try {
			setState(101);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new UnitDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(93);
				match(T__0);
				setState(94);
				unitAssigmentList();
				}
				break;
			case T__1:
				_localctx = new LayerDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				match(T__1);
				setState(96);
				layerAssigmentList();
				}
				break;
			case T__2:
				_localctx = new ShapeDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(97);
				match(T__2);
				setState(98);
				idList();
				}
				break;
			case T__3:
				_localctx = new ModelDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(99);
				match(T__3);
				setState(100);
				idList();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnitAssigmentListContext extends ParserRuleContext {
		public List<UnitAssignmentContext> unitAssignment() {
			return getRuleContexts(UnitAssignmentContext.class);
		}
		public UnitAssignmentContext unitAssignment(int i) {
			return getRuleContext(UnitAssignmentContext.class,i);
		}
		public UnitAssigmentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unitAssigmentList; }
	}

	public final UnitAssigmentListContext unitAssigmentList() throws RecognitionException {
		UnitAssigmentListContext _localctx = new UnitAssigmentListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_unitAssigmentList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			unitAssignment();
			setState(108);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(104);
					match(T__4);
					setState(105);
					unitAssignment();
					}
					} 
				}
				setState(110);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnitAssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public UnitExprContext unitExpr() {
			return getRuleContext(UnitExprContext.class,0);
		}
		public UnitAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unitAssignment; }
	}

	public final UnitAssignmentContext unitAssignment() throws RecognitionException {
		UnitAssignmentContext _localctx = new UnitAssignmentContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_unitAssignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(ID);
			setState(114);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(112);
				match(T__5);
				setState(113);
				unitExpr();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LayerAssigmentListContext extends ParserRuleContext {
		public List<LayerAssignmentContext> layerAssignment() {
			return getRuleContexts(LayerAssignmentContext.class);
		}
		public LayerAssignmentContext layerAssignment(int i) {
			return getRuleContext(LayerAssignmentContext.class,i);
		}
		public LayerAssigmentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_layerAssigmentList; }
	}

	public final LayerAssigmentListContext layerAssigmentList() throws RecognitionException {
		LayerAssigmentListContext _localctx = new LayerAssigmentListContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_layerAssigmentList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			layerAssignment();
			setState(121);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(117);
					match(T__4);
					setState(118);
					layerAssignment();
					}
					} 
				}
				setState(123);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LayerAssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public LayerExprContext layerExpr() {
			return getRuleContext(LayerExprContext.class,0);
		}
		public LayerAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_layerAssignment; }
	}

	public final LayerAssignmentContext layerAssignment() throws RecognitionException {
		LayerAssignmentContext _localctx = new LayerAssignmentContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_layerAssignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(ID);
			setState(127);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(125);
				match(T__5);
				setState(126);
				layerExpr(0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdListContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(ConnectITParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(ConnectITParser.ID, i);
		}
		public IdListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idList; }
	}

	public final IdListContext idList() throws RecognitionException {
		IdListContext _localctx = new IdListContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_idList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(ID);
			setState(134);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(130);
					match(T__4);
					setState(131);
					match(ID);
					}
					} 
				}
				setState(136);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LayerChainContext layerChain() {
			return getRuleContext(LayerChainContext.class,0);
		}
		public ShapeChainContext shapeChain() {
			return getRuleContext(ShapeChainContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_assignment);
		try {
			setState(148);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				match(ID);
				setState(138);
				match(T__5);
				setState(139);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				layerChain();
				setState(141);
				match(T__6);
				setState(142);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(144);
				shapeChain();
				setState(145);
				match(T__6);
				setState(146);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public UnitExprContext unitExpr() {
			return getRuleContext(UnitExprContext.class,0);
		}
		public LayerExprContext layerExpr() {
			return getRuleContext(LayerExprContext.class,0);
		}
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_expression);
		try {
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				unitExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				layerExpr(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(152);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnitExprContext extends ParserRuleContext {
		public TerminalNode COLOR() { return getToken(ConnectITParser.COLOR, 0); }
		public TerminalNode PATTERN() { return getToken(ConnectITParser.PATTERN, 0); }
		public UnitExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unitExpr; }
	}

	public final UnitExprContext unitExpr() throws RecognitionException {
		UnitExprContext _localctx = new UnitExprContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_unitExpr);
		try {
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(155);
				match(COLOR);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(156);
				match(PATTERN);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LayerExprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public TerminalNode NUMBER() { return getToken(ConnectITParser.NUMBER, 0); }
		public List<LayerExprContext> layerExpr() {
			return getRuleContexts(LayerExprContext.class);
		}
		public LayerExprContext layerExpr(int i) {
			return getRuleContext(LayerExprContext.class,i);
		}
		public LayerExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_layerExpr; }
	}

	public final LayerExprContext layerExpr() throws RecognitionException {
		return layerExpr(0);
	}

	private LayerExprContext layerExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		LayerExprContext _localctx = new LayerExprContext(_ctx, _parentState);
		LayerExprContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_layerExpr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(161);
				match(ID);
				setState(162);
				match(T__7);
				setState(163);
				match(NUMBER);
				}
				break;
			case 2:
				{
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(172);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new LayerExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_layerExpr);
					setState(167);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(168);
					match(T__8);
					setState(169);
					layerExpr(3);
					}
					} 
				}
				setState(174);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShapeDefContext extends ParserRuleContext {
		public LayerChainContext layerChain() {
			return getRuleContext(LayerChainContext.class,0);
		}
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public ShapeDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shapeDef; }
	}

	public final ShapeDefContext shapeDef() throws RecognitionException {
		ShapeDefContext _localctx = new ShapeDefContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_shapeDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			layerChain();
			setState(176);
			match(T__6);
			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(177);
				match(T__2);
				}
			}

			setState(180);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LayerChainContext extends ParserRuleContext {
		public LayerExprContext layerExpr() {
			return getRuleContext(LayerExprContext.class,0);
		}
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public LayerChainContext layerChain() {
			return getRuleContext(LayerChainContext.class,0);
		}
		public TerminalNode NUMBER() { return getToken(ConnectITParser.NUMBER, 0); }
		public LayerChainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_layerChain; }
	}

	public final LayerChainContext layerChain() throws RecognitionException {
		LayerChainContext _localctx = new LayerChainContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_layerChain);
		int _la;
		try {
			setState(208);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(184);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
				case 1:
					{
					setState(182);
					layerExpr(0);
					}
					break;
				case 2:
					{
					setState(183);
					match(ID);
					}
					break;
				}
				setState(188);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9) {
					{
					setState(186);
					match(T__9);
					setState(187);
					layerChain();
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(192);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
				case 1:
					{
					setState(190);
					layerExpr(0);
					}
					break;
				case 2:
					{
					setState(191);
					match(ID);
					}
					break;
				}
				setState(196);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(194);
					match(T__10);
					setState(195);
					layerChain();
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(200);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
				case 1:
					{
					setState(198);
					layerExpr(0);
					}
					break;
				case 2:
					{
					setState(199);
					match(ID);
					}
					break;
				}
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9) {
					{
					setState(202);
					match(T__9);
					setState(203);
					match(NUMBER);
					setState(204);
					match(T__11);
					setState(205);
					layerChain();
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModelDefContext extends ParserRuleContext {
		public ShapeChainContext shapeChain() {
			return getRuleContext(ShapeChainContext.class,0);
		}
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public ModelDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modelDef; }
	}

	public final ModelDefContext modelDef() throws RecognitionException {
		ModelDefContext _localctx = new ModelDefContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_modelDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			shapeChain();
			setState(211);
			match(T__6);
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(212);
				match(T__3);
				}
			}

			setState(215);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShapeChainContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public ShapeChainContext shapeChain() {
			return getRuleContext(ShapeChainContext.class,0);
		}
		public ShapeChainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shapeChain; }
	}

	public final ShapeChainContext shapeChain() throws RecognitionException {
		ShapeChainContext _localctx = new ShapeChainContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_shapeChain);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(ID);
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(218);
				match(T__9);
				setState(219);
				shapeChain();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShowStatementContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public ShowStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_showStatement; }
	}

	public final ShowStatementContext showStatement() throws RecognitionException {
		ShowStatementContext _localctx = new ShowStatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_showStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			match(T__12);
			setState(223);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends ParserRuleContext {
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<StatementBlockContext> statementBlock() {
			return getRuleContexts(StatementBlockContext.class);
		}
		public StatementBlockContext statementBlock(int i) {
			return getRuleContext(StatementBlockContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(ConnectITParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ConnectITParser.NEWLINE, i);
		}
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_ifStmt);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(T__13);
			setState(226);
			condition();
			setState(228);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NEWLINE) {
				{
				setState(227);
				match(NEWLINE);
				}
			}

			setState(230);
			match(T__14);
			setState(231);
			statementBlock();
			setState(233);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NEWLINE) {
				{
				setState(232);
				match(NEWLINE);
				}
			}

			setState(235);
			match(T__15);
			setState(253);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(237);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==NEWLINE) {
						{
						setState(236);
						match(NEWLINE);
						}
					}

					setState(239);
					match(T__16);
					setState(240);
					condition();
					setState(242);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==NEWLINE) {
						{
						setState(241);
						match(NEWLINE);
						}
					}

					setState(244);
					match(T__14);
					setState(245);
					statementBlock();
					setState(247);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==NEWLINE) {
						{
						setState(246);
						match(NEWLINE);
						}
					}

					setState(249);
					match(T__15);
					}
					} 
				}
				setState(255);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
			}
			setState(270);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(257);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NEWLINE) {
					{
					setState(256);
					match(NEWLINE);
					}
				}

				setState(259);
				match(T__17);
				setState(261);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NEWLINE) {
					{
					setState(260);
					match(NEWLINE);
					}
				}

				setState(263);
				match(T__14);
				setState(264);
				statementBlock();
				setState(266);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NEWLINE) {
					{
					setState(265);
					match(NEWLINE);
					}
				}

				setState(268);
				match(T__15);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStmtContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public StatementBlockContext statementBlock() {
			return getRuleContext(StatementBlockContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(ConnectITParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ConnectITParser.NEWLINE, i);
		}
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_whileStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(T__18);
			setState(273);
			condition();
			setState(275);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NEWLINE) {
				{
				setState(274);
				match(NEWLINE);
				}
			}

			setState(277);
			match(T__14);
			setState(278);
			statementBlock();
			setState(280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NEWLINE) {
				{
				setState(279);
				match(NEWLINE);
				}
			}

			setState(282);
			match(T__15);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			expression();
			setState(285);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 66060288L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(286);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementBlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(ConnectITParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ConnectITParser.NEWLINE, i);
		}
		public StatementBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementBlock; }
	}

	public final StatementBlockContext statementBlock() throws RecognitionException {
		StatementBlockContext _localctx = new StatementBlockContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_statementBlock);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			statement();
			setState(293);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(289);
					match(NEWLINE);
					setState(290);
					statement();
					}
					} 
				}
				setState(295);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStmtContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(ConnectITParser.NUMBER, 0); }
		public StatementBlockContext statementBlock() {
			return getRuleContext(StatementBlockContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ConnectITParser.NEWLINE, 0); }
		public ForStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStmt; }
	}

	public final ForStmtContext forStmt() throws RecognitionException {
		ForStmtContext _localctx = new ForStmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_forStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			match(T__25);
			setState(297);
			match(NUMBER);
			setState(298);
			match(T__26);
			setState(300);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				{
				setState(299);
				match(NEWLINE);
				}
				break;
			}
			setState(302);
			statementBlock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclarationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public StatementBlockContext statementBlock() {
			return getRuleContext(StatementBlockContext.class,0);
		}
		public ReturnExprContext returnExpr() {
			return getRuleContext(ReturnExprContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ConnectITParser.NEWLINE, 0); }
		public FunctionDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclaration; }
	}

	public final FunctionDeclarationContext functionDeclaration() throws RecognitionException {
		FunctionDeclarationContext _localctx = new FunctionDeclarationContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_functionDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(304);
			match(T__27);
			setState(305);
			match(ID);
			setState(306);
			match(T__28);
			setState(310);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589934622L) != 0)) {
				{
				{
				setState(307);
				type();
				}
				}
				setState(312);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(313);
			match(T__29);
			setState(314);
			match(T__30);
			setState(315);
			type();
			setState(316);
			match(T__14);
			setState(317);
			statementBlock();
			setState(318);
			returnExpr();
			setState(320);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NEWLINE) {
				{
				setState(319);
				match(NEWLINE);
				}
			}

			setState(322);
			match(T__15);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnExprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ConnectITParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnExpr; }
	}

	public final ReturnExprContext returnExpr() throws RecognitionException {
		ReturnExprContext _localctx = new ReturnExprContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_returnExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
			match(T__31);
			setState(327);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,43,_ctx) ) {
			case 1:
				{
				setState(325);
				match(ID);
				}
				break;
			case 2:
				{
				setState(326);
				expression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589934622L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 11:
			return layerExpr_sempred((LayerExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean layerExpr_sempred(LayerExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\'\u014c\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0001\u0000\u0005\u00004\b\u0000\n\u0000\f\u00007\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0004\u0000;\b\u0000\u000b\u0000\f\u0000<\u0001\u0000\u0005"+
		"\u0000@\b\u0000\n\u0000\f\u0000C\t\u0000\u0005\u0000E\b\u0000\n\u0000"+
		"\f\u0000H\t\u0000\u0001\u0000\u0005\u0000K\b\u0000\n\u0000\f\u0000N\t"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u0001\\\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002f\b"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003k\b\u0003\n\u0003"+
		"\f\u0003n\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004s\b\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005x\b\u0005\n\u0005\f\u0005"+
		"{\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0080\b\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u0085\b\u0007\n\u0007"+
		"\f\u0007\u0088\t\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0095\b\b\u0001\t\u0001"+
		"\t\u0001\t\u0003\t\u009a\b\t\u0001\n\u0001\n\u0001\n\u0003\n\u009f\b\n"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b"+
		"\u00a6\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u00ab\b"+
		"\u000b\n\u000b\f\u000b\u00ae\t\u000b\u0001\f\u0001\f\u0001\f\u0003\f\u00b3"+
		"\b\f\u0001\f\u0001\f\u0001\r\u0001\r\u0003\r\u00b9\b\r\u0001\r\u0001\r"+
		"\u0003\r\u00bd\b\r\u0001\r\u0001\r\u0003\r\u00c1\b\r\u0001\r\u0001\r\u0003"+
		"\r\u00c5\b\r\u0001\r\u0001\r\u0003\r\u00c9\b\r\u0001\r\u0001\r\u0001\r"+
		"\u0001\r\u0003\r\u00cf\b\r\u0003\r\u00d1\b\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0003\u000e\u00d6\b\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u00dd\b\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00e5\b\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00ea\b\u0011\u0001\u0011\u0001"+
		"\u0011\u0003\u0011\u00ee\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003"+
		"\u0011\u00f3\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00f8"+
		"\b\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u00fc\b\u0011\n\u0011\f\u0011"+
		"\u00ff\t\u0011\u0001\u0011\u0003\u0011\u0102\b\u0011\u0001\u0011\u0001"+
		"\u0011\u0003\u0011\u0106\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003"+
		"\u0011\u010b\b\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u010f\b\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u0114\b\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0003\u0012\u0119\b\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0005\u0014\u0124\b\u0014\n\u0014\f\u0014\u0127\t\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u012d\b\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0005"+
		"\u0016\u0135\b\u0016\n\u0016\f\u0016\u0138\t\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016"+
		"\u0141\b\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0003\u0017\u0148\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0000\u0001"+
		"\u0016\u0019\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.0\u0000\u0002\u0001\u0000\u0014\u0019"+
		"\u0002\u0000\u0001\u0004!!\u016c\u00005\u0001\u0000\u0000\u0000\u0002"+
		"[\u0001\u0000\u0000\u0000\u0004e\u0001\u0000\u0000\u0000\u0006g\u0001"+
		"\u0000\u0000\u0000\bo\u0001\u0000\u0000\u0000\nt\u0001\u0000\u0000\u0000"+
		"\f|\u0001\u0000\u0000\u0000\u000e\u0081\u0001\u0000\u0000\u0000\u0010"+
		"\u0094\u0001\u0000\u0000\u0000\u0012\u0099\u0001\u0000\u0000\u0000\u0014"+
		"\u009e\u0001\u0000\u0000\u0000\u0016\u00a5\u0001\u0000\u0000\u0000\u0018"+
		"\u00af\u0001\u0000\u0000\u0000\u001a\u00d0\u0001\u0000\u0000\u0000\u001c"+
		"\u00d2\u0001\u0000\u0000\u0000\u001e\u00d9\u0001\u0000\u0000\u0000 \u00de"+
		"\u0001\u0000\u0000\u0000\"\u00e1\u0001\u0000\u0000\u0000$\u0110\u0001"+
		"\u0000\u0000\u0000&\u011c\u0001\u0000\u0000\u0000(\u0120\u0001\u0000\u0000"+
		"\u0000*\u0128\u0001\u0000\u0000\u0000,\u0130\u0001\u0000\u0000\u0000."+
		"\u0144\u0001\u0000\u0000\u00000\u0149\u0001\u0000\u0000\u000024\u0005"+
		"\'\u0000\u000032\u0001\u0000\u0000\u000047\u0001\u0000\u0000\u000053\u0001"+
		"\u0000\u0000\u000056\u0001\u0000\u0000\u00006F\u0001\u0000\u0000\u0000"+
		"75\u0001\u0000\u0000\u00008A\u0003\u0002\u0001\u00009;\u0005\'\u0000\u0000"+
		":9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000"+
		"\u0000<=\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000>@\u0003\u0002"+
		"\u0001\u0000?:\u0001\u0000\u0000\u0000@C\u0001\u0000\u0000\u0000A?\u0001"+
		"\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000BE\u0001\u0000\u0000\u0000"+
		"CA\u0001\u0000\u0000\u0000D8\u0001\u0000\u0000\u0000EH\u0001\u0000\u0000"+
		"\u0000FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GL\u0001\u0000"+
		"\u0000\u0000HF\u0001\u0000\u0000\u0000IK\u0005\'\u0000\u0000JI\u0001\u0000"+
		"\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000LM\u0001"+
		"\u0000\u0000\u0000MO\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000"+
		"OP\u0005\u0000\u0000\u0001P\u0001\u0001\u0000\u0000\u0000Q\\\u0003\u0004"+
		"\u0002\u0000R\\\u0003\u0010\b\u0000S\\\u0003\u0018\f\u0000T\\\u0003\u001c"+
		"\u000e\u0000U\\\u0003 \u0010\u0000V\\\u0003$\u0012\u0000W\\\u0003*\u0015"+
		"\u0000X\\\u0003\"\u0011\u0000Y\\\u0003,\u0016\u0000Z\\\u0003.\u0017\u0000"+
		"[Q\u0001\u0000\u0000\u0000[R\u0001\u0000\u0000\u0000[S\u0001\u0000\u0000"+
		"\u0000[T\u0001\u0000\u0000\u0000[U\u0001\u0000\u0000\u0000[V\u0001\u0000"+
		"\u0000\u0000[W\u0001\u0000\u0000\u0000[X\u0001\u0000\u0000\u0000[Y\u0001"+
		"\u0000\u0000\u0000[Z\u0001\u0000\u0000\u0000\\\u0003\u0001\u0000\u0000"+
		"\u0000]^\u0005\u0001\u0000\u0000^f\u0003\u0006\u0003\u0000_`\u0005\u0002"+
		"\u0000\u0000`f\u0003\n\u0005\u0000ab\u0005\u0003\u0000\u0000bf\u0003\u000e"+
		"\u0007\u0000cd\u0005\u0004\u0000\u0000df\u0003\u000e\u0007\u0000e]\u0001"+
		"\u0000\u0000\u0000e_\u0001\u0000\u0000\u0000ea\u0001\u0000\u0000\u0000"+
		"ec\u0001\u0000\u0000\u0000f\u0005\u0001\u0000\u0000\u0000gl\u0003\b\u0004"+
		"\u0000hi\u0005\u0005\u0000\u0000ik\u0003\b\u0004\u0000jh\u0001\u0000\u0000"+
		"\u0000kn\u0001\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000lm\u0001\u0000"+
		"\u0000\u0000m\u0007\u0001\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000"+
		"or\u0005\"\u0000\u0000pq\u0005\u0006\u0000\u0000qs\u0003\u0014\n\u0000"+
		"rp\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000s\t\u0001\u0000\u0000"+
		"\u0000ty\u0003\f\u0006\u0000uv\u0005\u0005\u0000\u0000vx\u0003\f\u0006"+
		"\u0000wu\u0001\u0000\u0000\u0000x{\u0001\u0000\u0000\u0000yw\u0001\u0000"+
		"\u0000\u0000yz\u0001\u0000\u0000\u0000z\u000b\u0001\u0000\u0000\u0000"+
		"{y\u0001\u0000\u0000\u0000|\u007f\u0005\"\u0000\u0000}~\u0005\u0006\u0000"+
		"\u0000~\u0080\u0003\u0016\u000b\u0000\u007f}\u0001\u0000\u0000\u0000\u007f"+
		"\u0080\u0001\u0000\u0000\u0000\u0080\r\u0001\u0000\u0000\u0000\u0081\u0086"+
		"\u0005\"\u0000\u0000\u0082\u0083\u0005\u0005\u0000\u0000\u0083\u0085\u0005"+
		"\"\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0088\u0001\u0000"+
		"\u0000\u0000\u0086\u0084\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000"+
		"\u0000\u0000\u0087\u000f\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000"+
		"\u0000\u0000\u0089\u008a\u0005\"\u0000\u0000\u008a\u008b\u0005\u0006\u0000"+
		"\u0000\u008b\u0095\u0003\u0012\t\u0000\u008c\u008d\u0003\u001a\r\u0000"+
		"\u008d\u008e\u0005\u0007\u0000\u0000\u008e\u008f\u0005\"\u0000\u0000\u008f"+
		"\u0095\u0001\u0000\u0000\u0000\u0090\u0091\u0003\u001e\u000f\u0000\u0091"+
		"\u0092\u0005\u0007\u0000\u0000\u0092\u0093\u0005\"\u0000\u0000\u0093\u0095"+
		"\u0001\u0000\u0000\u0000\u0094\u0089\u0001\u0000\u0000\u0000\u0094\u008c"+
		"\u0001\u0000\u0000\u0000\u0094\u0090\u0001\u0000\u0000\u0000\u0095\u0011"+
		"\u0001\u0000\u0000\u0000\u0096\u009a\u0003\u0014\n\u0000\u0097\u009a\u0003"+
		"\u0016\u000b\u0000\u0098\u009a\u0005\"\u0000\u0000\u0099\u0096\u0001\u0000"+
		"\u0000\u0000\u0099\u0097\u0001\u0000\u0000\u0000\u0099\u0098\u0001\u0000"+
		"\u0000\u0000\u009a\u0013\u0001\u0000\u0000\u0000\u009b\u009f\u0005$\u0000"+
		"\u0000\u009c\u009f\u0005%\u0000\u0000\u009d\u009f\u0001\u0000\u0000\u0000"+
		"\u009e\u009b\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000"+
		"\u009e\u009d\u0001\u0000\u0000\u0000\u009f\u0015\u0001\u0000\u0000\u0000"+
		"\u00a0\u00a1\u0006\u000b\uffff\uffff\u0000\u00a1\u00a2\u0005\"\u0000\u0000"+
		"\u00a2\u00a3\u0005\b\u0000\u0000\u00a3\u00a6\u0005#\u0000\u0000\u00a4"+
		"\u00a6\u0001\u0000\u0000\u0000\u00a5\u00a0\u0001\u0000\u0000\u0000\u00a5"+
		"\u00a4\u0001\u0000\u0000\u0000\u00a6\u00ac\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a8\n\u0002\u0000\u0000\u00a8\u00a9\u0005\t\u0000\u0000\u00a9\u00ab"+
		"\u0003\u0016\u000b\u0003\u00aa\u00a7\u0001\u0000\u0000\u0000\u00ab\u00ae"+
		"\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ac\u00ad"+
		"\u0001\u0000\u0000\u0000\u00ad\u0017\u0001\u0000\u0000\u0000\u00ae\u00ac"+
		"\u0001\u0000\u0000\u0000\u00af\u00b0\u0003\u001a\r\u0000\u00b0\u00b2\u0005"+
		"\u0007\u0000\u0000\u00b1\u00b3\u0005\u0003\u0000\u0000\u00b2\u00b1\u0001"+
		"\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3\u00b4\u0001"+
		"\u0000\u0000\u0000\u00b4\u00b5\u0005\"\u0000\u0000\u00b5\u0019\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b9\u0003\u0016\u000b\u0000\u00b7\u00b9\u0005\"\u0000"+
		"\u0000\u00b8\u00b6\u0001\u0000\u0000\u0000\u00b8\u00b7\u0001\u0000\u0000"+
		"\u0000\u00b9\u00bc\u0001\u0000\u0000\u0000\u00ba\u00bb\u0005\n\u0000\u0000"+
		"\u00bb\u00bd\u0003\u001a\r\u0000\u00bc\u00ba\u0001\u0000\u0000\u0000\u00bc"+
		"\u00bd\u0001\u0000\u0000\u0000\u00bd\u00d1\u0001\u0000\u0000\u0000\u00be"+
		"\u00c1\u0003\u0016\u000b\u0000\u00bf\u00c1\u0005\"\u0000\u0000\u00c0\u00be"+
		"\u0001\u0000\u0000\u0000\u00c0\u00bf\u0001\u0000\u0000\u0000\u00c1\u00c4"+
		"\u0001\u0000\u0000\u0000\u00c2\u00c3\u0005\u000b\u0000\u0000\u00c3\u00c5"+
		"\u0003\u001a\r\u0000\u00c4\u00c2\u0001\u0000\u0000\u0000\u00c4\u00c5\u0001"+
		"\u0000\u0000\u0000\u00c5\u00d1\u0001\u0000\u0000\u0000\u00c6\u00c9\u0003"+
		"\u0016\u000b\u0000\u00c7\u00c9\u0005\"\u0000\u0000\u00c8\u00c6\u0001\u0000"+
		"\u0000\u0000\u00c8\u00c7\u0001\u0000\u0000\u0000\u00c9\u00ce\u0001\u0000"+
		"\u0000\u0000\u00ca\u00cb\u0005\n\u0000\u0000\u00cb\u00cc\u0005#\u0000"+
		"\u0000\u00cc\u00cd\u0005\f\u0000\u0000\u00cd\u00cf\u0003\u001a\r\u0000"+
		"\u00ce\u00ca\u0001\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000"+
		"\u00cf\u00d1\u0001\u0000\u0000\u0000\u00d0\u00b8\u0001\u0000\u0000\u0000"+
		"\u00d0\u00c0\u0001\u0000\u0000\u0000\u00d0\u00c8\u0001\u0000\u0000\u0000"+
		"\u00d1\u001b\u0001\u0000\u0000\u0000\u00d2\u00d3\u0003\u001e\u000f\u0000"+
		"\u00d3\u00d5\u0005\u0007\u0000\u0000\u00d4\u00d6\u0005\u0004\u0000\u0000"+
		"\u00d5\u00d4\u0001\u0000\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000"+
		"\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u00d8\u0005\"\u0000\u0000\u00d8"+
		"\u001d\u0001\u0000\u0000\u0000\u00d9\u00dc\u0005\"\u0000\u0000\u00da\u00db"+
		"\u0005\n\u0000\u0000\u00db\u00dd\u0003\u001e\u000f\u0000\u00dc\u00da\u0001"+
		"\u0000\u0000\u0000\u00dc\u00dd\u0001\u0000\u0000\u0000\u00dd\u001f\u0001"+
		"\u0000\u0000\u0000\u00de\u00df\u0005\r\u0000\u0000\u00df\u00e0\u0005\""+
		"\u0000\u0000\u00e0!\u0001\u0000\u0000\u0000\u00e1\u00e2\u0005\u000e\u0000"+
		"\u0000\u00e2\u00e4\u0003&\u0013\u0000\u00e3\u00e5\u0005\'\u0000\u0000"+
		"\u00e4\u00e3\u0001\u0000\u0000\u0000\u00e4\u00e5\u0001\u0000\u0000\u0000"+
		"\u00e5\u00e6\u0001\u0000\u0000\u0000\u00e6\u00e7\u0005\u000f\u0000\u0000"+
		"\u00e7\u00e9\u0003(\u0014\u0000\u00e8\u00ea\u0005\'\u0000\u0000\u00e9"+
		"\u00e8\u0001\u0000\u0000\u0000\u00e9\u00ea\u0001\u0000\u0000\u0000\u00ea"+
		"\u00eb\u0001\u0000\u0000\u0000\u00eb\u00fd\u0005\u0010\u0000\u0000\u00ec"+
		"\u00ee\u0005\'\u0000\u0000\u00ed\u00ec\u0001\u0000\u0000\u0000\u00ed\u00ee"+
		"\u0001\u0000\u0000\u0000\u00ee\u00ef\u0001\u0000\u0000\u0000\u00ef\u00f0"+
		"\u0005\u0011\u0000\u0000\u00f0\u00f2\u0003&\u0013\u0000\u00f1\u00f3\u0005"+
		"\'\u0000\u0000\u00f2\u00f1\u0001\u0000\u0000\u0000\u00f2\u00f3\u0001\u0000"+
		"\u0000\u0000\u00f3\u00f4\u0001\u0000\u0000\u0000\u00f4\u00f5\u0005\u000f"+
		"\u0000\u0000\u00f5\u00f7\u0003(\u0014\u0000\u00f6\u00f8\u0005\'\u0000"+
		"\u0000\u00f7\u00f6\u0001\u0000\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000"+
		"\u0000\u00f8\u00f9\u0001\u0000\u0000\u0000\u00f9\u00fa\u0005\u0010\u0000"+
		"\u0000\u00fa\u00fc\u0001\u0000\u0000\u0000\u00fb\u00ed\u0001\u0000\u0000"+
		"\u0000\u00fc\u00ff\u0001\u0000\u0000\u0000\u00fd\u00fb\u0001\u0000\u0000"+
		"\u0000\u00fd\u00fe\u0001\u0000\u0000\u0000\u00fe\u010e\u0001\u0000\u0000"+
		"\u0000\u00ff\u00fd\u0001\u0000\u0000\u0000\u0100\u0102\u0005\'\u0000\u0000"+
		"\u0101\u0100\u0001\u0000\u0000\u0000\u0101\u0102\u0001\u0000\u0000\u0000"+
		"\u0102\u0103\u0001\u0000\u0000\u0000\u0103\u0105\u0005\u0012\u0000\u0000"+
		"\u0104\u0106\u0005\'\u0000\u0000\u0105\u0104\u0001\u0000\u0000\u0000\u0105"+
		"\u0106\u0001\u0000\u0000\u0000\u0106\u0107\u0001\u0000\u0000\u0000\u0107"+
		"\u0108\u0005\u000f\u0000\u0000\u0108\u010a\u0003(\u0014\u0000\u0109\u010b"+
		"\u0005\'\u0000\u0000\u010a\u0109\u0001\u0000\u0000\u0000\u010a\u010b\u0001"+
		"\u0000\u0000\u0000\u010b\u010c\u0001\u0000\u0000\u0000\u010c\u010d\u0005"+
		"\u0010\u0000\u0000\u010d\u010f\u0001\u0000\u0000\u0000\u010e\u0101\u0001"+
		"\u0000\u0000\u0000\u010e\u010f\u0001\u0000\u0000\u0000\u010f#\u0001\u0000"+
		"\u0000\u0000\u0110\u0111\u0005\u0013\u0000\u0000\u0111\u0113\u0003&\u0013"+
		"\u0000\u0112\u0114\u0005\'\u0000\u0000\u0113\u0112\u0001\u0000\u0000\u0000"+
		"\u0113\u0114\u0001\u0000\u0000\u0000\u0114\u0115\u0001\u0000\u0000\u0000"+
		"\u0115\u0116\u0005\u000f\u0000\u0000\u0116\u0118\u0003(\u0014\u0000\u0117"+
		"\u0119\u0005\'\u0000\u0000\u0118\u0117\u0001\u0000\u0000\u0000\u0118\u0119"+
		"\u0001\u0000\u0000\u0000\u0119\u011a\u0001\u0000\u0000\u0000\u011a\u011b"+
		"\u0005\u0010\u0000\u0000\u011b%\u0001\u0000\u0000\u0000\u011c\u011d\u0003"+
		"\u0012\t\u0000\u011d\u011e\u0007\u0000\u0000\u0000\u011e\u011f\u0003\u0012"+
		"\t\u0000\u011f\'\u0001\u0000\u0000\u0000\u0120\u0125\u0003\u0002\u0001"+
		"\u0000\u0121\u0122\u0005\'\u0000\u0000\u0122\u0124\u0003\u0002\u0001\u0000"+
		"\u0123\u0121\u0001\u0000\u0000\u0000\u0124\u0127\u0001\u0000\u0000\u0000"+
		"\u0125\u0123\u0001\u0000\u0000\u0000\u0125\u0126\u0001\u0000\u0000\u0000"+
		"\u0126)\u0001\u0000\u0000\u0000\u0127\u0125\u0001\u0000\u0000\u0000\u0128"+
		"\u0129\u0005\u001a\u0000\u0000\u0129\u012a\u0005#\u0000\u0000\u012a\u012c"+
		"\u0005\u001b\u0000\u0000\u012b\u012d\u0005\'\u0000\u0000\u012c\u012b\u0001"+
		"\u0000\u0000\u0000\u012c\u012d\u0001\u0000\u0000\u0000\u012d\u012e\u0001"+
		"\u0000\u0000\u0000\u012e\u012f\u0003(\u0014\u0000\u012f+\u0001\u0000\u0000"+
		"\u0000\u0130\u0131\u0005\u001c\u0000\u0000\u0131\u0132\u0005\"\u0000\u0000"+
		"\u0132\u0136\u0005\u001d\u0000\u0000\u0133\u0135\u00030\u0018\u0000\u0134"+
		"\u0133\u0001\u0000\u0000\u0000\u0135\u0138\u0001\u0000\u0000\u0000\u0136"+
		"\u0134\u0001\u0000\u0000\u0000\u0136\u0137\u0001\u0000\u0000\u0000\u0137"+
		"\u0139\u0001\u0000\u0000\u0000\u0138\u0136\u0001\u0000\u0000\u0000\u0139"+
		"\u013a\u0005\u001e\u0000\u0000\u013a\u013b\u0005\u001f\u0000\u0000\u013b"+
		"\u013c\u00030\u0018\u0000\u013c\u013d\u0005\u000f\u0000\u0000\u013d\u013e"+
		"\u0003(\u0014\u0000\u013e\u0140\u0003.\u0017\u0000\u013f\u0141\u0005\'"+
		"\u0000\u0000\u0140\u013f\u0001\u0000\u0000\u0000\u0140\u0141\u0001\u0000"+
		"\u0000\u0000\u0141\u0142\u0001\u0000\u0000\u0000\u0142\u0143\u0005\u0010"+
		"\u0000\u0000\u0143-\u0001\u0000\u0000\u0000\u0144\u0147\u0005 \u0000\u0000"+
		"\u0145\u0148\u0005\"\u0000\u0000\u0146\u0148\u0003\u0012\t\u0000\u0147"+
		"\u0145\u0001\u0000\u0000\u0000\u0147\u0146\u0001\u0000\u0000\u0000\u0148"+
		"/\u0001\u0000\u0000\u0000\u0149\u014a\u0007\u0001\u0000\u0000\u014a1\u0001"+
		"\u0000\u0000\u0000,5<AFL[elry\u007f\u0086\u0094\u0099\u009e\u00a5\u00ac"+
		"\u00b2\u00b8\u00bc\u00c0\u00c4\u00c8\u00ce\u00d0\u00d5\u00dc\u00e4\u00e9"+
		"\u00ed\u00f2\u00f7\u00fd\u0101\u0105\u010a\u010e\u0113\u0118\u0125\u012c"+
		"\u0136\u0140\u0147";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}