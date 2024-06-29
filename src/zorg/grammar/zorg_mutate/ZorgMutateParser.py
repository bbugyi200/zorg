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
        4,1,41,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,3,0,38,8,0,1,1,1,1,1,
        1,1,1,3,1,44,8,1,1,2,1,2,1,3,3,3,49,8,3,1,3,1,3,1,4,1,4,1,4,1,4,
        3,4,57,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,9,1,9,3,9,77,8,9,1,10,1,10,1,11,1,11,1,12,3,12,84,8,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,0,2,4,0,4,4,9,9,24,24,37,37,1,0,8,15,88,0,28,1,
        0,0,0,2,43,1,0,0,0,4,45,1,0,0,0,6,48,1,0,0,0,8,56,1,0,0,0,10,58,
        1,0,0,0,12,61,1,0,0,0,14,64,1,0,0,0,16,67,1,0,0,0,18,76,1,0,0,0,
        20,78,1,0,0,0,22,80,1,0,0,0,24,83,1,0,0,0,26,89,1,0,0,0,28,33,3,
        2,1,0,29,30,5,28,0,0,30,32,3,2,1,0,31,29,1,0,0,0,32,35,1,0,0,0,33,
        31,1,0,0,0,33,34,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,36,38,5,7,0,
        0,37,36,1,0,0,0,37,38,1,0,0,0,38,1,1,0,0,0,39,44,3,4,2,0,40,44,3,
        6,3,0,41,44,3,18,9,0,42,44,3,24,12,0,43,39,1,0,0,0,43,40,1,0,0,0,
        43,41,1,0,0,0,43,42,1,0,0,0,44,3,1,0,0,0,45,46,7,0,0,0,46,5,1,0,
        0,0,47,49,5,24,0,0,48,47,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,
        51,3,8,4,0,51,7,1,0,0,0,52,57,3,10,5,0,53,57,3,12,6,0,54,57,3,14,
        7,0,55,57,3,16,8,0,56,52,1,0,0,0,56,53,1,0,0,0,56,54,1,0,0,0,56,
        55,1,0,0,0,57,9,1,0,0,0,58,59,5,31,0,0,59,60,3,26,13,0,60,11,1,0,
        0,0,61,62,5,32,0,0,62,63,3,26,13,0,63,13,1,0,0,0,64,65,5,34,0,0,
        65,66,3,26,13,0,66,15,1,0,0,0,67,68,5,33,0,0,68,69,3,26,13,0,69,
        17,1,0,0,0,70,71,3,20,10,0,71,72,5,41,0,0,72,73,3,22,11,0,73,77,
        1,0,0,0,74,75,5,24,0,0,75,77,3,20,10,0,76,70,1,0,0,0,76,74,1,0,0,
        0,77,19,1,0,0,0,78,79,3,26,13,0,79,21,1,0,0,0,80,81,3,26,13,0,81,
        23,1,0,0,0,82,84,5,24,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,0,
        0,0,85,86,5,1,0,0,86,87,3,26,13,0,87,88,5,2,0,0,88,25,1,0,0,0,89,
        90,7,1,0,0,90,27,1,0,0,0,7,33,37,43,48,56,76,83
    ]

class ZorgMutateParser ( Parser ):

    grammarFileName = "ZorgMutate.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'[['", "']]'", "'s='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'o'", "'x'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'################################'", 
                     "'========================'", "'++++++++++++++++'", 
                     "'--------'", "<INVALID>", "'$'", "'^'", "'-'", "'.'", 
                     "'/'", "'_'", "' '", "'('", "')'", "'#'", "'@'", "'+'", 
                     "'%'", "'''", "'\"'", "'~'", "'*'", "'<'", "'>'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "S_EQUAL", 
                      "OPEN_TODO_MUT", "OPEN_TODO_CHAR", "DIGIT", "NL", 
                      "LOWER_O", "LOWER_X", "DATE", "TIME", "PRIORITY", 
                      "ID", "ZID", "NUM_ID", "SHORT_DATE", "H1_HEADER", 
                      "H2_HEADER", "H3_HEADER", "H4_HEADER", "SYMBOL", "DOLLAR", 
                      "HAT", "DASH", "DOT", "FSLASH", "UNDERSCORE", "SPACE", 
                      "LPAREN", "RPAREN", "HASH", "AT_SIGN", "PLUS", "PERCENT", 
                      "SQUOTE", "DQUOTE", "TILDE", "STAR", "LANGLE", "RANGLE", 
                      "COLON" ]

    RULE_prog = 0
    RULE_mut_cmd = 1
    RULE_mut_note_type = 2
    RULE_mut_tag = 3
    RULE_tag = 4
    RULE_area = 5
    RULE_context = 6
    RULE_person = 7
    RULE_project = 8
    RULE_mut_prop = 9
    RULE_key = 10
    RULE_value = 11
    RULE_mut_link = 12
    RULE_id = 13

    ruleNames =  [ "prog", "mut_cmd", "mut_note_type", "mut_tag", "tag", 
                   "area", "context", "person", "project", "mut_prop", "key", 
                   "value", "mut_link", "id" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    S_EQUAL=3
    OPEN_TODO_MUT=4
    OPEN_TODO_CHAR=5
    DIGIT=6
    NL=7
    LOWER_O=8
    LOWER_X=9
    DATE=10
    TIME=11
    PRIORITY=12
    ID=13
    ZID=14
    NUM_ID=15
    SHORT_DATE=16
    H1_HEADER=17
    H2_HEADER=18
    H3_HEADER=19
    H4_HEADER=20
    SYMBOL=21
    DOLLAR=22
    HAT=23
    DASH=24
    DOT=25
    FSLASH=26
    UNDERSCORE=27
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
    COLON=41

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

        def NL(self):
            return self.getToken(ZorgMutateParser.NL, 0)

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
            self.state = 28
            self.mut_cmd()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 29
                self.match(ZorgMutateParser.SPACE)
                self.state = 30
                self.mut_cmd()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 36
                self.match(ZorgMutateParser.NL)


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

        def mut_note_type(self):
            return self.getTypedRuleContext(ZorgMutateParser.Mut_note_typeContext,0)


        def mut_tag(self):
            return self.getTypedRuleContext(ZorgMutateParser.Mut_tagContext,0)


        def mut_prop(self):
            return self.getTypedRuleContext(ZorgMutateParser.Mut_propContext,0)


        def mut_link(self):
            return self.getTypedRuleContext(ZorgMutateParser.Mut_linkContext,0)


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
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.mut_note_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.mut_tag()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.mut_prop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.mut_link()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mut_note_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(ZorgMutateParser.DASH, 0)

        def TILDE(self):
            return self.getToken(ZorgMutateParser.TILDE, 0)

        def LOWER_X(self):
            return self.getToken(ZorgMutateParser.LOWER_X, 0)

        def OPEN_TODO_MUT(self):
            return self.getToken(ZorgMutateParser.OPEN_TODO_MUT, 0)

        def getRuleIndex(self):
            return ZorgMutateParser.RULE_mut_note_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMut_note_type" ):
                listener.enterMut_note_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMut_note_type" ):
                listener.exitMut_note_type(self)




    def mut_note_type(self):

        localctx = ZorgMutateParser.Mut_note_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mut_note_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137455731216) != 0)):
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


    class Mut_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag(self):
            return self.getTypedRuleContext(ZorgMutateParser.TagContext,0)


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
        self.enterRule(localctx, 6, self.RULE_mut_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 47
                self.match(ZorgMutateParser.DASH)


            self.state = 50
            self.tag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)




    def tag(self):

        localctx = ZorgMutateParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tag)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.area()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.context()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.person()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
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
        self.enterRule(localctx, 10, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ZorgMutateParser.HASH)
            self.state = 59
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
        self.enterRule(localctx, 12, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ZorgMutateParser.AT_SIGN)
            self.state = 62
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
        self.enterRule(localctx, 14, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ZorgMutateParser.PERCENT)
            self.state = 65
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
        self.enterRule(localctx, 16, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ZorgMutateParser.PLUS)
            self.state = 68
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

        def key(self):
            return self.getTypedRuleContext(ZorgMutateParser.KeyContext,0)


        def COLON(self):
            return self.getToken(ZorgMutateParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(ZorgMutateParser.ValueContext,0)


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
        self.enterRule(localctx, 18, self.RULE_mut_prop)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.key()
                self.state = 71
                self.match(ZorgMutateParser.COLON)
                self.state = 72
                self.value()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(ZorgMutateParser.DASH)
                self.state = 75
                self.key()
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


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ZorgMutateParser.IdContext,0)


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = ZorgMutateParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ZorgMutateParser.IdContext,0)


        def getRuleIndex(self):
            return ZorgMutateParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ZorgMutateParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mut_linkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ZorgMutateParser.IdContext,0)


        def DASH(self):
            return self.getToken(ZorgMutateParser.DASH, 0)

        def getRuleIndex(self):
            return ZorgMutateParser.RULE_mut_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMut_link" ):
                listener.enterMut_link(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMut_link" ):
                listener.exitMut_link(self)




    def mut_link(self):

        localctx = ZorgMutateParser.Mut_linkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mut_link)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 82
                self.match(ZorgMutateParser.DASH)


            self.state = 85
            self.match(ZorgMutateParser.T__0)
            self.state = 86
            self.id_()
            self.state = 87
            self.match(ZorgMutateParser.T__1)
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
        self.enterRule(localctx, 26, self.RULE_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65280) != 0)):
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





