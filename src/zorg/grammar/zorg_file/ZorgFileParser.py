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
        4,1,27,309,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,4,0,65,8,0,11,0,
        12,0,66,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,5,0,76,8,0,10,0,12,0,
        79,9,0,3,0,81,8,0,1,0,1,0,1,1,4,1,86,8,1,11,1,12,1,87,1,2,1,2,3,
        2,92,8,2,1,2,1,2,1,3,4,3,97,8,3,11,3,12,3,98,1,3,3,3,102,8,3,1,4,
        1,4,3,4,106,8,4,1,5,1,5,5,5,110,8,5,10,5,12,5,113,9,5,1,5,1,5,1,
        5,3,5,118,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,5,7,129,8,7,10,
        7,12,7,132,9,7,1,7,1,7,1,7,1,7,1,8,4,8,139,8,8,11,8,12,8,140,1,9,
        1,9,3,9,145,8,9,1,9,1,9,3,9,149,8,9,1,9,5,9,152,8,9,10,9,12,9,155,
        9,9,1,9,3,9,158,8,9,1,10,1,10,1,10,1,10,1,10,3,10,165,8,10,1,11,
        1,11,1,11,1,11,1,12,1,12,4,12,173,8,12,11,12,12,12,174,1,12,1,12,
        5,12,179,8,12,10,12,12,12,182,9,12,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,3,14,191,8,14,1,15,1,15,1,16,1,16,1,16,1,16,3,16,199,8,16,1,
        17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,
        21,4,21,215,8,21,11,21,12,21,216,1,21,1,21,1,21,1,21,4,21,223,8,
        21,11,21,12,21,224,1,21,1,21,3,21,229,8,21,1,22,1,22,1,22,3,22,234,
        8,22,1,22,1,22,1,23,1,23,5,23,240,8,23,10,23,12,23,243,9,23,1,23,
        3,23,246,8,23,1,23,5,23,249,8,23,10,23,12,23,252,9,23,1,24,1,24,
        5,24,256,8,24,10,24,12,24,259,9,24,1,24,3,24,262,8,24,1,24,5,24,
        265,8,24,10,24,12,24,268,9,24,1,25,1,25,5,25,272,8,25,10,25,12,25,
        275,9,25,1,25,3,25,278,8,25,1,25,5,25,281,8,25,10,25,12,25,284,9,
        25,1,26,1,26,5,26,288,8,26,10,26,12,26,291,9,26,1,27,1,27,1,27,1,
        27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,
        30,0,0,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,0,2,1,0,20,24,2,0,1,1,6,8,322,0,
        62,1,0,0,0,2,85,1,0,0,0,4,89,1,0,0,0,6,96,1,0,0,0,8,105,1,0,0,0,
        10,111,1,0,0,0,12,122,1,0,0,0,14,130,1,0,0,0,16,138,1,0,0,0,18,142,
        1,0,0,0,20,164,1,0,0,0,22,166,1,0,0,0,24,170,1,0,0,0,26,183,1,0,
        0,0,28,190,1,0,0,0,30,192,1,0,0,0,32,198,1,0,0,0,34,200,1,0,0,0,
        36,203,1,0,0,0,38,206,1,0,0,0,40,209,1,0,0,0,42,228,1,0,0,0,44,230,
        1,0,0,0,46,237,1,0,0,0,48,253,1,0,0,0,50,269,1,0,0,0,52,285,1,0,
        0,0,54,292,1,0,0,0,56,296,1,0,0,0,58,300,1,0,0,0,60,304,1,0,0,0,
        62,80,3,2,1,0,63,65,5,17,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,
        0,0,0,66,67,1,0,0,0,67,71,1,0,0,0,68,70,3,6,3,0,69,68,1,0,0,0,70,
        73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,77,1,0,0,0,73,71,1,0,0,
        0,74,76,3,46,23,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,
        1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,80,64,1,0,0,0,80,81,1,0,0,0,
        81,82,1,0,0,0,82,83,5,0,0,1,83,1,1,0,0,0,84,86,3,4,2,0,85,84,1,0,
        0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,3,1,0,0,0,89,91,
        5,1,0,0,90,92,3,16,8,0,91,90,1,0,0,0,91,92,1,0,0,0,92,93,1,0,0,0,
        93,94,5,17,0,0,94,5,1,0,0,0,95,97,3,8,4,0,96,95,1,0,0,0,97,98,1,
        0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,102,5,17,0,
        0,101,100,1,0,0,0,101,102,1,0,0,0,102,7,1,0,0,0,103,106,3,10,5,0,
        104,106,3,14,7,0,105,103,1,0,0,0,105,104,1,0,0,0,106,9,1,0,0,0,107,
        108,5,25,0,0,108,110,5,25,0,0,109,107,1,0,0,0,110,113,1,0,0,0,111,
        109,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,
        117,5,2,0,0,115,116,5,25,0,0,116,118,3,12,6,0,117,115,1,0,0,0,117,
        118,1,0,0,0,118,119,1,0,0,0,119,120,3,16,8,0,120,121,5,17,0,0,121,
        11,1,0,0,0,122,123,5,3,0,0,123,124,5,18,0,0,124,125,5,4,0,0,125,
        13,1,0,0,0,126,127,5,25,0,0,127,129,5,25,0,0,128,126,1,0,0,0,129,
        132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,
        130,1,0,0,0,133,134,5,20,0,0,134,135,3,16,8,0,135,136,5,17,0,0,136,
        15,1,0,0,0,137,139,3,18,9,0,138,137,1,0,0,0,139,140,1,0,0,0,140,
        138,1,0,0,0,140,141,1,0,0,0,141,17,1,0,0,0,142,144,5,25,0,0,143,
        145,5,26,0,0,144,143,1,0,0,0,144,145,1,0,0,0,145,148,1,0,0,0,146,
        149,3,20,10,0,147,149,3,42,21,0,148,146,1,0,0,0,148,147,1,0,0,0,
        148,149,1,0,0,0,149,153,1,0,0,0,150,152,3,28,14,0,151,150,1,0,0,
        0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,157,1,0,0,
        0,155,153,1,0,0,0,156,158,5,27,0,0,157,156,1,0,0,0,157,158,1,0,0,
        0,158,19,1,0,0,0,159,165,3,30,15,0,160,165,3,32,16,0,161,165,3,44,
        22,0,162,165,3,22,11,0,163,165,3,24,12,0,164,159,1,0,0,0,164,160,
        1,0,0,0,164,161,1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,21,1,
        0,0,0,166,167,5,18,0,0,167,168,5,5,0,0,168,169,3,24,12,0,169,23,
        1,0,0,0,170,180,5,18,0,0,171,173,3,26,13,0,172,171,1,0,0,0,173,174,
        1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,
        5,18,0,0,177,179,1,0,0,0,178,172,1,0,0,0,179,182,1,0,0,0,180,178,
        1,0,0,0,180,181,1,0,0,0,181,25,1,0,0,0,182,180,1,0,0,0,183,184,7,
        0,0,0,184,27,1,0,0,0,185,191,5,19,0,0,186,191,5,26,0,0,187,191,5,
        27,0,0,188,191,3,26,13,0,189,191,3,30,15,0,190,185,1,0,0,0,190,186,
        1,0,0,0,190,187,1,0,0,0,190,188,1,0,0,0,190,189,1,0,0,0,191,29,1,
        0,0,0,192,193,7,1,0,0,193,31,1,0,0,0,194,199,3,34,17,0,195,199,3,
        36,18,0,196,199,3,38,19,0,197,199,3,40,20,0,198,194,1,0,0,0,198,
        195,1,0,0,0,198,196,1,0,0,0,198,197,1,0,0,0,199,33,1,0,0,0,200,201,
        5,1,0,0,201,202,5,18,0,0,202,35,1,0,0,0,203,204,5,6,0,0,204,205,
        5,18,0,0,205,37,1,0,0,0,206,207,5,7,0,0,207,208,5,18,0,0,208,39,
        1,0,0,0,209,210,5,8,0,0,210,211,5,18,0,0,211,41,1,0,0,0,212,214,
        5,9,0,0,213,215,3,20,10,0,214,213,1,0,0,0,215,216,1,0,0,0,216,214,
        1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,219,5,9,0,0,219,229,
        1,0,0,0,220,222,5,10,0,0,221,223,3,20,10,0,222,221,1,0,0,0,223,224,
        1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,227,
        5,10,0,0,227,229,1,0,0,0,228,212,1,0,0,0,228,220,1,0,0,0,229,43,
        1,0,0,0,230,233,5,11,0,0,231,234,3,24,12,0,232,234,3,22,11,0,233,
        231,1,0,0,0,233,232,1,0,0,0,234,235,1,0,0,0,235,236,5,12,0,0,236,
        45,1,0,0,0,237,241,3,54,27,0,238,240,3,6,3,0,239,238,1,0,0,0,240,
        243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,250,1,0,0,0,243,
        241,1,0,0,0,244,246,5,17,0,0,245,244,1,0,0,0,245,246,1,0,0,0,246,
        247,1,0,0,0,247,249,3,48,24,0,248,245,1,0,0,0,249,252,1,0,0,0,250,
        248,1,0,0,0,250,251,1,0,0,0,251,47,1,0,0,0,252,250,1,0,0,0,253,257,
        3,56,28,0,254,256,3,6,3,0,255,254,1,0,0,0,256,259,1,0,0,0,257,255,
        1,0,0,0,257,258,1,0,0,0,258,266,1,0,0,0,259,257,1,0,0,0,260,262,
        5,17,0,0,261,260,1,0,0,0,261,262,1,0,0,0,262,263,1,0,0,0,263,265,
        3,50,25,0,264,261,1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,
        1,0,0,0,267,49,1,0,0,0,268,266,1,0,0,0,269,273,3,58,29,0,270,272,
        3,6,3,0,271,270,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,
        1,0,0,0,274,282,1,0,0,0,275,273,1,0,0,0,276,278,5,17,0,0,277,276,
        1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,281,3,52,26,0,280,277,
        1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,51,1,
        0,0,0,284,282,1,0,0,0,285,289,3,60,30,0,286,288,3,6,3,0,287,286,
        1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,53,1,
        0,0,0,291,289,1,0,0,0,292,293,5,13,0,0,293,294,3,16,8,0,294,295,
        5,17,0,0,295,55,1,0,0,0,296,297,5,14,0,0,297,298,3,16,8,0,298,299,
        5,17,0,0,299,57,1,0,0,0,300,301,5,15,0,0,301,302,3,16,8,0,302,303,
        5,17,0,0,303,59,1,0,0,0,304,305,5,16,0,0,305,306,3,16,8,0,306,307,
        5,17,0,0,307,61,1,0,0,0,36,66,71,77,80,87,91,98,101,105,111,117,
        130,140,144,148,153,157,164,174,180,190,198,216,224,228,233,241,
        245,250,257,261,266,273,277,282,289
    ]

class ZorgFileParser ( Parser ):

    grammarFileName = "ZorgFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'o'", "'[#'", "']'", "'::'", "'@'", 
                     "'%'", "'+'", "'''", "'\"'", "'[['", "']]'", "'#########'", 
                     "'======='", "'*****'", "'---'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'-'", "'.'", "'/'", "'_'", "':'", "' '", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NL", "ID", "SYMBOL", "DASH", "DOT", 
                      "FSLASH", "UNDERSCORE", "COLON", "SPACE", "LPAREN", 
                      "RPAREN" ]

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
    RULE_id_group = 12
    RULE_id_symbol = 13
    RULE_any_symbol = 14
    RULE_tag_symbol = 15
    RULE_tag = 16
    RULE_area = 17
    RULE_context = 18
    RULE_person = 19
    RULE_project = 20
    RULE_quoted = 21
    RULE_link = 22
    RULE_h1_section = 23
    RULE_h2_section = 24
    RULE_h3_section = 25
    RULE_h4_section = 26
    RULE_h1_header = 27
    RULE_h2_header = 28
    RULE_h3_header = 29
    RULE_h4_header = 30

    ruleNames =  [ "prog", "head", "comment", "block", "item", "todo", "priority", 
                   "note", "space_atoms", "space_atom", "atom", "property", 
                   "id_group", "id_symbol", "any_symbol", "tag_symbol", 
                   "tag", "area", "context", "person", "project", "quoted", 
                   "link", "h1_section", "h2_section", "h3_section", "h4_section", 
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
    NL=17
    ID=18
    SYMBOL=19
    DASH=20
    DOT=21
    FSLASH=22
    UNDERSCORE=23
    COLON=24
    SPACE=25
    LPAREN=26
    RPAREN=27

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
            self.state = 62
            self.head()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 63
                    self.match(ZorgFileParser.NL)
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==17):
                        break

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                    self.state = 68
                    self.block()
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 74
                    self.h1_section()
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 82
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
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.comment()
                self.state = 87 
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
            self.state = 89
            self.match(ZorgFileParser.T__0)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 90
                self.space_atoms()


            self.state = 93
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
            self.state = 96 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 95
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 98 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 100
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
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 103
                self.todo()
                pass

            elif la_ == 2:
                self.state = 104
                self.note()
                pass


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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SPACE)
            else:
                return self.getToken(ZorgFileParser.SPACE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 107
                self.match(ZorgFileParser.SPACE)
                self.state = 108
                self.match(ZorgFileParser.SPACE)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(ZorgFileParser.T__1)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 115
                self.match(ZorgFileParser.SPACE)
                self.state = 116
                self.priority()


            self.state = 119
            self.space_atoms()
            self.state = 120
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
            self.state = 122
            self.match(ZorgFileParser.T__2)
            self.state = 123
            self.match(ZorgFileParser.ID)
            self.state = 124
            self.match(ZorgFileParser.T__3)
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

        def DASH(self):
            return self.getToken(ZorgFileParser.DASH, 0)

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SPACE)
            else:
                return self.getToken(ZorgFileParser.SPACE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 126
                self.match(ZorgFileParser.SPACE)
                self.state = 127
                self.match(ZorgFileParser.SPACE)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(ZorgFileParser.DASH)
            self.state = 134
            self.space_atoms()
            self.state = 135
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
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.space_atom()
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
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

        def SPACE(self):
            return self.getToken(ZorgFileParser.SPACE, 0)

        def LPAREN(self):
            return self.getToken(ZorgFileParser.LPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(ZorgFileParser.AtomContext,0)


        def quoted(self):
            return self.getTypedRuleContext(ZorgFileParser.QuotedContext,0)


        def any_symbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Any_symbolContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Any_symbolContext,i)


        def RPAREN(self):
            return self.getToken(ZorgFileParser.RPAREN, 0)

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
            self.state = 142
            self.match(ZorgFileParser.SPACE)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 143
                self.match(ZorgFileParser.LPAREN)


            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 146
                self.atom()

            elif la_ == 2:
                self.state = 147
                self.quoted()


            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 150
                    self.any_symbol() 
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 156
                self.match(ZorgFileParser.RPAREN)


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


        def id_group(self):
            return self.getTypedRuleContext(ZorgFileParser.Id_groupContext,0)


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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 159
                self.tag_symbol()
                pass

            elif la_ == 2:
                self.state = 160
                self.tag()
                pass

            elif la_ == 3:
                self.state = 161
                self.link()
                pass

            elif la_ == 4:
                self.state = 162
                self.property_()
                pass

            elif la_ == 5:
                self.state = 163
                self.id_group()
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

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def id_group(self):
            return self.getTypedRuleContext(ZorgFileParser.Id_groupContext,0)


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
            self.state = 166
            self.match(ZorgFileParser.ID)
            self.state = 167
            self.match(ZorgFileParser.T__4)
            self.state = 168
            self.id_group()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.ID)
            else:
                return self.getToken(ZorgFileParser.ID, i)

        def id_symbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Id_symbolContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Id_symbolContext,i)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_id_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_group" ):
                listener.enterId_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_group" ):
                listener.exitId_group(self)




    def id_group(self):

        localctx = ZorgFileParser.Id_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ZorgFileParser.ID)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 171
                        self.id_symbol()
                        self.state = 174 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0)):
                            break

                    self.state = 176
                    self.match(ZorgFileParser.ID) 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(ZorgFileParser.DASH, 0)

        def DOT(self):
            return self.getToken(ZorgFileParser.DOT, 0)

        def FSLASH(self):
            return self.getToken(ZorgFileParser.FSLASH, 0)

        def UNDERSCORE(self):
            return self.getToken(ZorgFileParser.UNDERSCORE, 0)

        def COLON(self):
            return self.getToken(ZorgFileParser.COLON, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_id_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_symbol" ):
                listener.enterId_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_symbol" ):
                listener.exitId_symbol(self)




    def id_symbol(self):

        localctx = ZorgFileParser.Id_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_id_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0)):
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


    class Any_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self):
            return self.getToken(ZorgFileParser.SYMBOL, 0)

        def LPAREN(self):
            return self.getToken(ZorgFileParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZorgFileParser.RPAREN, 0)

        def id_symbol(self):
            return self.getTypedRuleContext(ZorgFileParser.Id_symbolContext,0)


        def tag_symbol(self):
            return self.getTypedRuleContext(ZorgFileParser.Tag_symbolContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_any_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_symbol" ):
                listener.enterAny_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_symbol" ):
                listener.exitAny_symbol(self)




    def any_symbol(self):

        localctx = ZorgFileParser.Any_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_any_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 185
                self.match(ZorgFileParser.SYMBOL)
                pass
            elif token in [26]:
                self.state = 186
                self.match(ZorgFileParser.LPAREN)
                pass
            elif token in [27]:
                self.state = 187
                self.match(ZorgFileParser.RPAREN)
                pass
            elif token in [20, 21, 22, 23, 24]:
                self.state = 188
                self.id_symbol()
                pass
            elif token in [1, 6, 7, 8]:
                self.state = 189
                self.tag_symbol()
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
        self.enterRule(localctx, 30, self.RULE_tag_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 450) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 194
                self.area()
                pass
            elif token in [6]:
                self.state = 195
                self.context()
                pass
            elif token in [7]:
                self.state = 196
                self.person()
                pass
            elif token in [8]:
                self.state = 197
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
        self.enterRule(localctx, 34, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ZorgFileParser.T__0)
            self.state = 201
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
        self.enterRule(localctx, 36, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ZorgFileParser.T__5)
            self.state = 204
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
        self.enterRule(localctx, 38, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(ZorgFileParser.T__6)
            self.state = 207
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
        self.enterRule(localctx, 40, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(ZorgFileParser.T__7)
            self.state = 210
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
        self.enterRule(localctx, 42, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 212
                self.match(ZorgFileParser.T__8)
                self.state = 214 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 213
                    self.atom()
                    self.state = 216 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 264642) != 0)):
                        break

                self.state = 218
                self.match(ZorgFileParser.T__8)
                pass
            elif token in [10]:
                self.state = 220
                self.match(ZorgFileParser.T__9)
                self.state = 222 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 221
                    self.atom()
                    self.state = 224 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 264642) != 0)):
                        break

                self.state = 226
                self.match(ZorgFileParser.T__9)
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


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_group(self):
            return self.getTypedRuleContext(ZorgFileParser.Id_groupContext,0)


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
        self.enterRule(localctx, 44, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ZorgFileParser.T__10)
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 231
                self.id_group()
                pass

            elif la_ == 2:
                self.state = 232
                self.property_()
                pass


            self.state = 235
            self.match(ZorgFileParser.T__11)
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
        self.enterRule(localctx, 46, self.RULE_h1_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.h1_header()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                self.state = 238
                self.block()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==17:
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 244
                    self.match(ZorgFileParser.NL)


                self.state = 247
                self.h2_section()
                self.state = 252
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
        self.enterRule(localctx, 48, self.RULE_h2_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.h2_header()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                self.state = 254
                self.block()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 261
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 260
                        self.match(ZorgFileParser.NL)


                    self.state = 263
                    self.h3_section() 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_h3_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.h3_header()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                self.state = 270
                self.block()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 276
                        self.match(ZorgFileParser.NL)


                    self.state = 279
                    self.h4_section() 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 52, self.RULE_h4_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.h4_header()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                self.state = 286
                self.block()
                self.state = 291
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
        self.enterRule(localctx, 54, self.RULE_h1_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ZorgFileParser.T__12)
            self.state = 293
            self.space_atoms()
            self.state = 294
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
        self.enterRule(localctx, 56, self.RULE_h2_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(ZorgFileParser.T__13)
            self.state = 297
            self.space_atoms()
            self.state = 298
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
        self.enterRule(localctx, 58, self.RULE_h3_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZorgFileParser.T__14)
            self.state = 301
            self.space_atoms()
            self.state = 302
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
        self.enterRule(localctx, 60, self.RULE_h4_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ZorgFileParser.T__15)
            self.state = 305
            self.space_atoms()
            self.state = 306
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





