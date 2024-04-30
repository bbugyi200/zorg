# Generated from src/zorg/grammar/zorg_query/ZorgQuery.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,3,0,27,8,0,
        1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,3,2,36,8,2,1,2,1,2,1,2,3,2,41,8,2,
        1,2,1,2,3,2,45,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,
        6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,66,8,10,11,10,12,10,67,1,11,
        1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,2,2,0,5,6,9,12,
        1,0,13,18,65,0,24,1,0,0,0,2,30,1,0,0,0,4,35,1,0,0,0,6,46,1,0,0,0,
        8,48,1,0,0,0,10,52,1,0,0,0,12,56,1,0,0,0,14,58,1,0,0,0,16,60,1,0,
        0,0,18,62,1,0,0,0,20,65,1,0,0,0,22,69,1,0,0,0,24,26,3,2,1,0,25,27,
        5,7,0,0,26,25,1,0,0,0,26,27,1,0,0,0,27,1,1,0,0,0,28,31,3,4,2,0,29,
        31,3,6,3,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,3,8,4,
        0,33,34,5,8,0,0,34,36,1,0,0,0,35,32,1,0,0,0,35,36,1,0,0,0,36,37,
        1,0,0,0,37,40,3,10,5,0,38,39,5,8,0,0,39,41,3,12,6,0,40,38,1,0,0,
        0,40,41,1,0,0,0,41,44,1,0,0,0,42,43,5,8,0,0,43,45,3,14,7,0,44,42,
        1,0,0,0,44,45,1,0,0,0,45,5,1,0,0,0,46,47,3,8,4,0,47,7,1,0,0,0,48,
        49,5,1,0,0,49,50,5,8,0,0,50,51,3,16,8,0,51,9,1,0,0,0,52,53,5,2,0,
        0,53,54,5,8,0,0,54,55,3,18,9,0,55,11,1,0,0,0,56,57,5,3,0,0,57,13,
        1,0,0,0,58,59,5,4,0,0,59,15,1,0,0,0,60,61,7,0,0,0,61,17,1,0,0,0,
        62,63,3,20,10,0,63,19,1,0,0,0,64,66,3,22,11,0,65,64,1,0,0,0,66,67,
        1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,21,1,0,0,0,69,70,7,1,0,0,
        70,23,1,0,0,0,6,26,30,35,40,44,67
    ]

class ZorgQueryParser ( Parser ):

    grammarFileName = "ZorgQuery.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'S'", "'W'", "'O'", "'G'", "'file'", 
                     "'note'", "<INVALID>", "' '", "'+'", "'@'", "'%'", 
                     "'#'", "'-'", "'o'", "'x'", "'<'", "'>'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NL", "SPACE", 
                      "PLUS", "AT_SIGN", "PERCENT", "HASH", "DASH", "LOWER_O", 
                      "LOWER_X", "LANGLE", "RANGLE", "TILDE" ]

    RULE_prog = 0
    RULE_query = 1
    RULE_where_query = 2
    RULE_select_query = 3
    RULE_select = 4
    RULE_where = 5
    RULE_order_by = 6
    RULE_group_by = 7
    RULE_select_body = 8
    RULE_where_body = 9
    RULE_note_status = 10
    RULE_note_status_char = 11

    ruleNames =  [ "prog", "query", "where_query", "select_query", "select", 
                   "where", "order_by", "group_by", "select_body", "where_body", 
                   "note_status", "note_status_char" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NL=7
    SPACE=8
    PLUS=9
    AT_SIGN=10
    PERCENT=11
    HASH=12
    DASH=13
    LOWER_O=14
    LOWER_X=15
    LANGLE=16
    RANGLE=17
    TILDE=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query(self):
            return self.getTypedRuleContext(ZorgQueryParser.QueryContext,0)


        def NL(self):
            return self.getToken(ZorgQueryParser.NL, 0)

        def getRuleIndex(self):
            return ZorgQueryParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ZorgQueryParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.query()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 25
                self.match(ZorgQueryParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def where_query(self):
            return self.getTypedRuleContext(ZorgQueryParser.Where_queryContext,0)


        def select_query(self):
            return self.getTypedRuleContext(ZorgQueryParser.Select_queryContext,0)


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = ZorgQueryParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.where_query()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.select_query()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def where(self):
            return self.getTypedRuleContext(ZorgQueryParser.WhereContext,0)


        def select(self):
            return self.getTypedRuleContext(ZorgQueryParser.SelectContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgQueryParser.SPACE)
            else:
                return self.getToken(ZorgQueryParser.SPACE, i)

        def order_by(self):
            return self.getTypedRuleContext(ZorgQueryParser.Order_byContext,0)


        def group_by(self):
            return self.getTypedRuleContext(ZorgQueryParser.Group_byContext,0)


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_where_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_query" ):
                listener.enterWhere_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_query" ):
                listener.exitWhere_query(self)




    def where_query(self):

        localctx = ZorgQueryParser.Where_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_where_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 32
                self.select()
                self.state = 33
                self.match(ZorgQueryParser.SPACE)


            self.state = 37
            self.where()
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 38
                self.match(ZorgQueryParser.SPACE)
                self.state = 39
                self.order_by()


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 42
                self.match(ZorgQueryParser.SPACE)
                self.state = 43
                self.group_by()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select(self):
            return self.getTypedRuleContext(ZorgQueryParser.SelectContext,0)


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_select_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_query" ):
                listener.enterSelect_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_query" ):
                listener.exitSelect_query(self)




    def select_query(self):

        localctx = ZorgQueryParser.Select_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_select_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.select()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self):
            return self.getToken(ZorgQueryParser.SPACE, 0)

        def select_body(self):
            return self.getTypedRuleContext(ZorgQueryParser.Select_bodyContext,0)


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)




    def select(self):

        localctx = ZorgQueryParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_select)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ZorgQueryParser.T__0)
            self.state = 49
            self.match(ZorgQueryParser.SPACE)
            self.state = 50
            self.select_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self):
            return self.getToken(ZorgQueryParser.SPACE, 0)

        def where_body(self):
            return self.getTypedRuleContext(ZorgQueryParser.Where_bodyContext,0)


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_where

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere" ):
                listener.enterWhere(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere" ):
                listener.exitWhere(self)




    def where(self):

        localctx = ZorgQueryParser.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_where)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ZorgQueryParser.T__1)
            self.state = 53
            self.match(ZorgQueryParser.SPACE)
            self.state = 54
            self.where_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Order_byContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_order_by

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrder_by" ):
                listener.enterOrder_by(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrder_by" ):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = ZorgQueryParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_order_by)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ZorgQueryParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_byContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_group_by

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_by" ):
                listener.enterGroup_by(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_by" ):
                listener.exitGroup_by(self)




    def group_by(self):

        localctx = ZorgQueryParser.Group_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_group_by)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ZorgQueryParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_SIGN(self):
            return self.getToken(ZorgQueryParser.AT_SIGN, 0)

        def HASH(self):
            return self.getToken(ZorgQueryParser.HASH, 0)

        def PLUS(self):
            return self.getToken(ZorgQueryParser.PLUS, 0)

        def PERCENT(self):
            return self.getToken(ZorgQueryParser.PERCENT, 0)

        def getRuleIndex(self):
            return ZorgQueryParser.RULE_select_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_body" ):
                listener.enterSelect_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_body" ):
                listener.exitSelect_body(self)




    def select_body(self):

        localctx = ZorgQueryParser.Select_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_select_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7776) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def note_status(self):
            return self.getTypedRuleContext(ZorgQueryParser.Note_statusContext,0)


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_where_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_body" ):
                listener.enterWhere_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_body" ):
                listener.exitWhere_body(self)




    def where_body(self):

        localctx = ZorgQueryParser.Where_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_where_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.note_status()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Note_statusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def note_status_char(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgQueryParser.Note_status_charContext)
            else:
                return self.getTypedRuleContext(ZorgQueryParser.Note_status_charContext,i)


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_note_status

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote_status" ):
                listener.enterNote_status(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote_status" ):
                listener.exitNote_status(self)




    def note_status(self):

        localctx = ZorgQueryParser.Note_statusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_note_status)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.note_status_char()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Note_status_charContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(ZorgQueryParser.DASH, 0)

        def LOWER_O(self):
            return self.getToken(ZorgQueryParser.LOWER_O, 0)

        def LOWER_X(self):
            return self.getToken(ZorgQueryParser.LOWER_X, 0)

        def TILDE(self):
            return self.getToken(ZorgQueryParser.TILDE, 0)

        def LANGLE(self):
            return self.getToken(ZorgQueryParser.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(ZorgQueryParser.RANGLE, 0)

        def getRuleIndex(self):
            return ZorgQueryParser.RULE_note_status_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote_status_char" ):
                listener.enterNote_status_char(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote_status_char" ):
                listener.exitNote_status_char(self)




    def note_status_char(self):

        localctx = ZorgQueryParser.Note_status_charContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_note_status_char)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





