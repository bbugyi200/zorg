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
        4,1,21,254,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,4,0,59,8,0,11,0,12,0,60,1,0,5,0,64,8,0,10,0,12,
        0,67,9,0,1,0,5,0,70,8,0,10,0,12,0,73,9,0,3,0,75,8,0,1,0,1,0,1,1,
        4,1,80,8,1,11,1,12,1,81,1,2,1,2,3,2,86,8,2,1,2,1,2,1,3,4,3,91,8,
        3,11,3,12,3,92,1,3,3,3,96,8,3,1,4,1,4,3,4,100,8,4,1,5,1,5,1,5,3,
        5,105,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,4,8,119,
        8,8,11,8,12,8,120,1,9,1,9,3,9,125,8,9,1,9,1,9,3,9,129,8,9,1,9,5,
        9,132,8,9,10,9,12,9,135,9,9,1,10,1,10,1,10,1,10,1,10,3,10,142,8,
        10,1,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,3,13,154,8,
        13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,
        18,1,18,4,18,170,8,18,11,18,12,18,171,1,18,1,18,1,19,1,19,1,19,3,
        19,179,8,19,1,19,1,19,1,20,1,20,5,20,185,8,20,10,20,12,20,188,9,
        20,1,20,3,20,191,8,20,1,20,5,20,194,8,20,10,20,12,20,197,9,20,1,
        21,1,21,5,21,201,8,21,10,21,12,21,204,9,21,1,21,3,21,207,8,21,1,
        21,5,21,210,8,21,10,21,12,21,213,9,21,1,22,1,22,5,22,217,8,22,10,
        22,12,22,220,9,22,1,22,3,22,223,8,22,1,22,5,22,226,8,22,10,22,12,
        22,229,9,22,1,23,1,23,5,23,233,8,23,10,23,12,23,236,9,23,1,24,1,
        24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,
        27,1,27,1,27,0,0,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,0,1,2,0,1,1,9,11,259,0,56,1,0,0,
        0,2,79,1,0,0,0,4,83,1,0,0,0,6,90,1,0,0,0,8,99,1,0,0,0,10,101,1,0,
        0,0,12,109,1,0,0,0,14,113,1,0,0,0,16,118,1,0,0,0,18,122,1,0,0,0,
        20,141,1,0,0,0,22,143,1,0,0,0,24,147,1,0,0,0,26,153,1,0,0,0,28,155,
        1,0,0,0,30,158,1,0,0,0,32,161,1,0,0,0,34,164,1,0,0,0,36,167,1,0,
        0,0,38,175,1,0,0,0,40,182,1,0,0,0,42,198,1,0,0,0,44,214,1,0,0,0,
        46,230,1,0,0,0,48,237,1,0,0,0,50,241,1,0,0,0,52,245,1,0,0,0,54,249,
        1,0,0,0,56,74,3,2,1,0,57,59,5,19,0,0,58,57,1,0,0,0,59,60,1,0,0,0,
        60,58,1,0,0,0,60,61,1,0,0,0,61,65,1,0,0,0,62,64,3,6,3,0,63,62,1,
        0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,71,1,0,0,0,67,
        65,1,0,0,0,68,70,3,40,20,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,
        0,0,71,72,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,74,58,1,0,0,0,74,75,
        1,0,0,0,75,76,1,0,0,0,76,77,5,0,0,1,77,1,1,0,0,0,78,80,3,4,2,0,79,
        78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,3,1,0,0,
        0,83,85,5,1,0,0,84,86,3,16,8,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,
        1,0,0,0,87,88,5,19,0,0,88,5,1,0,0,0,89,91,3,8,4,0,90,89,1,0,0,0,
        91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,96,5,
        19,0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,7,1,0,0,0,97,100,3,10,5,0,
        98,100,3,14,7,0,99,97,1,0,0,0,99,98,1,0,0,0,100,9,1,0,0,0,101,104,
        5,2,0,0,102,103,5,3,0,0,103,105,3,12,6,0,104,102,1,0,0,0,104,105,
        1,0,0,0,105,106,1,0,0,0,106,107,3,16,8,0,107,108,5,19,0,0,108,11,
        1,0,0,0,109,110,5,4,0,0,110,111,5,20,0,0,111,112,5,5,0,0,112,13,
        1,0,0,0,113,114,5,6,0,0,114,115,3,16,8,0,115,116,5,19,0,0,116,15,
        1,0,0,0,117,119,3,18,9,0,118,117,1,0,0,0,119,120,1,0,0,0,120,118,
        1,0,0,0,120,121,1,0,0,0,121,17,1,0,0,0,122,124,5,3,0,0,123,125,5,
        7,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,128,1,0,0,0,126,129,3,
        20,10,0,127,129,3,36,18,0,128,126,1,0,0,0,128,127,1,0,0,0,128,129,
        1,0,0,0,129,133,1,0,0,0,130,132,5,21,0,0,131,130,1,0,0,0,132,135,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,19,1,0,0,0,135,133,1,
        0,0,0,136,142,3,24,12,0,137,142,3,26,13,0,138,142,3,38,19,0,139,
        142,3,22,11,0,140,142,5,20,0,0,141,136,1,0,0,0,141,137,1,0,0,0,141,
        138,1,0,0,0,141,139,1,0,0,0,141,140,1,0,0,0,142,21,1,0,0,0,143,144,
        5,20,0,0,144,145,5,8,0,0,145,146,5,20,0,0,146,23,1,0,0,0,147,148,
        7,0,0,0,148,25,1,0,0,0,149,154,3,28,14,0,150,154,3,30,15,0,151,154,
        3,32,16,0,152,154,3,34,17,0,153,149,1,0,0,0,153,150,1,0,0,0,153,
        151,1,0,0,0,153,152,1,0,0,0,154,27,1,0,0,0,155,156,5,1,0,0,156,157,
        5,20,0,0,157,29,1,0,0,0,158,159,5,9,0,0,159,160,5,20,0,0,160,31,
        1,0,0,0,161,162,5,10,0,0,162,163,5,20,0,0,163,33,1,0,0,0,164,165,
        5,11,0,0,165,166,5,20,0,0,166,35,1,0,0,0,167,169,5,12,0,0,168,170,
        3,20,10,0,169,168,1,0,0,0,170,171,1,0,0,0,171,169,1,0,0,0,171,172,
        1,0,0,0,172,173,1,0,0,0,173,174,5,12,0,0,174,37,1,0,0,0,175,178,
        5,13,0,0,176,179,5,20,0,0,177,179,3,22,11,0,178,176,1,0,0,0,178,
        177,1,0,0,0,179,180,1,0,0,0,180,181,5,14,0,0,181,39,1,0,0,0,182,
        186,3,48,24,0,183,185,3,6,3,0,184,183,1,0,0,0,185,188,1,0,0,0,186,
        184,1,0,0,0,186,187,1,0,0,0,187,195,1,0,0,0,188,186,1,0,0,0,189,
        191,5,19,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,
        194,3,42,21,0,193,190,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,
        196,1,0,0,0,196,41,1,0,0,0,197,195,1,0,0,0,198,202,3,50,25,0,199,
        201,3,6,3,0,200,199,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,
        203,1,0,0,0,203,211,1,0,0,0,204,202,1,0,0,0,205,207,5,19,0,0,206,
        205,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,210,3,44,22,0,209,
        206,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,
        43,1,0,0,0,213,211,1,0,0,0,214,218,3,52,26,0,215,217,3,6,3,0,216,
        215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,
        227,1,0,0,0,220,218,1,0,0,0,221,223,5,19,0,0,222,221,1,0,0,0,222,
        223,1,0,0,0,223,224,1,0,0,0,224,226,3,46,23,0,225,222,1,0,0,0,226,
        229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,45,1,0,0,0,229,227,
        1,0,0,0,230,234,3,54,27,0,231,233,3,6,3,0,232,231,1,0,0,0,233,236,
        1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,47,1,0,0,0,236,234,1,
        0,0,0,237,238,5,15,0,0,238,239,3,16,8,0,239,240,5,19,0,0,240,49,
        1,0,0,0,241,242,5,16,0,0,242,243,3,16,8,0,243,244,5,19,0,0,244,51,
        1,0,0,0,245,246,5,17,0,0,246,247,3,16,8,0,247,248,5,19,0,0,248,53,
        1,0,0,0,249,250,5,18,0,0,250,251,3,16,8,0,251,252,5,19,0,0,252,55,
        1,0,0,0,28,60,65,71,74,81,85,92,95,99,104,120,124,128,133,141,153,
        171,178,186,190,195,202,206,211,218,222,227,234
    ]

class ZorgFileParser ( Parser ):

    grammarFileName = "ZorgFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'o'", "' '", "'[#'", "']'", "'-'", 
                     "'('", "'::'", "'@'", "'%'", "'+'", "'''", "'[['", 
                     "']]'", "'#########'", "'======='", "'*****'", "'---'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NL", "ID", 
                      "SYMBOL" ]

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
    RULE_atom = 10
    RULE_property = 11
    RULE_tag_symbol = 12
    RULE_tag = 13
    RULE_area = 14
    RULE_context = 15
    RULE_person = 16
    RULE_project = 17
    RULE_quoted = 18
    RULE_link = 19
    RULE_h1_section = 20
    RULE_h2_section = 21
    RULE_h3_section = 22
    RULE_h4_section = 23
    RULE_h1_header = 24
    RULE_h2_header = 25
    RULE_h3_header = 26
    RULE_h4_header = 27

    ruleNames =  [ "prog", "head", "comment", "block", "item", "todo", "priority", 
                   "note", "space_atoms", "space_atom", "atom", "property", 
                   "tag_symbol", "tag", "area", "context", "person", "project", 
                   "quoted", "link", "h1_section", "h2_section", "h3_section", 
                   "h4_section", "h1_header", "h2_header", "h3_header", 
                   "h4_header" ]

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
    T__17=18
    NL=19
    ID=20
    SYMBOL=21

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
            self.state = 56
            self.head()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 57
                    self.match(ZorgFileParser.NL)
                    self.state = 60 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==19):
                        break

                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2 or _la==6:
                    self.state = 62
                    self.block()
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 68
                    self.h1_section()
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 76
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
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.comment()
                self.state = 81 
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
            self.state = 83
            self.match(ZorgFileParser.T__0)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 84
                self.space_atoms()


            self.state = 87
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
            self.state = 90 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 89
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 92 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 94
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
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 97
                self.todo()
                pass
            elif token in [6]:
                self.state = 98
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
            self.state = 101
            self.match(ZorgFileParser.T__1)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 102
                self.match(ZorgFileParser.T__2)
                self.state = 103
                self.priority()


            self.state = 106
            self.space_atoms()
            self.state = 107
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
            self.state = 109
            self.match(ZorgFileParser.T__3)
            self.state = 110
            self.match(ZorgFileParser.ID)
            self.state = 111
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
            self.state = 113
            self.match(ZorgFileParser.T__5)
            self.state = 114
            self.space_atoms()
            self.state = 115
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
            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.space_atom()
                self.state = 120 
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

        def atom(self):
            return self.getTypedRuleContext(ZorgFileParser.AtomContext,0)


        def quoted(self):
            return self.getTypedRuleContext(ZorgFileParser.QuotedContext,0)


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
            self.state = 122
            self.match(ZorgFileParser.T__2)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 123
                self.match(ZorgFileParser.T__6)


            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 9, 10, 11, 13, 20]:
                self.state = 126
                self.atom()
                pass
            elif token in [12]:
                self.state = 127
                self.quoted()
                pass
            elif token in [3, 19, 21]:
                pass
            else:
                pass
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 130
                self.match(ZorgFileParser.SYMBOL)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_symbol(self):
            return self.getTypedRuleContext(ZorgFileParser.Tag_symbolContext,0)


        def tag(self):
            return self.getTypedRuleContext(ZorgFileParser.TagContext,0)


        def link(self):
            return self.getTypedRuleContext(ZorgFileParser.LinkContext,0)


        def property_(self):
            return self.getTypedRuleContext(ZorgFileParser.PropertyContext,0)


        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = ZorgFileParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 136
                self.tag_symbol()
                pass

            elif la_ == 2:
                self.state = 137
                self.tag()
                pass

            elif la_ == 3:
                self.state = 138
                self.link()
                pass

            elif la_ == 4:
                self.state = 139
                self.property_()
                pass

            elif la_ == 5:
                self.state = 140
                self.match(ZorgFileParser.ID)
                pass


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
        self.enterRule(localctx, 22, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ZorgFileParser.ID)
            self.state = 144
            self.match(ZorgFileParser.T__7)
            self.state = 145
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
        self.enterRule(localctx, 24, self.RULE_tag_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
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
        self.enterRule(localctx, 26, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 149
                self.area()
                pass
            elif token in [9]:
                self.state = 150
                self.context()
                pass
            elif token in [10]:
                self.state = 151
                self.person()
                pass
            elif token in [11]:
                self.state = 152
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
        self.enterRule(localctx, 28, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(ZorgFileParser.T__0)
            self.state = 156
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
        self.enterRule(localctx, 30, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ZorgFileParser.T__8)
            self.state = 159
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
        self.enterRule(localctx, 32, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ZorgFileParser.T__9)
            self.state = 162
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
        self.enterRule(localctx, 34, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ZorgFileParser.T__10)
            self.state = 165
            self.match(ZorgFileParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.AtomContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.AtomContext,i)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)




    def quoted(self):

        localctx = ZorgFileParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(ZorgFileParser.T__11)
            self.state = 169 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 168
                self.atom()
                self.state = 171 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1060354) != 0)):
                    break

            self.state = 173
            self.match(ZorgFileParser.T__11)
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
        self.enterRule(localctx, 38, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(ZorgFileParser.T__12)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 176
                self.match(ZorgFileParser.ID)
                pass

            elif la_ == 2:
                self.state = 177
                self.property_()
                pass


            self.state = 180
            self.match(ZorgFileParser.T__13)
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
        self.enterRule(localctx, 40, self.RULE_h1_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.h1_header()
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
            _la = self._input.LA(1)
            while _la==16 or _la==19:
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 189
                    self.match(ZorgFileParser.NL)


                self.state = 192
                self.h2_section()
                self.state = 197
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
        self.enterRule(localctx, 42, self.RULE_h2_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.h2_header()
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
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==19:
                        self.state = 205
                        self.match(ZorgFileParser.NL)


                    self.state = 208
                    self.h3_section() 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_h3_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.h3_header()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 215
                self.block()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==19:
                        self.state = 221
                        self.match(ZorgFileParser.NL)


                    self.state = 224
                    self.h4_section() 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_h4_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.h4_header()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 231
                self.block()
                self.state = 236
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
        self.enterRule(localctx, 48, self.RULE_h1_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(ZorgFileParser.T__14)
            self.state = 238
            self.space_atoms()
            self.state = 239
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
        self.enterRule(localctx, 50, self.RULE_h2_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZorgFileParser.T__15)
            self.state = 242
            self.space_atoms()
            self.state = 243
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
        self.enterRule(localctx, 52, self.RULE_h3_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ZorgFileParser.T__16)
            self.state = 246
            self.space_atoms()
            self.state = 247
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
        self.enterRule(localctx, 54, self.RULE_h4_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ZorgFileParser.T__17)
            self.state = 250
            self.space_atoms()
            self.state = 251
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





