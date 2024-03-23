# Generated from src/zorg/grammar/zorg_file/ZorgFile.g4 by ANTLR 4.13.1
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
        4,1,20,238,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,4,
        0,55,8,0,11,0,12,0,56,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,5,0,66,
        8,0,10,0,12,0,69,9,0,3,0,71,8,0,1,0,1,0,1,1,4,1,76,8,1,11,1,12,1,
        77,1,2,1,2,3,2,82,8,2,1,2,1,2,1,3,4,3,87,8,3,11,3,12,3,88,1,3,3,
        3,92,8,3,1,4,1,4,3,4,96,8,4,1,5,1,5,1,5,3,5,101,8,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,4,8,115,8,8,11,8,12,8,116,1,
        9,1,9,3,9,121,8,9,1,9,1,9,1,9,1,9,1,9,3,9,128,8,9,1,9,5,9,131,8,
        9,10,9,12,9,134,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,
        1,12,3,12,146,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,
        1,16,1,16,1,16,1,17,1,17,1,17,3,17,163,8,17,1,17,1,17,1,18,1,18,
        5,18,169,8,18,10,18,12,18,172,9,18,1,18,3,18,175,8,18,1,18,5,18,
        178,8,18,10,18,12,18,181,9,18,1,19,1,19,5,19,185,8,19,10,19,12,19,
        188,9,19,1,19,3,19,191,8,19,1,19,5,19,194,8,19,10,19,12,19,197,9,
        19,1,20,1,20,5,20,201,8,20,10,20,12,20,204,9,20,1,20,3,20,207,8,
        20,1,20,5,20,210,8,20,10,20,12,20,213,9,20,1,21,1,21,5,21,217,8,
        21,10,21,12,21,220,9,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,0,0,26,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,1,
        2,0,1,1,9,11,243,0,52,1,0,0,0,2,75,1,0,0,0,4,79,1,0,0,0,6,86,1,0,
        0,0,8,95,1,0,0,0,10,97,1,0,0,0,12,105,1,0,0,0,14,109,1,0,0,0,16,
        114,1,0,0,0,18,118,1,0,0,0,20,135,1,0,0,0,22,139,1,0,0,0,24,145,
        1,0,0,0,26,147,1,0,0,0,28,150,1,0,0,0,30,153,1,0,0,0,32,156,1,0,
        0,0,34,159,1,0,0,0,36,166,1,0,0,0,38,182,1,0,0,0,40,198,1,0,0,0,
        42,214,1,0,0,0,44,221,1,0,0,0,46,225,1,0,0,0,48,229,1,0,0,0,50,233,
        1,0,0,0,52,70,3,2,1,0,53,55,5,18,0,0,54,53,1,0,0,0,55,56,1,0,0,0,
        56,54,1,0,0,0,56,57,1,0,0,0,57,61,1,0,0,0,58,60,3,6,3,0,59,58,1,
        0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,67,1,0,0,0,63,
        61,1,0,0,0,64,66,3,36,18,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,
        0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,70,54,1,0,0,0,70,71,
        1,0,0,0,71,72,1,0,0,0,72,73,5,0,0,1,73,1,1,0,0,0,74,76,3,4,2,0,75,
        74,1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,3,1,0,0,
        0,79,81,5,1,0,0,80,82,3,16,8,0,81,80,1,0,0,0,81,82,1,0,0,0,82,83,
        1,0,0,0,83,84,5,18,0,0,84,5,1,0,0,0,85,87,3,8,4,0,86,85,1,0,0,0,
        87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,92,5,
        18,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,7,1,0,0,0,93,96,3,10,5,0,94,
        96,3,14,7,0,95,93,1,0,0,0,95,94,1,0,0,0,96,9,1,0,0,0,97,100,5,2,
        0,0,98,99,5,3,0,0,99,101,3,12,6,0,100,98,1,0,0,0,100,101,1,0,0,0,
        101,102,1,0,0,0,102,103,3,16,8,0,103,104,5,18,0,0,104,11,1,0,0,0,
        105,106,5,4,0,0,106,107,5,19,0,0,107,108,5,5,0,0,108,13,1,0,0,0,
        109,110,5,6,0,0,110,111,3,16,8,0,111,112,5,18,0,0,112,15,1,0,0,0,
        113,115,3,18,9,0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,1,0,0,0,
        116,117,1,0,0,0,117,17,1,0,0,0,118,120,5,3,0,0,119,121,5,7,0,0,120,
        119,1,0,0,0,120,121,1,0,0,0,121,127,1,0,0,0,122,128,3,24,12,0,123,
        128,3,22,11,0,124,128,3,34,17,0,125,128,3,20,10,0,126,128,5,19,0,
        0,127,122,1,0,0,0,127,123,1,0,0,0,127,124,1,0,0,0,127,125,1,0,0,
        0,127,126,1,0,0,0,127,128,1,0,0,0,128,132,1,0,0,0,129,131,5,20,0,
        0,130,129,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,
        0,133,19,1,0,0,0,134,132,1,0,0,0,135,136,5,19,0,0,136,137,5,8,0,
        0,137,138,5,19,0,0,138,21,1,0,0,0,139,140,7,0,0,0,140,23,1,0,0,0,
        141,146,3,26,13,0,142,146,3,28,14,0,143,146,3,30,15,0,144,146,3,
        32,16,0,145,141,1,0,0,0,145,142,1,0,0,0,145,143,1,0,0,0,145,144,
        1,0,0,0,146,25,1,0,0,0,147,148,5,1,0,0,148,149,5,19,0,0,149,27,1,
        0,0,0,150,151,5,9,0,0,151,152,5,19,0,0,152,29,1,0,0,0,153,154,5,
        10,0,0,154,155,5,19,0,0,155,31,1,0,0,0,156,157,5,11,0,0,157,158,
        5,19,0,0,158,33,1,0,0,0,159,162,5,12,0,0,160,163,5,19,0,0,161,163,
        3,20,10,0,162,160,1,0,0,0,162,161,1,0,0,0,163,164,1,0,0,0,164,165,
        5,13,0,0,165,35,1,0,0,0,166,170,3,44,22,0,167,169,3,6,3,0,168,167,
        1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,179,
        1,0,0,0,172,170,1,0,0,0,173,175,5,18,0,0,174,173,1,0,0,0,174,175,
        1,0,0,0,175,176,1,0,0,0,176,178,3,38,19,0,177,174,1,0,0,0,178,181,
        1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,37,1,0,0,0,181,179,1,
        0,0,0,182,186,3,46,23,0,183,185,3,6,3,0,184,183,1,0,0,0,185,188,
        1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,195,1,0,0,0,188,186,
        1,0,0,0,189,191,5,18,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,
        1,0,0,0,192,194,3,40,20,0,193,190,1,0,0,0,194,197,1,0,0,0,195,193,
        1,0,0,0,195,196,1,0,0,0,196,39,1,0,0,0,197,195,1,0,0,0,198,202,3,
        48,24,0,199,201,3,6,3,0,200,199,1,0,0,0,201,204,1,0,0,0,202,200,
        1,0,0,0,202,203,1,0,0,0,203,211,1,0,0,0,204,202,1,0,0,0,205,207,
        5,18,0,0,206,205,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,210,
        3,42,21,0,209,206,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,
        1,0,0,0,212,41,1,0,0,0,213,211,1,0,0,0,214,218,3,50,25,0,215,217,
        3,6,3,0,216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,
        1,0,0,0,219,43,1,0,0,0,220,218,1,0,0,0,221,222,5,14,0,0,222,223,
        3,16,8,0,223,224,5,18,0,0,224,45,1,0,0,0,225,226,5,15,0,0,226,227,
        3,16,8,0,227,228,5,18,0,0,228,47,1,0,0,0,229,230,5,16,0,0,230,231,
        3,16,8,0,231,232,5,18,0,0,232,49,1,0,0,0,233,234,5,17,0,0,234,235,
        3,16,8,0,235,236,5,18,0,0,236,51,1,0,0,0,26,56,61,67,70,77,81,88,
        91,95,100,116,120,127,132,145,162,170,174,179,186,190,195,202,206,
        211,218
    ]

class ZorgFileParser ( Parser ):

    grammarFileName = "ZorgFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'o'", "' '", "'[#'", "']'", "'-'", 
                     "'('", "'::'", "'@'", "'%'", "'+'", "'[['", "']]'", 
                     "'#########'", "'======='", "'*****'", "'---'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NL", "ID", "SYMBOL" ]

    RULE_prog = 0
    RULE_head = 1
    RULE_comment = 2
    RULE_block = 3
    RULE_item = 4
    RULE_todo = 5
    RULE_priority = 6
    RULE_note = 7
    RULE_space_atoms = 8
    RULE_space_atom = 9
    RULE_property = 10
    RULE_tag_symbol = 11
    RULE_tag = 12
    RULE_area = 13
    RULE_context = 14
    RULE_person = 15
    RULE_project = 16
    RULE_link = 17
    RULE_h1_section = 18
    RULE_h2_section = 19
    RULE_h3_section = 20
    RULE_h4_section = 21
    RULE_h1_header = 22
    RULE_h2_header = 23
    RULE_h3_header = 24
    RULE_h4_header = 25

    ruleNames =  [ "prog", "head", "comment", "block", "item", "todo", "priority", 
                   "note", "space_atoms", "space_atom", "property", "tag_symbol", 
                   "tag", "area", "context", "person", "project", "link", 
                   "h1_section", "h2_section", "h3_section", "h4_section", 
                   "h1_header", "h2_header", "h3_header", "h4_header" ]

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
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    NL=18
    ID=19
    SYMBOL=20

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

        def head(self):
            return self.getTypedRuleContext(ZorgFileParser.HeadContext,0)


        def EOF(self):
            return self.getToken(ZorgFileParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.NL)
            else:
                return self.getToken(ZorgFileParser.NL, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.BlockContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.BlockContext,i)


        def h1_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.H1_sectionContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.H1_sectionContext,i)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ZorgFileParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.head()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 53
                    self.match(ZorgFileParser.NL)
                    self.state = 56 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==18):
                        break

                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2 or _la==6:
                    self.state = 58
                    self.block()
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 64
                    self.h1_section()
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 72
            self.match(ZorgFileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.CommentContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.CommentContext,i)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead" ):
                listener.enterHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead" ):
                listener.exitHead(self)




    def head(self):

        localctx = ZorgFileParser.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.comment()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = ZorgFileParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ZorgFileParser.T__0)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 80
                self.space_atoms()


            self.state = 83
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.ItemContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.ItemContext,i)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ZorgFileParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 85
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 88 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 90
                self.match(ZorgFileParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def todo(self):
            return self.getTypedRuleContext(ZorgFileParser.TodoContext,0)


        def note(self):
            return self.getTypedRuleContext(ZorgFileParser.NoteContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = ZorgFileParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 93
                self.todo()
                pass
            elif token in [6]:
                self.state = 94
                self.note()
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


    class TodoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def priority(self):
            return self.getTypedRuleContext(ZorgFileParser.PriorityContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_todo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo" ):
                listener.enterTodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo" ):
                listener.exitTodo(self)




    def todo(self):

        localctx = ZorgFileParser.TodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_todo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ZorgFileParser.T__1)
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 98
                self.match(ZorgFileParser.T__2)
                self.state = 99
                self.priority()


            self.state = 102
            self.space_atoms()
            self.state = 103
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PriorityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_priority

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPriority" ):
                listener.enterPriority(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPriority" ):
                listener.exitPriority(self)




    def priority(self):

        localctx = ZorgFileParser.PriorityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_priority)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ZorgFileParser.T__3)
            self.state = 106
            self.match(ZorgFileParser.ID)
            self.state = 107
            self.match(ZorgFileParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = ZorgFileParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_note)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ZorgFileParser.T__5)
            self.state = 110
            self.space_atoms()
            self.state = 111
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Space_atomsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Space_atomContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Space_atomContext,i)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_space_atoms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpace_atoms" ):
                listener.enterSpace_atoms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpace_atoms" ):
                listener.exitSpace_atoms(self)




    def space_atoms(self):

        localctx = ZorgFileParser.Space_atomsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_space_atoms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 113
                self.space_atom()
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Space_atomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag(self):
            return self.getTypedRuleContext(ZorgFileParser.TagContext,0)


        def tag_symbol(self):
            return self.getTypedRuleContext(ZorgFileParser.Tag_symbolContext,0)


        def link(self):
            return self.getTypedRuleContext(ZorgFileParser.LinkContext,0)


        def property_(self):
            return self.getTypedRuleContext(ZorgFileParser.PropertyContext,0)


        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SYMBOL)
            else:
                return self.getToken(ZorgFileParser.SYMBOL, i)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_space_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpace_atom" ):
                listener.enterSpace_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpace_atom" ):
                listener.exitSpace_atom(self)




    def space_atom(self):

        localctx = ZorgFileParser.Space_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_space_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ZorgFileParser.T__2)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 119
                self.match(ZorgFileParser.T__6)


            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 122
                self.tag()

            elif la_ == 2:
                self.state = 123
                self.tag_symbol()

            elif la_ == 3:
                self.state = 124
                self.link()

            elif la_ == 4:
                self.state = 125
                self.property_()

            elif la_ == 5:
                self.state = 126
                self.match(ZorgFileParser.ID)


            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 129
                self.match(ZorgFileParser.SYMBOL)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.ID)
            else:
                return self.getToken(ZorgFileParser.ID, i)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProperty" ):
                listener.enterProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProperty" ):
                listener.exitProperty(self)




    def property_(self):

        localctx = ZorgFileParser.PropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ZorgFileParser.ID)
            self.state = 136
            self.match(ZorgFileParser.T__7)
            self.state = 137
            self.match(ZorgFileParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZorgFileParser.RULE_tag_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_symbol" ):
                listener.enterTag_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_symbol" ):
                listener.exitTag_symbol(self)




    def tag_symbol(self):

        localctx = ZorgFileParser.Tag_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tag_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3586) != 0)):
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


    class TagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def area(self):
            return self.getTypedRuleContext(ZorgFileParser.AreaContext,0)


        def context(self):
            return self.getTypedRuleContext(ZorgFileParser.ContextContext,0)


        def person(self):
            return self.getTypedRuleContext(ZorgFileParser.PersonContext,0)


        def project(self):
            return self.getTypedRuleContext(ZorgFileParser.ProjectContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)




    def tag(self):

        localctx = ZorgFileParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 141
                self.area()
                pass
            elif token in [9]:
                self.state = 142
                self.context()
                pass
            elif token in [10]:
                self.state = 143
                self.person()
                pass
            elif token in [11]:
                self.state = 144
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

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_area

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArea" ):
                listener.enterArea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArea" ):
                listener.exitArea(self)




    def area(self):

        localctx = ZorgFileParser.AreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ZorgFileParser.T__0)
            self.state = 148
            self.match(ZorgFileParser.ID)
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

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_context

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContext" ):
                listener.enterContext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContext" ):
                listener.exitContext(self)




    def context(self):

        localctx = ZorgFileParser.ContextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ZorgFileParser.T__8)
            self.state = 151
            self.match(ZorgFileParser.ID)
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

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_person

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPerson" ):
                listener.enterPerson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPerson" ):
                listener.exitPerson(self)




    def person(self):

        localctx = ZorgFileParser.PersonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ZorgFileParser.T__9)
            self.state = 154
            self.match(ZorgFileParser.ID)
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

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_project

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProject" ):
                listener.enterProject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProject" ):
                listener.exitProject(self)




    def project(self):

        localctx = ZorgFileParser.ProjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ZorgFileParser.T__10)
            self.state = 157
            self.match(ZorgFileParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def property_(self):
            return self.getTypedRuleContext(ZorgFileParser.PropertyContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)




    def link(self):

        localctx = ZorgFileParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ZorgFileParser.T__11)
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(ZorgFileParser.ID)
                pass

            elif la_ == 2:
                self.state = 161
                self.property_()
                pass


            self.state = 164
            self.match(ZorgFileParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class H1_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h1_header(self):
            return self.getTypedRuleContext(ZorgFileParser.H1_headerContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.BlockContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.BlockContext,i)


        def h2_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.H2_sectionContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.H2_sectionContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.NL)
            else:
                return self.getToken(ZorgFileParser.NL, i)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_h1_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH1_section" ):
                listener.enterH1_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH1_section" ):
                listener.exitH1_section(self)




    def h1_section(self):

        localctx = ZorgFileParser.H1_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_h1_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.h1_header()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 167
                self.block()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==18:
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 173
                    self.match(ZorgFileParser.NL)


                self.state = 176
                self.h2_section()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class H2_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h2_header(self):
            return self.getTypedRuleContext(ZorgFileParser.H2_headerContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.BlockContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.BlockContext,i)


        def h3_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.H3_sectionContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.H3_sectionContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.NL)
            else:
                return self.getToken(ZorgFileParser.NL, i)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_h2_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH2_section" ):
                listener.enterH2_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH2_section" ):
                listener.exitH2_section(self)




    def h2_section(self):

        localctx = ZorgFileParser.H2_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_h2_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.h2_header()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 183
                self.block()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 190
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==18:
                        self.state = 189
                        self.match(ZorgFileParser.NL)


                    self.state = 192
                    self.h3_section() 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class H3_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h3_header(self):
            return self.getTypedRuleContext(ZorgFileParser.H3_headerContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.BlockContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.BlockContext,i)


        def h4_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.H4_sectionContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.H4_sectionContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.NL)
            else:
                return self.getToken(ZorgFileParser.NL, i)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_h3_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH3_section" ):
                listener.enterH3_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH3_section" ):
                listener.exitH3_section(self)




    def h3_section(self):

        localctx = ZorgFileParser.H3_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_h3_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.h3_header()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 199
                self.block()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==18:
                        self.state = 205
                        self.match(ZorgFileParser.NL)


                    self.state = 208
                    self.h4_section() 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class H4_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h4_header(self):
            return self.getTypedRuleContext(ZorgFileParser.H4_headerContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.BlockContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.BlockContext,i)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_h4_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH4_section" ):
                listener.enterH4_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH4_section" ):
                listener.exitH4_section(self)




    def h4_section(self):

        localctx = ZorgFileParser.H4_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_h4_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.h4_header()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 215
                self.block()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class H1_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_h1_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH1_header" ):
                listener.enterH1_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH1_header" ):
                listener.exitH1_header(self)




    def h1_header(self):

        localctx = ZorgFileParser.H1_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_h1_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ZorgFileParser.T__13)
            self.state = 222
            self.space_atoms()
            self.state = 223
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class H2_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_h2_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH2_header" ):
                listener.enterH2_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH2_header" ):
                listener.exitH2_header(self)




    def h2_header(self):

        localctx = ZorgFileParser.H2_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_h2_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(ZorgFileParser.T__14)
            self.state = 226
            self.space_atoms()
            self.state = 227
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class H3_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_h3_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH3_header" ):
                listener.enterH3_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH3_header" ):
                listener.exitH3_header(self)




    def h3_header(self):

        localctx = ZorgFileParser.H3_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_h3_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ZorgFileParser.T__15)
            self.state = 230
            self.space_atoms()
            self.state = 231
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class H4_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_h4_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH4_header" ):
                listener.enterH4_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH4_header" ):
                listener.exitH4_header(self)




    def h4_header(self):

        localctx = ZorgFileParser.H4_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_h4_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ZorgFileParser.T__16)
            self.state = 234
            self.space_atoms()
            self.state = 235
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





