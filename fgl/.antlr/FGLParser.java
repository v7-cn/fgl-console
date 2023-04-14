// Generated from /data/data1t/DSL/slht-fgl-lite/fgl/FGL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class FGLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		AS=18, LOAD=19, SAVE=20, INSERT=21, CREATE=22, DROP=23, REFRESH=24, SET=25, 
		CONNECT=26, DISCONNECT=27, TRAIN=28, PREDICT=29, REGISTER=30, UNREGISTER=31, 
		INCLUDE=32, OPTIONS=33, WHERE=34, PARTITIONBY=35, OVERWRITE=36, APPEND=37, 
		SHOW=38, ERRORIfExists=39, IGNORE=40, AND=41, OR=42, NOT=43, REPLACE=44, 
		DELETE=45, PARADIGM=46, JOB=47, DATAMODEL=48, PARADIGMS=49, JOBS=50, DATAMODELS=51, 
		BEGIN=52, END=53, CALL=54, RETURN=55, FORMAT=56, TYPING=57, NUMBER=58, 
		BOOLEAN=59, STRING_LITERAL=60, NEWLINE=61, WS=62, COMMENT=63, CLINE_COMMENT=64, 
		PLINE_COMMENT=65, SLINE_COMMENT=66, IDENTIFIER=67, IDENTIFIER_TEMPLATE=68;
	public static final int
		RULE_prog = 0, RULE_sqlStatement = 1, RULE_dqlStatement = 2, RULE_ddlStatement = 3, 
		RULE_dmlStatement = 4, RULE_load = 5, RULE_save = 6, RULE_connect = 7, 
		RULE_disconnect = 8, RULE_config = 9, RULE_create = 10, RULE_train = 11, 
		RULE_predict = 12, RULE_setArguments = 13, RULE_setArgument = 14, RULE_conditions = 15, 
		RULE_macro_key = 16, RULE_call = 17, RULE_ret = 18, RULE_module = 19, 
		RULE_checkOp = 20, RULE_conditionOp = 21, RULE_createParadigm = 22, RULE_createDatamodel = 23, 
		RULE_createJob = 24, RULE_showAlls = 25, RULE_showMacro = 26, RULE_show = 27, 
		RULE_deleteMacro = 28, RULE_delete = 29, RULE_begin_block = 30, RULE_block_content = 31, 
		RULE_argument_typing = 32, RULE_argument = 33, RULE_expr = 34, RULE_function = 35, 
		RULE_ender = 36, RULE_identifier = 37, RULE_parameter = 38, RULE_macro_name = 39, 
		RULE_json = 40, RULE_array = 41, RULE_constant = 42;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "sqlStatement", "dqlStatement", "ddlStatement", "dmlStatement", 
			"load", "save", "connect", "disconnect", "config", "create", "train", 
			"predict", "setArguments", "setArgument", "conditions", "macro_key", 
			"call", "ret", "module", "checkOp", "conditionOp", "createParadigm", 
			"createDatamodel", "createJob", "showAlls", "showMacro", "show", "deleteMacro", 
			"delete", "begin_block", "block_content", "argument_typing", "argument", 
			"expr", "function", "ender", "identifier", "parameter", "macro_name", 
			"json", "array", "constant"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "','", "'='", "'!='", "'=='", "'('", "')'", "'*'", "'/'", 
			"'+'", "'-'", "';'", "'{'", "':'", "'}'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "AS", "LOAD", "SAVE", "INSERT", "CREATE", 
			"DROP", "REFRESH", "SET", "CONNECT", "DISCONNECT", "TRAIN", "PREDICT", 
			"REGISTER", "UNREGISTER", "INCLUDE", "OPTIONS", "WHERE", "PARTITIONBY", 
			"OVERWRITE", "APPEND", "SHOW", "ERRORIfExists", "IGNORE", "AND", "OR", 
			"NOT", "REPLACE", "DELETE", "PARADIGM", "JOB", "DATAMODEL", "PARADIGMS", 
			"JOBS", "DATAMODELS", "BEGIN", "END", "CALL", "RETURN", "FORMAT", "TYPING", 
			"NUMBER", "BOOLEAN", "STRING_LITERAL", "NEWLINE", "WS", "COMMENT", "CLINE_COMMENT", 
			"PLINE_COMMENT", "SLINE_COMMENT", "IDENTIFIER", "IDENTIFIER_TEMPLATE"
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
	public String getGrammarFileName() { return "FGL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public FGLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(FGLParser.EOF, 0); }
		public List<SqlStatementContext> sqlStatement() {
			return getRuleContexts(SqlStatementContext.class);
		}
		public SqlStatementContext sqlStatement(int i) {
			return getRuleContext(SqlStatementContext.class,i);
		}
		public List<EnderContext> ender() {
			return getRuleContexts(EnderContext.class);
		}
		public EnderContext ender(int i) {
			return getRuleContext(EnderContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(86);
					sqlStatement();
					setState(88); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(87);
						ender();
						}
						}
						setState(90); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==T__11 );
					}
					} 
				}
				setState(96);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LOAD) | (1L << SAVE) | (1L << CREATE) | (1L << CONNECT) | (1L << DISCONNECT) | (1L << TRAIN) | (1L << PREDICT) | (1L << SHOW) | (1L << DELETE) | (1L << CALL) | (1L << RETURN))) != 0)) {
				{
				setState(97);
				sqlStatement();
				}
			}

			setState(100);
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

	public static class SqlStatementContext extends ParserRuleContext {
		public DdlStatementContext ddlStatement() {
			return getRuleContext(DdlStatementContext.class,0);
		}
		public DmlStatementContext dmlStatement() {
			return getRuleContext(DmlStatementContext.class,0);
		}
		public DqlStatementContext dqlStatement() {
			return getRuleContext(DqlStatementContext.class,0);
		}
		public SqlStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sqlStatement; }
	}

	public final SqlStatementContext sqlStatement() throws RecognitionException {
		SqlStatementContext _localctx = new SqlStatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sqlStatement);
		try {
			setState(105);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CREATE:
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				ddlStatement();
				}
				break;
			case LOAD:
			case SAVE:
			case CONNECT:
			case DISCONNECT:
			case TRAIN:
			case PREDICT:
			case DELETE:
			case CALL:
			case RETURN:
				enterOuterAlt(_localctx, 2);
				{
				setState(103);
				dmlStatement();
				}
				break;
			case SHOW:
				enterOuterAlt(_localctx, 3);
				{
				setState(104);
				dqlStatement();
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

	public static class DqlStatementContext extends ParserRuleContext {
		public ShowContext show() {
			return getRuleContext(ShowContext.class,0);
		}
		public ShowAllsContext showAlls() {
			return getRuleContext(ShowAllsContext.class,0);
		}
		public DqlStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dqlStatement; }
	}

	public final DqlStatementContext dqlStatement() throws RecognitionException {
		DqlStatementContext _localctx = new DqlStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_dqlStatement);
		try {
			setState(109);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(107);
				show();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(108);
				showAlls();
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

	public static class DdlStatementContext extends ParserRuleContext {
		public CreateContext create() {
			return getRuleContext(CreateContext.class,0);
		}
		public DdlStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ddlStatement; }
	}

	public final DdlStatementContext ddlStatement() throws RecognitionException {
		DdlStatementContext _localctx = new DdlStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ddlStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			create();
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

	public static class DmlStatementContext extends ParserRuleContext {
		public LoadContext load() {
			return getRuleContext(LoadContext.class,0);
		}
		public ConfigContext config() {
			return getRuleContext(ConfigContext.class,0);
		}
		public SaveContext save() {
			return getRuleContext(SaveContext.class,0);
		}
		public TrainContext train() {
			return getRuleContext(TrainContext.class,0);
		}
		public PredictContext predict() {
			return getRuleContext(PredictContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public RetContext ret() {
			return getRuleContext(RetContext.class,0);
		}
		public DeleteContext delete() {
			return getRuleContext(DeleteContext.class,0);
		}
		public DmlStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dmlStatement; }
	}

	public final DmlStatementContext dmlStatement() throws RecognitionException {
		DmlStatementContext _localctx = new DmlStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_dmlStatement);
		try {
			setState(121);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LOAD:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				load();
				}
				break;
			case CONNECT:
			case DISCONNECT:
				enterOuterAlt(_localctx, 2);
				{
				setState(114);
				config();
				}
				break;
			case SAVE:
				enterOuterAlt(_localctx, 3);
				{
				setState(115);
				save();
				}
				break;
			case TRAIN:
				enterOuterAlt(_localctx, 4);
				{
				setState(116);
				train();
				}
				break;
			case PREDICT:
				enterOuterAlt(_localctx, 5);
				{
				setState(117);
				predict();
				}
				break;
			case CALL:
				enterOuterAlt(_localctx, 6);
				{
				setState(118);
				call();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 7);
				{
				setState(119);
				ret();
				}
				break;
			case DELETE:
				enterOuterAlt(_localctx, 8);
				{
				setState(120);
				delete();
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

	public static class LoadContext extends ParserRuleContext {
		public TerminalNode LOAD() { return getToken(FGLParser.LOAD, 0); }
		public TerminalNode FORMAT() { return getToken(FGLParser.FORMAT, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(FGLParser.STRING_LITERAL, 0); }
		public SetArgumentsContext setArguments() {
			return getRuleContext(SetArgumentsContext.class,0);
		}
		public TerminalNode AS() { return getToken(FGLParser.AS, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public LoadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_load; }
	}

	public final LoadContext load() throws RecognitionException {
		LoadContext _localctx = new LoadContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_load);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(LOAD);
			setState(124);
			match(FORMAT);
			setState(125);
			match(T__0);
			setState(126);
			match(STRING_LITERAL);
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(127);
				setArguments();
				}
			}

			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(130);
				match(AS);
				setState(131);
				identifier();
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

	public static class SaveContext extends ParserRuleContext {
		public TerminalNode SAVE() { return getToken(FGLParser.SAVE, 0); }
		public TerminalNode FORMAT() { return getToken(FGLParser.FORMAT, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(FGLParser.STRING_LITERAL, 0); }
		public SetArgumentsContext setArguments() {
			return getRuleContext(SetArgumentsContext.class,0);
		}
		public TerminalNode AS() { return getToken(FGLParser.AS, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public SaveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_save; }
	}

	public final SaveContext save() throws RecognitionException {
		SaveContext _localctx = new SaveContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_save);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(SAVE);
			setState(135);
			match(FORMAT);
			setState(136);
			match(T__0);
			setState(137);
			match(STRING_LITERAL);
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(138);
				setArguments();
				}
			}

			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(141);
				match(AS);
				setState(142);
				identifier();
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

	public static class ConnectContext extends ParserRuleContext {
		public TerminalNode CONNECT() { return getToken(FGLParser.CONNECT, 0); }
		public TerminalNode FORMAT() { return getToken(FGLParser.FORMAT, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(FGLParser.STRING_LITERAL, 0); }
		public SetArgumentsContext setArguments() {
			return getRuleContext(SetArgumentsContext.class,0);
		}
		public TerminalNode AS() { return getToken(FGLParser.AS, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ConnectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_connect; }
	}

	public final ConnectContext connect() throws RecognitionException {
		ConnectContext _localctx = new ConnectContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_connect);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(CONNECT);
			setState(146);
			match(FORMAT);
			setState(147);
			match(T__0);
			setState(148);
			match(STRING_LITERAL);
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(149);
				setArguments();
				}
			}

			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(152);
				match(AS);
				setState(153);
				identifier();
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

	public static class DisconnectContext extends ParserRuleContext {
		public TerminalNode DISCONNECT() { return getToken(FGLParser.DISCONNECT, 0); }
		public TerminalNode FORMAT() { return getToken(FGLParser.FORMAT, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(FGLParser.STRING_LITERAL, 0); }
		public SetArgumentsContext setArguments() {
			return getRuleContext(SetArgumentsContext.class,0);
		}
		public TerminalNode AS() { return getToken(FGLParser.AS, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public DisconnectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_disconnect; }
	}

	public final DisconnectContext disconnect() throws RecognitionException {
		DisconnectContext _localctx = new DisconnectContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_disconnect);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(DISCONNECT);
			setState(157);
			match(FORMAT);
			setState(158);
			match(T__0);
			setState(159);
			match(STRING_LITERAL);
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(160);
				setArguments();
				}
			}

			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(163);
				match(AS);
				setState(164);
				identifier();
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

	public static class ConfigContext extends ParserRuleContext {
		public ConnectContext connect() {
			return getRuleContext(ConnectContext.class,0);
		}
		public DisconnectContext disconnect() {
			return getRuleContext(DisconnectContext.class,0);
		}
		public ConfigContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_config; }
	}

	public final ConfigContext config() throws RecognitionException {
		ConfigContext _localctx = new ConfigContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_config);
		try {
			setState(169);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CONNECT:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				connect();
				}
				break;
			case DISCONNECT:
				enterOuterAlt(_localctx, 2);
				{
				setState(168);
				disconnect();
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

	public static class CreateContext extends ParserRuleContext {
		public CreateParadigmContext createParadigm() {
			return getRuleContext(CreateParadigmContext.class,0);
		}
		public CreateDatamodelContext createDatamodel() {
			return getRuleContext(CreateDatamodelContext.class,0);
		}
		public CreateJobContext createJob() {
			return getRuleContext(CreateJobContext.class,0);
		}
		public CreateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_create; }
	}

	public final CreateContext create() throws RecognitionException {
		CreateContext _localctx = new CreateContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_create);
		try {
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				createParadigm();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(172);
				createDatamodel();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(173);
				createJob();
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

	public static class TrainContext extends ParserRuleContext {
		public TerminalNode TRAIN() { return getToken(FGLParser.TRAIN, 0); }
		public ModuleContext module() {
			return getRuleContext(ModuleContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode STRING_LITERAL() { return getToken(FGLParser.STRING_LITERAL, 0); }
		public SetArgumentsContext setArguments() {
			return getRuleContext(SetArgumentsContext.class,0);
		}
		public TerminalNode AS() { return getToken(FGLParser.AS, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TrainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_train; }
	}

	public final TrainContext train() throws RecognitionException {
		TrainContext _localctx = new TrainContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_train);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(TRAIN);
			setState(182);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(177);
					expr(0);
					setState(178);
					match(T__1);
					}
					} 
				}
				setState(184);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			setState(186);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(185);
				expr(0);
				}
				break;
			}
			setState(188);
			module();
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__0) {
				{
				setState(189);
				match(T__0);
				setState(190);
				match(STRING_LITERAL);
				}
			}

			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(193);
				setArguments();
				}
			}

			setState(208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(196);
				match(AS);
				setState(202);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(197);
						identifier();
						setState(198);
						match(T__1);
						}
						} 
					}
					setState(204);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
				}
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 56)) & ~0x3f) == 0 && ((1L << (_la - 56)) & ((1L << (FORMAT - 56)) | (1L << (IDENTIFIER - 56)) | (1L << (IDENTIFIER_TEMPLATE - 56)))) != 0)) {
					{
					setState(205);
					identifier();
					}
				}

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

	public static class PredictContext extends ParserRuleContext {
		public TerminalNode PREDICT() { return getToken(FGLParser.PREDICT, 0); }
		public ModuleContext module() {
			return getRuleContext(ModuleContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode STRING_LITERAL() { return getToken(FGLParser.STRING_LITERAL, 0); }
		public SetArgumentsContext setArguments() {
			return getRuleContext(SetArgumentsContext.class,0);
		}
		public TerminalNode AS() { return getToken(FGLParser.AS, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public PredictContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predict; }
	}

	public final PredictContext predict() throws RecognitionException {
		PredictContext _localctx = new PredictContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_predict);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			match(PREDICT);
			setState(216);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(211);
					expr(0);
					setState(212);
					match(T__1);
					}
					} 
				}
				setState(218);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(219);
				expr(0);
				}
				break;
			}
			setState(222);
			module();
			setState(223);
			match(T__0);
			setState(225);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STRING_LITERAL) {
				{
				setState(224);
				match(STRING_LITERAL);
				}
			}

			setState(228);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(227);
				setArguments();
				}
			}

			setState(242);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(230);
				match(AS);
				setState(236);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(231);
						identifier();
						setState(232);
						match(T__1);
						}
						} 
					}
					setState(238);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
				}
				setState(240);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 56)) & ~0x3f) == 0 && ((1L << (_la - 56)) & ((1L << (FORMAT - 56)) | (1L << (IDENTIFIER - 56)) | (1L << (IDENTIFIER_TEMPLATE - 56)))) != 0)) {
					{
					setState(239);
					identifier();
					}
				}

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

	public static class SetArgumentsContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(FGLParser.WHERE, 0); }
		public List<SetArgumentContext> setArgument() {
			return getRuleContexts(SetArgumentContext.class);
		}
		public SetArgumentContext setArgument(int i) {
			return getRuleContext(SetArgumentContext.class,i);
		}
		public SetArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setArguments; }
	}

	public final SetArgumentsContext setArguments() throws RecognitionException {
		SetArgumentsContext _localctx = new SetArgumentsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_setArguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			match(WHERE);
			setState(248);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 56)) & ~0x3f) == 0 && ((1L << (_la - 56)) & ((1L << (FORMAT - 56)) | (1L << (IDENTIFIER - 56)) | (1L << (IDENTIFIER_TEMPLATE - 56)))) != 0)) {
				{
				{
				setState(245);
				setArgument();
				}
				}
				setState(250);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class SetArgumentContext extends ParserRuleContext {
		public ParameterContext parameter() {
			return getRuleContext(ParameterContext.class,0);
		}
		public CheckOpContext checkOp() {
			return getRuleContext(CheckOpContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode AND() { return getToken(FGLParser.AND, 0); }
		public SetArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setArgument; }
	}

	public final SetArgumentContext setArgument() throws RecognitionException {
		SetArgumentContext _localctx = new SetArgumentContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_setArgument);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(251);
			parameter();
			setState(252);
			checkOp();
			setState(253);
			expr(0);
			setState(255);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AND) {
				{
				setState(254);
				match(AND);
				}
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

	public static class ConditionsContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(FGLParser.WHERE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<CheckOpContext> checkOp() {
			return getRuleContexts(CheckOpContext.class);
		}
		public CheckOpContext checkOp(int i) {
			return getRuleContext(CheckOpContext.class,i);
		}
		public List<ConditionOpContext> conditionOp() {
			return getRuleContexts(ConditionOpContext.class);
		}
		public ConditionOpContext conditionOp(int i) {
			return getRuleContext(ConditionOpContext.class,i);
		}
		public ConditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditions; }
	}

	public final ConditionsContext conditions() throws RecognitionException {
		ConditionsContext _localctx = new ConditionsContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_conditions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(WHERE);
			setState(266);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 6)) & ~0x3f) == 0 && ((1L << (_la - 6)) & ((1L << (T__5 - 6)) | (1L << (T__12 - 6)) | (1L << (T__15 - 6)) | (1L << (FORMAT - 6)) | (1L << (NUMBER - 6)) | (1L << (BOOLEAN - 6)) | (1L << (STRING_LITERAL - 6)) | (1L << (IDENTIFIER - 6)) | (1L << (IDENTIFIER_TEMPLATE - 6)))) != 0)) {
				{
				{
				setState(258);
				expr(0);
				setState(259);
				checkOp();
				setState(260);
				expr(0);
				setState(262);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AND || _la==OR) {
					{
					setState(261);
					conditionOp();
					}
				}

				}
				}
				setState(268);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class Macro_keyContext extends ParserRuleContext {
		public TerminalNode PARADIGM() { return getToken(FGLParser.PARADIGM, 0); }
		public TerminalNode DATAMODEL() { return getToken(FGLParser.DATAMODEL, 0); }
		public TerminalNode JOB() { return getToken(FGLParser.JOB, 0); }
		public Macro_keyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_key; }
	}

	public final Macro_keyContext macro_key() throws RecognitionException {
		Macro_keyContext _localctx = new Macro_keyContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_macro_key);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(269);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PARADIGM) | (1L << JOB) | (1L << DATAMODEL))) != 0)) ) {
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

	public static class CallContext extends ParserRuleContext {
		public TerminalNode CALL() { return getToken(FGLParser.CALL, 0); }
		public Macro_nameContext macro_name() {
			return getRuleContext(Macro_nameContext.class,0);
		}
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public Macro_keyContext macro_key() {
			return getRuleContext(Macro_keyContext.class,0);
		}
		public TerminalNode AS() { return getToken(FGLParser.AS, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			match(CALL);
			setState(273);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PARADIGM) | (1L << JOB) | (1L << DATAMODEL))) != 0)) {
				{
				setState(272);
				macro_key();
				}
			}

			setState(275);
			macro_name();
			setState(276);
			argument();
			setState(279);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(277);
				match(AS);
				setState(278);
				identifier();
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

	public static class RetContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(FGLParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public RetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ret; }
	}

	public final RetContext ret() throws RecognitionException {
		RetContext _localctx = new RetContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_ret);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			match(RETURN);
			setState(282);
			expr(0);
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

	public static class ModuleContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(FGLParser.IDENTIFIER, 0); }
		public ModuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_module; }
	}

	public final ModuleContext module() throws RecognitionException {
		ModuleContext _localctx = new ModuleContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_module);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(IDENTIFIER);
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

	public static class CheckOpContext extends ParserRuleContext {
		public CheckOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_checkOp; }
	}

	public final CheckOpContext checkOp() throws RecognitionException {
		CheckOpContext _localctx = new CheckOpContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_checkOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__3) | (1L << T__4))) != 0)) ) {
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

	public static class ConditionOpContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(FGLParser.AND, 0); }
		public TerminalNode OR() { return getToken(FGLParser.OR, 0); }
		public ConditionOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditionOp; }
	}

	public final ConditionOpContext conditionOp() throws RecognitionException {
		ConditionOpContext _localctx = new ConditionOpContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_conditionOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
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

	public static class CreateParadigmContext extends ParserRuleContext {
		public TerminalNode CREATE() { return getToken(FGLParser.CREATE, 0); }
		public TerminalNode PARADIGM() { return getToken(FGLParser.PARADIGM, 0); }
		public TerminalNode IDENTIFIER() { return getToken(FGLParser.IDENTIFIER, 0); }
		public Argument_typingContext argument_typing() {
			return getRuleContext(Argument_typingContext.class,0);
		}
		public Begin_blockContext begin_block() {
			return getRuleContext(Begin_blockContext.class,0);
		}
		public TerminalNode OR() { return getToken(FGLParser.OR, 0); }
		public TerminalNode REPLACE() { return getToken(FGLParser.REPLACE, 0); }
		public CreateParadigmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createParadigm; }
	}

	public final CreateParadigmContext createParadigm() throws RecognitionException {
		CreateParadigmContext _localctx = new CreateParadigmContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_createParadigm);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			match(CREATE);
			setState(293);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OR) {
				{
				setState(291);
				match(OR);
				setState(292);
				match(REPLACE);
				}
			}

			setState(295);
			match(PARADIGM);
			setState(296);
			match(IDENTIFIER);
			setState(297);
			argument_typing();
			setState(298);
			begin_block();
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

	public static class CreateDatamodelContext extends ParserRuleContext {
		public TerminalNode CREATE() { return getToken(FGLParser.CREATE, 0); }
		public TerminalNode DATAMODEL() { return getToken(FGLParser.DATAMODEL, 0); }
		public TerminalNode IDENTIFIER() { return getToken(FGLParser.IDENTIFIER, 0); }
		public Argument_typingContext argument_typing() {
			return getRuleContext(Argument_typingContext.class,0);
		}
		public Begin_blockContext begin_block() {
			return getRuleContext(Begin_blockContext.class,0);
		}
		public TerminalNode OR() { return getToken(FGLParser.OR, 0); }
		public TerminalNode REPLACE() { return getToken(FGLParser.REPLACE, 0); }
		public CreateDatamodelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createDatamodel; }
	}

	public final CreateDatamodelContext createDatamodel() throws RecognitionException {
		CreateDatamodelContext _localctx = new CreateDatamodelContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_createDatamodel);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			match(CREATE);
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OR) {
				{
				setState(301);
				match(OR);
				setState(302);
				match(REPLACE);
				}
			}

			setState(305);
			match(DATAMODEL);
			setState(306);
			match(IDENTIFIER);
			setState(307);
			argument_typing();
			setState(308);
			begin_block();
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

	public static class CreateJobContext extends ParserRuleContext {
		public TerminalNode CREATE() { return getToken(FGLParser.CREATE, 0); }
		public TerminalNode JOB() { return getToken(FGLParser.JOB, 0); }
		public TerminalNode IDENTIFIER() { return getToken(FGLParser.IDENTIFIER, 0); }
		public Begin_blockContext begin_block() {
			return getRuleContext(Begin_blockContext.class,0);
		}
		public TerminalNode OR() { return getToken(FGLParser.OR, 0); }
		public TerminalNode REPLACE() { return getToken(FGLParser.REPLACE, 0); }
		public SetArgumentsContext setArguments() {
			return getRuleContext(SetArgumentsContext.class,0);
		}
		public CreateJobContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createJob; }
	}

	public final CreateJobContext createJob() throws RecognitionException {
		CreateJobContext _localctx = new CreateJobContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_createJob);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
			match(CREATE);
			setState(313);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OR) {
				{
				setState(311);
				match(OR);
				setState(312);
				match(REPLACE);
				}
			}

			setState(315);
			match(JOB);
			setState(316);
			match(IDENTIFIER);
			setState(317);
			begin_block();
			setState(319);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(318);
				setArguments();
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

	public static class ShowAllsContext extends ParserRuleContext {
		public TerminalNode SHOW() { return getToken(FGLParser.SHOW, 0); }
		public TerminalNode PARADIGMS() { return getToken(FGLParser.PARADIGMS, 0); }
		public TerminalNode JOBS() { return getToken(FGLParser.JOBS, 0); }
		public TerminalNode DATAMODELS() { return getToken(FGLParser.DATAMODELS, 0); }
		public ShowAllsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_showAlls; }
	}

	public final ShowAllsContext showAlls() throws RecognitionException {
		ShowAllsContext _localctx = new ShowAllsContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_showAlls);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(321);
			match(SHOW);
			setState(322);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PARADIGMS) | (1L << JOBS) | (1L << DATAMODELS))) != 0)) ) {
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

	public static class ShowMacroContext extends ParserRuleContext {
		public TerminalNode SHOW() { return getToken(FGLParser.SHOW, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode PARADIGM() { return getToken(FGLParser.PARADIGM, 0); }
		public TerminalNode JOB() { return getToken(FGLParser.JOB, 0); }
		public TerminalNode DATAMODEL() { return getToken(FGLParser.DATAMODEL, 0); }
		public ShowMacroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_showMacro; }
	}

	public final ShowMacroContext showMacro() throws RecognitionException {
		ShowMacroContext _localctx = new ShowMacroContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_showMacro);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
			match(SHOW);
			setState(325);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PARADIGM) | (1L << JOB) | (1L << DATAMODEL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(326);
			identifier();
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

	public static class ShowContext extends ParserRuleContext {
		public ShowMacroContext showMacro() {
			return getRuleContext(ShowMacroContext.class,0);
		}
		public ShowContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_show; }
	}

	public final ShowContext show() throws RecognitionException {
		ShowContext _localctx = new ShowContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_show);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(328);
			showMacro();
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

	public static class DeleteMacroContext extends ParserRuleContext {
		public TerminalNode DELETE() { return getToken(FGLParser.DELETE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode PARADIGM() { return getToken(FGLParser.PARADIGM, 0); }
		public TerminalNode JOB() { return getToken(FGLParser.JOB, 0); }
		public TerminalNode DATAMODEL() { return getToken(FGLParser.DATAMODEL, 0); }
		public DeleteMacroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_deleteMacro; }
	}

	public final DeleteMacroContext deleteMacro() throws RecognitionException {
		DeleteMacroContext _localctx = new DeleteMacroContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_deleteMacro);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(330);
			match(DELETE);
			setState(331);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PARADIGM) | (1L << JOB) | (1L << DATAMODEL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(332);
			identifier();
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

	public static class DeleteContext extends ParserRuleContext {
		public DeleteMacroContext deleteMacro() {
			return getRuleContext(DeleteMacroContext.class,0);
		}
		public DeleteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delete; }
	}

	public final DeleteContext delete() throws RecognitionException {
		DeleteContext _localctx = new DeleteContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_delete);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			deleteMacro();
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

	public static class Begin_blockContext extends ParserRuleContext {
		public TerminalNode BEGIN() { return getToken(FGLParser.BEGIN, 0); }
		public Block_contentContext block_content() {
			return getRuleContext(Block_contentContext.class,0);
		}
		public TerminalNode END() { return getToken(FGLParser.END, 0); }
		public Begin_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_begin_block; }
	}

	public final Begin_blockContext begin_block() throws RecognitionException {
		Begin_blockContext _localctx = new Begin_blockContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_begin_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			match(BEGIN);
			setState(337);
			block_content();
			setState(338);
			match(END);
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

	public static class Block_contentContext extends ParserRuleContext {
		public Block_contentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_content; }
	}

	public final Block_contentContext block_content() throws RecognitionException {
		Block_contentContext _localctx = new Block_contentContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_block_content);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(343);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(340);
					matchWildcard();
					}
					} 
				}
				setState(345);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
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

	public static class Argument_typingContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> TYPING() { return getTokens(FGLParser.TYPING); }
		public TerminalNode TYPING(int i) {
			return getToken(FGLParser.TYPING, i);
		}
		public Argument_typingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument_typing; }
	}

	public final Argument_typingContext argument_typing() throws RecognitionException {
		Argument_typingContext _localctx = new Argument_typingContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_argument_typing);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(346);
			match(T__5);
			setState(354);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 6)) & ~0x3f) == 0 && ((1L << (_la - 6)) & ((1L << (T__5 - 6)) | (1L << (T__12 - 6)) | (1L << (T__15 - 6)) | (1L << (FORMAT - 6)) | (1L << (NUMBER - 6)) | (1L << (BOOLEAN - 6)) | (1L << (STRING_LITERAL - 6)) | (1L << (IDENTIFIER - 6)) | (1L << (IDENTIFIER_TEMPLATE - 6)))) != 0)) {
				{
				{
				setState(347);
				expr(0);
				setState(348);
				match(TYPING);
				setState(350);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(349);
					match(T__1);
					}
				}

				}
				}
				setState(356);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(357);
			match(T__6);
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

	public static class ArgumentContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_argument);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(359);
			match(T__5);
			setState(366);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 6)) & ~0x3f) == 0 && ((1L << (_la - 6)) & ((1L << (T__5 - 6)) | (1L << (T__12 - 6)) | (1L << (T__15 - 6)) | (1L << (FORMAT - 6)) | (1L << (NUMBER - 6)) | (1L << (BOOLEAN - 6)) | (1L << (STRING_LITERAL - 6)) | (1L << (IDENTIFIER - 6)) | (1L << (IDENTIFIER_TEMPLATE - 6)))) != 0)) {
				{
				{
				setState(360);
				expr(0);
				setState(362);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(361);
					match(T__1);
					}
				}

				}
				}
				setState(368);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(369);
			match(T__6);
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

	public static class ExprContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 68;
		enterRecursionRule(_localctx, 68, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(379);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				{
				setState(372);
				identifier();
				}
				break;
			case 2:
				{
				setState(373);
				constant();
				}
				break;
			case 3:
				{
				setState(374);
				function();
				}
				break;
			case 4:
				{
				setState(375);
				match(T__5);
				setState(376);
				expr(0);
				setState(377);
				match(T__6);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(389);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,47,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(387);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(381);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(382);
						_la = _input.LA(1);
						if ( !(_la==T__7 || _la==T__8) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(383);
						expr(7);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(384);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(385);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__10) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(386);
						expr(6);
						}
						break;
					}
					} 
				}
				setState(391);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,47,_ctx);
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

	public static class FunctionContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(392);
			identifier();
			setState(393);
			argument();
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

	public static class EnderContext extends ParserRuleContext {
		public EnderContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ender; }
	}

	public final EnderContext ender() throws RecognitionException {
		EnderContext _localctx = new EnderContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_ender);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(395);
			match(T__11);
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

	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER_TEMPLATE() { return getToken(FGLParser.IDENTIFIER_TEMPLATE, 0); }
		public TerminalNode IDENTIFIER() { return getToken(FGLParser.IDENTIFIER, 0); }
		public TerminalNode FORMAT() { return getToken(FGLParser.FORMAT, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_identifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			_la = _input.LA(1);
			if ( !(((((_la - 56)) & ~0x3f) == 0 && ((1L << (_la - 56)) & ((1L << (FORMAT - 56)) | (1L << (IDENTIFIER - 56)) | (1L << (IDENTIFIER_TEMPLATE - 56)))) != 0)) ) {
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

	public static class ParameterContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER_TEMPLATE() { return getToken(FGLParser.IDENTIFIER_TEMPLATE, 0); }
		public TerminalNode IDENTIFIER() { return getToken(FGLParser.IDENTIFIER, 0); }
		public TerminalNode FORMAT() { return getToken(FGLParser.FORMAT, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(399);
			_la = _input.LA(1);
			if ( !(((((_la - 56)) & ~0x3f) == 0 && ((1L << (_la - 56)) & ((1L << (FORMAT - 56)) | (1L << (IDENTIFIER - 56)) | (1L << (IDENTIFIER_TEMPLATE - 56)))) != 0)) ) {
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

	public static class Macro_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(FGLParser.IDENTIFIER, 0); }
		public TerminalNode FORMAT() { return getToken(FGLParser.FORMAT, 0); }
		public Macro_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macro_name; }
	}

	public final Macro_nameContext macro_name() throws RecognitionException {
		Macro_nameContext _localctx = new Macro_nameContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_macro_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(401);
			_la = _input.LA(1);
			if ( !(_la==FORMAT || _la==IDENTIFIER) ) {
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

	public static class JsonContext extends ParserRuleContext {
		public List<TerminalNode> STRING_LITERAL() { return getTokens(FGLParser.STRING_LITERAL); }
		public TerminalNode STRING_LITERAL(int i) {
			return getToken(FGLParser.STRING_LITERAL, i);
		}
		public List<ConstantContext> constant() {
			return getRuleContexts(ConstantContext.class);
		}
		public ConstantContext constant(int i) {
			return getRuleContext(ConstantContext.class,i);
		}
		public JsonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_json; }
	}

	public final JsonContext json() throws RecognitionException {
		JsonContext _localctx = new JsonContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_json);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(403);
			match(T__12);
			setState(411);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,48,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(404);
					match(STRING_LITERAL);
					setState(405);
					match(T__13);
					setState(406);
					constant();
					setState(407);
					match(T__1);
					}
					} 
				}
				setState(413);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,48,_ctx);
			}
			setState(417);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STRING_LITERAL) {
				{
				setState(414);
				match(STRING_LITERAL);
				setState(415);
				match(T__13);
				setState(416);
				constant();
				}
			}

			setState(419);
			match(T__14);
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

	public static class ArrayContext extends ParserRuleContext {
		public List<ConstantContext> constant() {
			return getRuleContexts(ConstantContext.class);
		}
		public ConstantContext constant(int i) {
			return getRuleContext(ConstantContext.class,i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_array);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(421);
			match(T__15);
			setState(427);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,50,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(422);
					constant();
					setState(423);
					match(T__1);
					}
					} 
				}
				setState(429);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,50,_ctx);
			}
			setState(431);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__15) | (1L << NUMBER) | (1L << BOOLEAN) | (1L << STRING_LITERAL))) != 0)) {
				{
				setState(430);
				constant();
				}
			}

			setState(433);
			match(T__16);
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

	public static class ConstantContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(FGLParser.NUMBER, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(FGLParser.STRING_LITERAL, 0); }
		public TerminalNode BOOLEAN() { return getToken(FGLParser.BOOLEAN, 0); }
		public JsonContext json() {
			return getRuleContext(JsonContext.class,0);
		}
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public ConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant; }
	}

	public final ConstantContext constant() throws RecognitionException {
		ConstantContext _localctx = new ConstantContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_constant);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(440);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				{
				setState(435);
				match(NUMBER);
				}
				break;
			case STRING_LITERAL:
				{
				setState(436);
				match(STRING_LITERAL);
				}
				break;
			case BOOLEAN:
				{
				setState(437);
				match(BOOLEAN);
				}
				break;
			case T__12:
				{
				setState(438);
				json();
				}
				break;
			case T__15:
				{
				setState(439);
				array();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		case 34:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F\u01bd\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\3\2\3\2\6\2[\n\2\r\2\16\2\\\7\2_\n\2\f\2\16\2b\13\2\3\2\5\2e\n\2"+
		"\3\2\3\2\3\3\3\3\3\3\5\3l\n\3\3\4\3\4\5\4p\n\4\3\5\3\5\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\5\6|\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u0083\n\7\3\7\3\7\5"+
		"\7\u0087\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u008e\n\b\3\b\3\b\5\b\u0092\n\b\3"+
		"\t\3\t\3\t\3\t\3\t\5\t\u0099\n\t\3\t\3\t\5\t\u009d\n\t\3\n\3\n\3\n\3\n"+
		"\3\n\5\n\u00a4\n\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\5\13\u00ac\n\13\3\f"+
		"\3\f\3\f\5\f\u00b1\n\f\3\r\3\r\3\r\3\r\7\r\u00b7\n\r\f\r\16\r\u00ba\13"+
		"\r\3\r\5\r\u00bd\n\r\3\r\3\r\3\r\5\r\u00c2\n\r\3\r\5\r\u00c5\n\r\3\r\3"+
		"\r\3\r\3\r\7\r\u00cb\n\r\f\r\16\r\u00ce\13\r\3\r\5\r\u00d1\n\r\5\r\u00d3"+
		"\n\r\3\16\3\16\3\16\3\16\7\16\u00d9\n\16\f\16\16\16\u00dc\13\16\3\16\5"+
		"\16\u00df\n\16\3\16\3\16\3\16\5\16\u00e4\n\16\3\16\5\16\u00e7\n\16\3\16"+
		"\3\16\3\16\3\16\7\16\u00ed\n\16\f\16\16\16\u00f0\13\16\3\16\5\16\u00f3"+
		"\n\16\5\16\u00f5\n\16\3\17\3\17\7\17\u00f9\n\17\f\17\16\17\u00fc\13\17"+
		"\3\20\3\20\3\20\3\20\5\20\u0102\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u0109"+
		"\n\21\7\21\u010b\n\21\f\21\16\21\u010e\13\21\3\22\3\22\3\23\3\23\5\23"+
		"\u0114\n\23\3\23\3\23\3\23\3\23\5\23\u011a\n\23\3\24\3\24\3\24\3\25\3"+
		"\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\5\30\u0128\n\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\31\3\31\3\31\5\31\u0132\n\31\3\31\3\31\3\31\3\31\3\31\3\32"+
		"\3\32\3\32\5\32\u013c\n\32\3\32\3\32\3\32\3\32\5\32\u0142\n\32\3\33\3"+
		"\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3"+
		" \3 \3 \3 \3!\7!\u0158\n!\f!\16!\u015b\13!\3\"\3\"\3\"\3\"\5\"\u0161\n"+
		"\"\7\"\u0163\n\"\f\"\16\"\u0166\13\"\3\"\3\"\3#\3#\3#\5#\u016d\n#\7#\u016f"+
		"\n#\f#\16#\u0172\13#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\5$\u017e\n$\3$\3$\3"+
		"$\3$\3$\3$\7$\u0186\n$\f$\16$\u0189\13$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3"+
		")\3)\3*\3*\3*\3*\3*\3*\7*\u019c\n*\f*\16*\u019f\13*\3*\3*\3*\5*\u01a4"+
		"\n*\3*\3*\3+\3+\3+\3+\7+\u01ac\n+\f+\16+\u01af\13+\3+\5+\u01b2\n+\3+\3"+
		"+\3,\3,\3,\3,\3,\5,\u01bb\n,\3,\3\u0159\3F-\2\4\6\b\n\f\16\20\22\24\26"+
		"\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\n\3\2\60\62\3\2\5"+
		"\7\3\2+,\3\2\63\65\3\2\n\13\3\2\f\r\4\2::EF\4\2::EE\2\u01d3\2`\3\2\2\2"+
		"\4k\3\2\2\2\6o\3\2\2\2\bq\3\2\2\2\n{\3\2\2\2\f}\3\2\2\2\16\u0088\3\2\2"+
		"\2\20\u0093\3\2\2\2\22\u009e\3\2\2\2\24\u00ab\3\2\2\2\26\u00b0\3\2\2\2"+
		"\30\u00b2\3\2\2\2\32\u00d4\3\2\2\2\34\u00f6\3\2\2\2\36\u00fd\3\2\2\2 "+
		"\u0103\3\2\2\2\"\u010f\3\2\2\2$\u0111\3\2\2\2&\u011b\3\2\2\2(\u011e\3"+
		"\2\2\2*\u0120\3\2\2\2,\u0122\3\2\2\2.\u0124\3\2\2\2\60\u012e\3\2\2\2\62"+
		"\u0138\3\2\2\2\64\u0143\3\2\2\2\66\u0146\3\2\2\28\u014a\3\2\2\2:\u014c"+
		"\3\2\2\2<\u0150\3\2\2\2>\u0152\3\2\2\2@\u0159\3\2\2\2B\u015c\3\2\2\2D"+
		"\u0169\3\2\2\2F\u017d\3\2\2\2H\u018a\3\2\2\2J\u018d\3\2\2\2L\u018f\3\2"+
		"\2\2N\u0191\3\2\2\2P\u0193\3\2\2\2R\u0195\3\2\2\2T\u01a7\3\2\2\2V\u01ba"+
		"\3\2\2\2XZ\5\4\3\2Y[\5J&\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2"+
		"]_\3\2\2\2^X\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ad\3\2\2\2b`\3\2\2\2"+
		"ce\5\4\3\2dc\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\7\2\2\3g\3\3\2\2\2hl\5\b\5"+
		"\2il\5\n\6\2jl\5\6\4\2kh\3\2\2\2ki\3\2\2\2kj\3\2\2\2l\5\3\2\2\2mp\58\35"+
		"\2np\5\64\33\2om\3\2\2\2on\3\2\2\2p\7\3\2\2\2qr\5\26\f\2r\t\3\2\2\2s|"+
		"\5\f\7\2t|\5\24\13\2u|\5\16\b\2v|\5\30\r\2w|\5\32\16\2x|\5$\23\2y|\5&"+
		"\24\2z|\5<\37\2{s\3\2\2\2{t\3\2\2\2{u\3\2\2\2{v\3\2\2\2{w\3\2\2\2{x\3"+
		"\2\2\2{y\3\2\2\2{z\3\2\2\2|\13\3\2\2\2}~\7\25\2\2~\177\7:\2\2\177\u0080"+
		"\7\3\2\2\u0080\u0082\7>\2\2\u0081\u0083\5\34\17\2\u0082\u0081\3\2\2\2"+
		"\u0082\u0083\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0085\7\24\2\2\u0085\u0087"+
		"\5L\'\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\r\3\2\2\2\u0088"+
		"\u0089\7\26\2\2\u0089\u008a\7:\2\2\u008a\u008b\7\3\2\2\u008b\u008d\7>"+
		"\2\2\u008c\u008e\5\34\17\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e"+
		"\u0091\3\2\2\2\u008f\u0090\7\24\2\2\u0090\u0092\5L\'\2\u0091\u008f\3\2"+
		"\2\2\u0091\u0092\3\2\2\2\u0092\17\3\2\2\2\u0093\u0094\7\34\2\2\u0094\u0095"+
		"\7:\2\2\u0095\u0096\7\3\2\2\u0096\u0098\7>\2\2\u0097\u0099\5\34\17\2\u0098"+
		"\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u009b\7\24"+
		"\2\2\u009b\u009d\5L\'\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d"+
		"\21\3\2\2\2\u009e\u009f\7\35\2\2\u009f\u00a0\7:\2\2\u00a0\u00a1\7\3\2"+
		"\2\u00a1\u00a3\7>\2\2\u00a2\u00a4\5\34\17\2\u00a3\u00a2\3\2\2\2\u00a3"+
		"\u00a4\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a6\7\24\2\2\u00a6\u00a8\5"+
		"L\'\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\23\3\2\2\2\u00a9\u00ac"+
		"\5\20\t\2\u00aa\u00ac\5\22\n\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2"+
		"\u00ac\25\3\2\2\2\u00ad\u00b1\5.\30\2\u00ae\u00b1\5\60\31\2\u00af\u00b1"+
		"\5\62\32\2\u00b0\u00ad\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2"+
		"\u00b1\27\3\2\2\2\u00b2\u00b8\7\36\2\2\u00b3\u00b4\5F$\2\u00b4\u00b5\7"+
		"\4\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8"+
		"\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2"+
		"\2\2\u00bb\u00bd\5F$\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be"+
		"\3\2\2\2\u00be\u00c1\5(\25\2\u00bf\u00c0\7\3\2\2\u00c0\u00c2\7>\2\2\u00c1"+
		"\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c5\5\34"+
		"\17\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00d2\3\2\2\2\u00c6"+
		"\u00cc\7\24\2\2\u00c7\u00c8\5L\'\2\u00c8\u00c9\7\4\2\2\u00c9\u00cb\3\2"+
		"\2\2\u00ca\u00c7\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc"+
		"\u00cd\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1\5L"+
		"\'\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\3\2\2\2\u00d2"+
		"\u00c6\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\31\3\2\2\2\u00d4\u00da\7\37\2"+
		"\2\u00d5\u00d6\5F$\2\u00d6\u00d7\7\4\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d5"+
		"\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db"+
		"\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00df\5F$\2\u00de\u00dd\3\2\2"+
		"\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\5(\25\2\u00e1\u00e3"+
		"\7\3\2\2\u00e2\u00e4\7>\2\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4"+
		"\u00e6\3\2\2\2\u00e5\u00e7\5\34\17\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3"+
		"\2\2\2\u00e7\u00f4\3\2\2\2\u00e8\u00ee\7\24\2\2\u00e9\u00ea\5L\'\2\u00ea"+
		"\u00eb\7\4\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ed\u00f0\3\2"+
		"\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0"+
		"\u00ee\3\2\2\2\u00f1\u00f3\5L\'\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2"+
		"\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00e8\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5"+
		"\33\3\2\2\2\u00f6\u00fa\7$\2\2\u00f7\u00f9\5\36\20\2\u00f8\u00f7\3\2\2"+
		"\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\35"+
		"\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\5N(\2\u00fe\u00ff\5*\26\2\u00ff"+
		"\u0101\5F$\2\u0100\u0102\7+\2\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2"+
		"\2\u0102\37\3\2\2\2\u0103\u010c\7$\2\2\u0104\u0105\5F$\2\u0105\u0106\5"+
		"*\26\2\u0106\u0108\5F$\2\u0107\u0109\5,\27\2\u0108\u0107\3\2\2\2\u0108"+
		"\u0109\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0104\3\2\2\2\u010b\u010e\3\2"+
		"\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d!\3\2\2\2\u010e\u010c"+
		"\3\2\2\2\u010f\u0110\t\2\2\2\u0110#\3\2\2\2\u0111\u0113\78\2\2\u0112\u0114"+
		"\5\"\22\2\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\3\2\2\2"+
		"\u0115\u0116\5P)\2\u0116\u0119\5D#\2\u0117\u0118\7\24\2\2\u0118\u011a"+
		"\5L\'\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a%\3\2\2\2\u011b\u011c"+
		"\79\2\2\u011c\u011d\5F$\2\u011d\'\3\2\2\2\u011e\u011f\7E\2\2\u011f)\3"+
		"\2\2\2\u0120\u0121\t\3\2\2\u0121+\3\2\2\2\u0122\u0123\t\4\2\2\u0123-\3"+
		"\2\2\2\u0124\u0127\7\30\2\2\u0125\u0126\7,\2\2\u0126\u0128\7.\2\2\u0127"+
		"\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\7\60"+
		"\2\2\u012a\u012b\7E\2\2\u012b\u012c\5B\"\2\u012c\u012d\5> \2\u012d/\3"+
		"\2\2\2\u012e\u0131\7\30\2\2\u012f\u0130\7,\2\2\u0130\u0132\7.\2\2\u0131"+
		"\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\7\62"+
		"\2\2\u0134\u0135\7E\2\2\u0135\u0136\5B\"\2\u0136\u0137\5> \2\u0137\61"+
		"\3\2\2\2\u0138\u013b\7\30\2\2\u0139\u013a\7,\2\2\u013a\u013c\7.\2\2\u013b"+
		"\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\7\61"+
		"\2\2\u013e\u013f\7E\2\2\u013f\u0141\5> \2\u0140\u0142\5\34\17\2\u0141"+
		"\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142\63\3\2\2\2\u0143\u0144\7(\2\2"+
		"\u0144\u0145\t\5\2\2\u0145\65\3\2\2\2\u0146\u0147\7(\2\2\u0147\u0148\t"+
		"\2\2\2\u0148\u0149\5L\'\2\u0149\67\3\2\2\2\u014a\u014b\5\66\34\2\u014b"+
		"9\3\2\2\2\u014c\u014d\7/\2\2\u014d\u014e\t\2\2\2\u014e\u014f\5L\'\2\u014f"+
		";\3\2\2\2\u0150\u0151\5:\36\2\u0151=\3\2\2\2\u0152\u0153\7\66\2\2\u0153"+
		"\u0154\5@!\2\u0154\u0155\7\67\2\2\u0155?\3\2\2\2\u0156\u0158\13\2\2\2"+
		"\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u015a\3\2\2\2\u0159\u0157"+
		"\3\2\2\2\u015aA\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u0164\7\b\2\2\u015d"+
		"\u015e\5F$\2\u015e\u0160\7;\2\2\u015f\u0161\7\4\2\2\u0160\u015f\3\2\2"+
		"\2\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u015d\3\2\2\2\u0163\u0166"+
		"\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166"+
		"\u0164\3\2\2\2\u0167\u0168\7\t\2\2\u0168C\3\2\2\2\u0169\u0170\7\b\2\2"+
		"\u016a\u016c\5F$\2\u016b\u016d\7\4\2\2\u016c\u016b\3\2\2\2\u016c\u016d"+
		"\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u016a\3\2\2\2\u016f\u0172\3\2\2\2\u0170"+
		"\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2"+
		"\2\2\u0173\u0174\7\t\2\2\u0174E\3\2\2\2\u0175\u0176\b$\1\2\u0176\u017e"+
		"\5L\'\2\u0177\u017e\5V,\2\u0178\u017e\5H%\2\u0179\u017a\7\b\2\2\u017a"+
		"\u017b\5F$\2\u017b\u017c\7\t\2\2\u017c\u017e\3\2\2\2\u017d\u0175\3\2\2"+
		"\2\u017d\u0177\3\2\2\2\u017d\u0178\3\2\2\2\u017d\u0179\3\2\2\2\u017e\u0187"+
		"\3\2\2\2\u017f\u0180\f\b\2\2\u0180\u0181\t\6\2\2\u0181\u0186\5F$\t\u0182"+
		"\u0183\f\7\2\2\u0183\u0184\t\7\2\2\u0184\u0186\5F$\b\u0185\u017f\3\2\2"+
		"\2\u0185\u0182\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188"+
		"\3\2\2\2\u0188G\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b\5L\'\2\u018b\u018c"+
		"\5D#\2\u018cI\3\2\2\2\u018d\u018e\7\16\2\2\u018eK\3\2\2\2\u018f\u0190"+
		"\t\b\2\2\u0190M\3\2\2\2\u0191\u0192\t\b\2\2\u0192O\3\2\2\2\u0193\u0194"+
		"\t\t\2\2\u0194Q\3\2\2\2\u0195\u019d\7\17\2\2\u0196\u0197\7>\2\2\u0197"+
		"\u0198\7\20\2\2\u0198\u0199\5V,\2\u0199\u019a\7\4\2\2\u019a\u019c\3\2"+
		"\2\2\u019b\u0196\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d"+
		"\u019e\3\2\2\2\u019e\u01a3\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a1\7>"+
		"\2\2\u01a1\u01a2\7\20\2\2\u01a2\u01a4\5V,\2\u01a3\u01a0\3\2\2\2\u01a3"+
		"\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\7\21\2\2\u01a6S\3\2\2\2"+
		"\u01a7\u01ad\7\22\2\2\u01a8\u01a9\5V,\2\u01a9\u01aa\7\4\2\2\u01aa\u01ac"+
		"\3\2\2\2\u01ab\u01a8\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad"+
		"\u01ae\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b2\5V"+
		",\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3"+
		"\u01b4\7\23\2\2\u01b4U\3\2\2\2\u01b5\u01bb\7<\2\2\u01b6\u01bb\7>\2\2\u01b7"+
		"\u01bb\7=\2\2\u01b8\u01bb\5R*\2\u01b9\u01bb\5T+\2\u01ba\u01b5\3\2\2\2"+
		"\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9"+
		"\3\2\2\2\u01bbW\3\2\2\2\67\\`dko{\u0082\u0086\u008d\u0091\u0098\u009c"+
		"\u00a3\u00a7\u00ab\u00b0\u00b8\u00bc\u00c1\u00c4\u00cc\u00d0\u00d2\u00da"+
		"\u00de\u00e3\u00e6\u00ee\u00f2\u00f4\u00fa\u0101\u0108\u010c\u0113\u0119"+
		"\u0127\u0131\u013b\u0141\u0159\u0160\u0164\u016c\u0170\u017d\u0185\u0187"+
		"\u019d\u01a3\u01ad\u01b1\u01ba";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}