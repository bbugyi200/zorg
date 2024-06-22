# Generated from ZorgMutate.g4 by ANTLR 4.13.1
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
        4,1,37,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,3,1,18,8,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,1,2,
        1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,
        10,12,0,1,1,0,2,9,36,0,14,1,0,0,0,2,17,1,0,0,0,4,25,1,0,0,0,6,28,
        1,0,0,0,8,31,1,0,0,0,10,34,1,0,0,0,12,37,1,0,0,0,14,15,3,2,1,0,15,
        1,1,0,0,0,16,18,5,20,0,0,17,16,1,0,0,0,17,18,1,0,0,0,18,23,1,0,0,
        0,19,24,3,4,2,0,20,24,3,6,3,0,21,24,3,8,4,0,22,24,3,10,5,0,23,19,
        1,0,0,0,23,20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,
        26,5,27,0,0,26,27,3,12,6,0,27,5,1,0,0,0,28,29,5,28,0,0,29,30,3,12,
        6,0,30,7,1,0,0,0,31,32,5,30,0,0,32,33,3,12,6,0,33,9,1,0,0,0,34,35,
        5,29,0,0,35,36,3,12,6,0,36,11,1,0,0,0,37,38,7,0,0,0,38,13,1,0,0,
        0,2,17,23
    ]

class ZorgMutateParser ( Parser ):

    grammarFileName = "ZorgMutate.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'o'", "'x'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'################################'", 
                     "'========================'", "'++++++++++++++++'", 
                     "'--------'", "'  -'", "'    -'", "<INVALID>", "'$'", 
                     "'^'", "'-'", "'.'", "'/'", "'_'", "' '", "'('", "')'", 
                     "'#'", "'@'", "'+'", "'%'", "'''", "'\"'", "'~'", "'*'", 
                     "'<'", "'>'", "':'" ]

    symbolicNames = [ "<INVALID>", "NL", "LOWER_O", "LOWER_X", "DATE", "TIME", 
                      "PRIORITY", "ID", "ZID", "NUM_ID", "SHORT_DATE", "H1_HEADER", 
                      "H2_HEADER", "H3_HEADER", "H4_HEADER", "TWO_SPACE_DASH", 
                      "FOUR_SPACE_DASH", "SYMBOL", "DOLLAR", "HAT", "DASH", 
                      "DOT", "FSLASH", "UNDERSCORE", "SPACE", "LPAREN", 
                      "RPAREN", "HASH", "AT_SIGN", "PLUS", "PERCENT", "SQUOTE", 
                      "DQUOTE", "TILDE", "STAR", "LANGLE", "RANGLE", "COLON" ]

    RULE_prog = 0
    RULE_mut_tag = 1
    RULE_area = 2
    RULE_context = 3
    RULE_person = 4
    RULE_project = 5
    RULE_id = 6

    ruleNames =  [ "prog", "mut_tag", "area", "context", "person", "project", 
                   "id" ]

    EOF = Token.EOF
    NL=1
    LOWER_O=2
    LOWER_X=3
    DATE=4
    TIME=5
    PRIORITY=6
    ID=7
    ZID=8
    NUM_ID=9
    SHORT_DATE=10
    H1_HEADER=11
    H2_HEADER=12
    H3_HEADER=13
    H4_HEADER=14
    TWO_SPACE_DASH=15
    FOUR_SPACE_DASH=16
    SYMBOL=17
    DOLLAR=18
    HAT=19
    DASH=20
    DOT=21
    FSLASH=22
    UNDERSCORE=23
    SPACE=24
    LPAREN=25
    RPAREN=26
    HASH=27
    AT_SIGN=28
    PLUS=29
    PERCENT=30
    SQUOTE=31
    DQUOTE=32
    TILDE=33
    STAR=34
    LANGLE=35
    RANGLE=36
    COLON=37

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

        def mut_tag(self):
            return self.getTypedRuleContext(ZorgMutateParser.Mut_tagContext,0)


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ZorgMutateParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.mut_tag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mut_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def area(self):
            return self.getTypedRuleContext(ZorgMutateParser.AreaContext,0)


        def context(self):
            return self.getTypedRuleContext(ZorgMutateParser.ContextContext,0)


        def person(self):
            return self.getTypedRuleContext(ZorgMutateParser.PersonContext,0)


        def project(self):
            return self.getTypedRuleContext(ZorgMutateParser.ProjectContext,0)


        def DASH(self):
            return self.getToken(ZorgMutateParser.DASH, 0)

        def getRuleIndex(self):
            return ZorgMutateParser.RULE_mut_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMut_tag" ):
                listener.enterMut_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMut_tag" ):
                listener.exitMut_tag(self)




    def mut_tag(self):

        localctx = ZorgMutateParser.Mut_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mut_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 16
                self.match(ZorgMutateParser.DASH)


            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 19
                self.area()
                pass
            elif token in [28]:
                self.state = 20
                self.context()
                pass
            elif token in [30]:
                self.state = 21
                self.person()
                pass
            elif token in [29]:
                self.state = 22
                self.project()
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


    class AreaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(ZorgMutateParser.HASH, 0)

        def id_(self):
            return self.getTypedRuleContext(ZorgMutateParser.IdContext,0)


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_area

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArea" ):
                listener.enterArea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArea" ):
                listener.exitArea(self)




    def area(self):

        localctx = ZorgMutateParser.AreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ZorgMutateParser.HASH)
            self.state = 26
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_SIGN(self):
            return self.getToken(ZorgMutateParser.AT_SIGN, 0)

        def id_(self):
            return self.getTypedRuleContext(ZorgMutateParser.IdContext,0)


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_context

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContext" ):
                listener.enterContext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContext" ):
                listener.exitContext(self)




    def context(self):

        localctx = ZorgMutateParser.ContextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ZorgMutateParser.AT_SIGN)
            self.state = 29
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PersonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(ZorgMutateParser.PERCENT, 0)

        def id_(self):
            return self.getTypedRuleContext(ZorgMutateParser.IdContext,0)


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_person

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPerson" ):
                listener.enterPerson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPerson" ):
                listener.exitPerson(self)




    def person(self):

        localctx = ZorgMutateParser.PersonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ZorgMutateParser.PERCENT)
            self.state = 32
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ZorgMutateParser.PLUS, 0)

        def id_(self):
            return self.getTypedRuleContext(ZorgMutateParser.IdContext,0)


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_project

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProject" ):
                listener.enterProject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProject" ):
                listener.exitProject(self)




    def project(self):

        localctx = ZorgMutateParser.ProjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ZorgMutateParser.PLUS)
            self.state = 35
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZorgMutateParser.ID, 0)

        def NUM_ID(self):
            return self.getToken(ZorgMutateParser.NUM_ID, 0)

        def PRIORITY(self):
            return self.getToken(ZorgMutateParser.PRIORITY, 0)

        def DATE(self):
            return self.getToken(ZorgMutateParser.DATE, 0)

        def TIME(self):
            return self.getToken(ZorgMutateParser.TIME, 0)

        def ZID(self):
            return self.getToken(ZorgMutateParser.ZID, 0)

        def LOWER_O(self):
            return self.getToken(ZorgMutateParser.LOWER_O, 0)

        def LOWER_X(self):
            return self.getToken(ZorgMutateParser.LOWER_X, 0)

        def getRuleIndex(self):
            return ZorgMutateParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)




    def id_(self):

        localctx = ZorgMutateParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1020) != 0)):
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





