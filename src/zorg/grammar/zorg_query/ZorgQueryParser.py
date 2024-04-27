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
        4,1,13,60,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,1,1,3,1,26,8,1,1,2,1,2,
        1,2,3,2,31,8,2,1,2,1,2,1,2,3,2,36,8,2,1,2,1,2,3,2,40,8,2,1,3,1,3,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,1,0,5,10,53,0,20,1,0,0,0,
        2,25,1,0,0,0,4,30,1,0,0,0,6,41,1,0,0,0,8,43,1,0,0,0,10,47,1,0,0,
        0,12,51,1,0,0,0,14,53,1,0,0,0,16,55,1,0,0,0,18,57,1,0,0,0,20,21,
        3,2,1,0,21,22,5,12,0,0,22,1,1,0,0,0,23,26,3,4,2,0,24,26,3,6,3,0,
        25,23,1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,3,8,4,0,28,29,5,13,
        0,0,29,31,1,0,0,0,30,27,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,35,
        3,10,5,0,33,34,5,13,0,0,34,36,3,12,6,0,35,33,1,0,0,0,35,36,1,0,0,
        0,36,39,1,0,0,0,37,38,5,13,0,0,38,40,3,14,7,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,5,1,0,0,0,41,42,3,8,4,0,42,7,1,0,0,0,43,44,5,1,0,0,44,
        45,5,13,0,0,45,46,3,16,8,0,46,9,1,0,0,0,47,48,5,2,0,0,48,49,5,13,
        0,0,49,50,3,18,9,0,50,11,1,0,0,0,51,52,5,3,0,0,52,13,1,0,0,0,53,
        54,5,4,0,0,54,15,1,0,0,0,55,56,7,0,0,0,56,17,1,0,0,0,57,58,5,11,
        0,0,58,19,1,0,0,0,4,25,30,35,39
    ]

class ZorgQueryParser ( Parser ):

    grammarFileName = "ZorgQuery.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'S'", "'W'", "'O'", "'G'", "'file'", 
                     "'note'", "'@'", "'#'", "'+'", "'%'", "'o'", "<INVALID>", 
                     "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NL", "SPACE" ]

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

    ruleNames =  [ "prog", "query", "where_query", "select_query", "select", 
                   "where", "order_by", "group_by", "select_body", "where_body" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NL=12
    SPACE=13

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.query()
            self.state = 21
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
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.where_query()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
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
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 27
                self.select()
                self.state = 28
                self.match(ZorgQueryParser.SPACE)


            self.state = 32
            self.where()
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 33
                self.match(ZorgQueryParser.SPACE)
                self.state = 34
                self.order_by()


            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 37
                self.match(ZorgQueryParser.SPACE)
                self.state = 38
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
            self.state = 41
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
            self.state = 43
            self.match(ZorgQueryParser.T__0)
            self.state = 44
            self.match(ZorgQueryParser.SPACE)
            self.state = 45
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
            self.state = 47
            self.match(ZorgQueryParser.T__1)
            self.state = 48
            self.match(ZorgQueryParser.SPACE)
            self.state = 49
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
            self.state = 51
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
            self.state = 53
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
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
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
            self.state = 57
            self.match(ZorgQueryParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





