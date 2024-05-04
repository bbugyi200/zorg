# Generated from ZorgQuery.g4 by ANTLR 4.13.1
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
        4,1,40,127,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,3,0,39,8,0,1,1,1,
        1,3,1,43,8,1,1,2,1,2,1,2,3,2,48,8,2,1,2,1,2,1,2,3,2,53,8,2,1,2,1,
        2,3,2,57,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,5,9,82,8,9,10,9,12,9,85,
        9,9,1,10,1,10,3,10,89,8,10,1,11,4,11,92,8,11,11,11,12,11,93,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,5,13,103,8,13,10,13,12,13,106,9,13,
        1,13,1,13,1,14,1,14,1,14,3,14,113,8,14,1,15,1,15,1,16,1,16,1,16,
        5,16,120,8,16,10,16,12,16,123,9,16,1,17,1,17,1,17,0,0,18,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,4,2,0,5,6,31,34,4,0,13,
        14,23,23,37,37,39,40,2,0,5,5,31,34,1,0,10,11,119,0,36,1,0,0,0,2,
        42,1,0,0,0,4,47,1,0,0,0,6,58,1,0,0,0,8,60,1,0,0,0,10,64,1,0,0,0,
        12,68,1,0,0,0,14,72,1,0,0,0,16,76,1,0,0,0,18,78,1,0,0,0,20,88,1,
        0,0,0,22,91,1,0,0,0,24,95,1,0,0,0,26,97,1,0,0,0,28,109,1,0,0,0,30,
        114,1,0,0,0,32,116,1,0,0,0,34,124,1,0,0,0,36,38,3,2,1,0,37,39,5,
        12,0,0,38,37,1,0,0,0,38,39,1,0,0,0,39,1,1,0,0,0,40,43,3,4,2,0,41,
        43,3,6,3,0,42,40,1,0,0,0,42,41,1,0,0,0,43,3,1,0,0,0,44,45,3,8,4,
        0,45,46,5,28,0,0,46,48,1,0,0,0,47,44,1,0,0,0,47,48,1,0,0,0,48,49,
        1,0,0,0,49,52,3,10,5,0,50,51,5,28,0,0,51,53,3,12,6,0,52,50,1,0,0,
        0,52,53,1,0,0,0,53,56,1,0,0,0,54,55,5,28,0,0,55,57,3,14,7,0,56,54,
        1,0,0,0,56,57,1,0,0,0,57,5,1,0,0,0,58,59,3,8,4,0,59,7,1,0,0,0,60,
        61,5,1,0,0,61,62,5,28,0,0,62,63,3,16,8,0,63,9,1,0,0,0,64,65,5,2,
        0,0,65,66,5,28,0,0,66,67,3,18,9,0,67,11,1,0,0,0,68,69,5,3,0,0,69,
        70,5,28,0,0,70,71,3,32,16,0,71,13,1,0,0,0,72,73,5,4,0,0,73,74,5,
        28,0,0,74,75,3,28,14,0,75,15,1,0,0,0,76,77,7,0,0,0,77,17,1,0,0,0,
        78,83,3,20,10,0,79,80,5,28,0,0,80,82,3,20,10,0,81,79,1,0,0,0,82,
        85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,19,1,0,0,0,85,83,1,0,0,
        0,86,89,3,22,11,0,87,89,3,26,13,0,88,86,1,0,0,0,88,87,1,0,0,0,89,
        21,1,0,0,0,90,92,3,24,12,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,
        0,0,93,94,1,0,0,0,94,23,1,0,0,0,95,96,7,1,0,0,96,25,1,0,0,0,97,98,
        5,7,0,0,98,99,5,31,0,0,99,104,5,17,0,0,100,101,5,8,0,0,101,103,5,
        17,0,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,
        0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,108,5,9,0,0,108,27,1,0,
        0,0,109,112,3,30,15,0,110,111,5,28,0,0,111,113,3,30,15,0,112,110,
        1,0,0,0,112,113,1,0,0,0,113,29,1,0,0,0,114,115,7,2,0,0,115,31,1,
        0,0,0,116,121,3,34,17,0,117,118,5,28,0,0,118,120,3,34,17,0,119,117,
        1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,33,1,
        0,0,0,123,121,1,0,0,0,124,125,7,3,0,0,125,35,1,0,0,0,11,38,42,47,
        52,56,83,88,93,104,112,121
    ]

class ZorgQueryParser ( Parser ):

    grammarFileName = "ZorgQuery.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'S'", "'W'", "'O'", "'G'", "'file'", 
                     "'note'", "'['", "','", "']'", "'priority'", "'zid'", 
                     "<INVALID>", "'o'", "'x'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'  -'", "'    -'", 
                     "<INVALID>", "'-'", "'.'", "'/'", "'_'", "':'", "' '", 
                     "'('", "')'", "'#'", "'@'", "'+'", "'%'", "'''", "'\"'", 
                     "'~'", "'*'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NL", "LOWER_O", "LOWER_X", "DATE", "TIME", "ID", 
                      "ZID", "NUM_ID", "TWO_SPACE_DASH", "FOUR_SPACE_DASH", 
                      "SYMBOL", "DASH", "DOT", "FSLASH", "UNDERSCORE", "COLON", 
                      "SPACE", "LPAREN", "RPAREN", "HASH", "AT_SIGN", "PLUS", 
                      "PERCENT", "SQUOTE", "DQUOTE", "TILDE", "STAR", "LANGLE", 
                      "RANGLE" ]

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
    RULE_where_atom = 10
    RULE_note_status = 11
    RULE_note_status_char = 12
    RULE_priority_range = 13
    RULE_group_by_body = 14
    RULE_group_by_atom = 15
    RULE_order_by_body = 16
    RULE_order_by_atom = 17

    ruleNames =  [ "prog", "query", "where_query", "select_query", "select", 
                   "where", "order_by", "group_by", "select_body", "where_body", 
                   "where_atom", "note_status", "note_status_char", "priority_range", 
                   "group_by_body", "group_by_atom", "order_by_body", "order_by_atom" ]

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
    LOWER_O=13
    LOWER_X=14
    DATE=15
    TIME=16
    ID=17
    ZID=18
    NUM_ID=19
    TWO_SPACE_DASH=20
    FOUR_SPACE_DASH=21
    SYMBOL=22
    DASH=23
    DOT=24
    FSLASH=25
    UNDERSCORE=26
    COLON=27
    SPACE=28
    LPAREN=29
    RPAREN=30
    HASH=31
    AT_SIGN=32
    PLUS=33
    PERCENT=34
    SQUOTE=35
    DQUOTE=36
    TILDE=37
    STAR=38
    LANGLE=39
    RANGLE=40

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
            self.state = 36
            self.query()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 37
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
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.where_query()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
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
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 44
                self.select()
                self.state = 45
                self.match(ZorgQueryParser.SPACE)


            self.state = 49
            self.where()
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 50
                self.match(ZorgQueryParser.SPACE)
                self.state = 51
                self.order_by()


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 54
                self.match(ZorgQueryParser.SPACE)
                self.state = 55
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
            self.state = 58
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
            self.state = 60
            self.match(ZorgQueryParser.T__0)
            self.state = 61
            self.match(ZorgQueryParser.SPACE)
            self.state = 62
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
            self.state = 64
            self.match(ZorgQueryParser.T__1)
            self.state = 65
            self.match(ZorgQueryParser.SPACE)
            self.state = 66
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

        def SPACE(self):
            return self.getToken(ZorgQueryParser.SPACE, 0)

        def order_by_body(self):
            return self.getTypedRuleContext(ZorgQueryParser.Order_by_bodyContext,0)


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
            self.state = 68
            self.match(ZorgQueryParser.T__2)
            self.state = 69
            self.match(ZorgQueryParser.SPACE)
            self.state = 70
            self.order_by_body()
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

        def SPACE(self):
            return self.getToken(ZorgQueryParser.SPACE, 0)

        def group_by_body(self):
            return self.getTypedRuleContext(ZorgQueryParser.Group_by_bodyContext,0)


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
            self.state = 72
            self.match(ZorgQueryParser.T__3)
            self.state = 73
            self.match(ZorgQueryParser.SPACE)
            self.state = 74
            self.group_by_body()
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
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254816) != 0)):
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

        def where_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgQueryParser.Where_atomContext)
            else:
                return self.getTypedRuleContext(ZorgQueryParser.Where_atomContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgQueryParser.SPACE)
            else:
                return self.getToken(ZorgQueryParser.SPACE, i)

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
            self.state = 78
            self.where_atom()
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 79
                    self.match(ZorgQueryParser.SPACE)
                    self.state = 80
                    self.where_atom() 
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_atomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def note_status(self):
            return self.getTypedRuleContext(ZorgQueryParser.Note_statusContext,0)


        def priority_range(self):
            return self.getTypedRuleContext(ZorgQueryParser.Priority_rangeContext,0)


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_where_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_atom" ):
                listener.enterWhere_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_atom" ):
                listener.exitWhere_atom(self)




    def where_atom(self):

        localctx = ZorgQueryParser.Where_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_where_atom)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 23, 37, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.note_status()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.priority_range()
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 22, self.RULE_note_status)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                self.note_status_char()
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1786714808320) != 0)):
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
        self.enterRule(localctx, 24, self.RULE_note_status_char)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1786714808320) != 0)):
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


    class Priority_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(ZorgQueryParser.HASH, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgQueryParser.ID)
            else:
                return self.getToken(ZorgQueryParser.ID, i)

        def getRuleIndex(self):
            return ZorgQueryParser.RULE_priority_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPriority_range" ):
                listener.enterPriority_range(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPriority_range" ):
                listener.exitPriority_range(self)




    def priority_range(self):

        localctx = ZorgQueryParser.Priority_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_priority_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ZorgQueryParser.T__6)
            self.state = 98
            self.match(ZorgQueryParser.HASH)
            self.state = 99
            self.match(ZorgQueryParser.ID)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 100
                self.match(ZorgQueryParser.T__7)
                self.state = 101
                self.match(ZorgQueryParser.ID)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(ZorgQueryParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_by_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def group_by_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgQueryParser.Group_by_atomContext)
            else:
                return self.getTypedRuleContext(ZorgQueryParser.Group_by_atomContext,i)


        def SPACE(self):
            return self.getToken(ZorgQueryParser.SPACE, 0)

        def getRuleIndex(self):
            return ZorgQueryParser.RULE_group_by_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_by_body" ):
                listener.enterGroup_by_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_by_body" ):
                listener.exitGroup_by_body(self)




    def group_by_body(self):

        localctx = ZorgQueryParser.Group_by_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_group_by_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.group_by_atom()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 110
                self.match(ZorgQueryParser.SPACE)
                self.state = 111
                self.group_by_atom()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_by_atomContext(ParserRuleContext):
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
            return ZorgQueryParser.RULE_group_by_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_by_atom" ):
                listener.enterGroup_by_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_by_atom" ):
                listener.exitGroup_by_atom(self)




    def group_by_atom(self):

        localctx = ZorgQueryParser.Group_by_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_group_by_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254752) != 0)):
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


    class Order_by_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def order_by_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgQueryParser.Order_by_atomContext)
            else:
                return self.getTypedRuleContext(ZorgQueryParser.Order_by_atomContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgQueryParser.SPACE)
            else:
                return self.getToken(ZorgQueryParser.SPACE, i)

        def getRuleIndex(self):
            return ZorgQueryParser.RULE_order_by_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrder_by_body" ):
                listener.enterOrder_by_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrder_by_body" ):
                listener.exitOrder_by_body(self)




    def order_by_body(self):

        localctx = ZorgQueryParser.Order_by_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_order_by_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.order_by_atom()
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 117
                    self.match(ZorgQueryParser.SPACE)
                    self.state = 118
                    self.order_by_atom() 
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Order_by_atomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZorgQueryParser.RULE_order_by_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrder_by_atom" ):
                listener.enterOrder_by_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrder_by_atom" ):
                listener.exitOrder_by_atom(self)




    def order_by_atom(self):

        localctx = ZorgQueryParser.Order_by_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_order_by_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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





