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
        4,1,35,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,1,1,
        1,3,1,29,8,1,1,2,3,2,32,8,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,3,1,3,1,
        3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,58,8,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,2,9,59,
        0,18,1,0,0,0,2,28,1,0,0,0,4,31,1,0,0,0,6,39,1,0,0,0,8,42,1,0,0,0,
        10,45,1,0,0,0,12,48,1,0,0,0,14,57,1,0,0,0,16,59,1,0,0,0,18,23,3,
        2,1,0,19,20,5,22,0,0,20,22,3,2,1,0,21,19,1,0,0,0,22,25,1,0,0,0,23,
        21,1,0,0,0,23,24,1,0,0,0,24,1,1,0,0,0,25,23,1,0,0,0,26,29,3,4,2,
        0,27,29,3,14,7,0,28,26,1,0,0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,32,
        5,18,0,0,31,30,1,0,0,0,31,32,1,0,0,0,32,37,1,0,0,0,33,38,3,6,3,0,
        34,38,3,8,4,0,35,38,3,10,5,0,36,38,3,12,6,0,37,33,1,0,0,0,37,34,
        1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,5,1,0,0,0,39,40,5,25,0,0,
        40,41,3,16,8,0,41,7,1,0,0,0,42,43,5,26,0,0,43,44,3,16,8,0,44,9,1,
        0,0,0,45,46,5,28,0,0,46,47,3,16,8,0,47,11,1,0,0,0,48,49,5,27,0,0,
        49,50,3,16,8,0,50,13,1,0,0,0,51,52,3,16,8,0,52,53,5,35,0,0,53,54,
        3,16,8,0,54,58,1,0,0,0,55,56,5,18,0,0,56,58,3,16,8,0,57,51,1,0,0,
        0,57,55,1,0,0,0,58,15,1,0,0,0,59,60,7,0,0,0,60,17,1,0,0,0,5,23,28,
        31,37,57
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
                     "'--------'", "<INVALID>", "'$'", "'^'", "'-'", "'.'", 
                     "'/'", "'_'", "' '", "'('", "')'", "'#'", "'@'", "'+'", 
                     "'%'", "'''", "'\"'", "'~'", "'*'", "'<'", "'>'", "':'" ]

    symbolicNames = [ "<INVALID>", "NL", "LOWER_O", "LOWER_X", "DATE", "TIME", 
                      "PRIORITY", "ID", "ZID", "NUM_ID", "SHORT_DATE", "H1_HEADER", 
                      "H2_HEADER", "H3_HEADER", "H4_HEADER", "SYMBOL", "DOLLAR", 
                      "HAT", "DASH", "DOT", "FSLASH", "UNDERSCORE", "SPACE", 
                      "LPAREN", "RPAREN", "HASH", "AT_SIGN", "PLUS", "PERCENT", 
                      "SQUOTE", "DQUOTE", "TILDE", "STAR", "LANGLE", "RANGLE", 
                      "COLON" ]

    RULE_prog = 0
    RULE_mut_cmd = 1
    RULE_mut_tag = 2
    RULE_area = 3
    RULE_context = 4
    RULE_person = 5
    RULE_project = 6
    RULE_mut_prop = 7
    RULE_id = 8

    ruleNames =  [ "prog", "mut_cmd", "mut_tag", "area", "context", "person", 
                   "project", "mut_prop", "id" ]

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
    SYMBOL=15
    DOLLAR=16
    HAT=17
    DASH=18
    DOT=19
    FSLASH=20
    UNDERSCORE=21
    SPACE=22
    LPAREN=23
    RPAREN=24
    HASH=25
    AT_SIGN=26
    PLUS=27
    PERCENT=28
    SQUOTE=29
    DQUOTE=30
    TILDE=31
    STAR=32
    LANGLE=33
    RANGLE=34
    COLON=35

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

        def mut_cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgMutateParser.Mut_cmdContext)
            else:
                return self.getTypedRuleContext(ZorgMutateParser.Mut_cmdContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgMutateParser.SPACE)
            else:
                return self.getToken(ZorgMutateParser.SPACE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.mut_cmd()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 19
                self.match(ZorgMutateParser.SPACE)
                self.state = 20
                self.mut_cmd()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mut_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mut_tag(self):
            return self.getTypedRuleContext(ZorgMutateParser.Mut_tagContext,0)


        def mut_prop(self):
            return self.getTypedRuleContext(ZorgMutateParser.Mut_propContext,0)


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_mut_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMut_cmd" ):
                listener.enterMut_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMut_cmd" ):
                listener.exitMut_cmd(self)




    def mut_cmd(self):

        localctx = ZorgMutateParser.Mut_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mut_cmd)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.mut_tag()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.mut_prop()
                pass


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
        self.enterRule(localctx, 4, self.RULE_mut_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 30
                self.match(ZorgMutateParser.DASH)


            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 33
                self.area()
                pass
            elif token in [26]:
                self.state = 34
                self.context()
                pass
            elif token in [28]:
                self.state = 35
                self.person()
                pass
            elif token in [27]:
                self.state = 36
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
        self.enterRule(localctx, 6, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ZorgMutateParser.HASH)
            self.state = 40
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
        self.enterRule(localctx, 8, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ZorgMutateParser.AT_SIGN)
            self.state = 43
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
        self.enterRule(localctx, 10, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ZorgMutateParser.PERCENT)
            self.state = 46
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
        self.enterRule(localctx, 12, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ZorgMutateParser.PLUS)
            self.state = 49
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mut_propContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgMutateParser.IdContext)
            else:
                return self.getTypedRuleContext(ZorgMutateParser.IdContext,i)


        def COLON(self):
            return self.getToken(ZorgMutateParser.COLON, 0)

        def DASH(self):
            return self.getToken(ZorgMutateParser.DASH, 0)

        def getRuleIndex(self):
            return ZorgMutateParser.RULE_mut_prop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMut_prop" ):
                listener.enterMut_prop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMut_prop" ):
                listener.exitMut_prop(self)




    def mut_prop(self):

        localctx = ZorgMutateParser.Mut_propContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mut_prop)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.id_()
                self.state = 52
                self.match(ZorgMutateParser.COLON)
                self.state = 53
                self.id_()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(ZorgMutateParser.DASH)
                self.state = 56
                self.id_()
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
        self.enterRule(localctx, 16, self.RULE_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
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





