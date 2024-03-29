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
        4,1,27,316,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,4,0,65,8,0,11,0,
        12,0,66,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,5,0,76,8,0,10,0,12,0,
        79,9,0,1,0,5,0,82,8,0,10,0,12,0,85,9,0,3,0,87,8,0,1,0,1,0,1,1,4,
        1,92,8,1,11,1,12,1,93,1,2,1,2,3,2,98,8,2,1,2,1,2,1,3,4,3,103,8,3,
        11,3,12,3,104,1,3,3,3,108,8,3,1,4,1,4,3,4,112,8,4,1,5,1,5,5,5,116,
        8,5,10,5,12,5,119,9,5,1,5,1,5,1,5,3,5,124,8,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,7,1,7,5,7,135,8,7,10,7,12,7,138,9,7,1,7,1,7,1,7,1,7,
        1,8,4,8,145,8,8,11,8,12,8,146,1,9,1,9,3,9,151,8,9,1,9,1,9,3,9,155,
        8,9,1,9,5,9,158,8,9,10,9,12,9,161,9,9,1,9,3,9,164,8,9,1,10,1,10,
        1,10,1,10,1,10,3,10,171,8,10,1,11,1,11,1,11,1,11,1,12,1,12,4,12,
        179,8,12,11,12,12,12,180,1,12,1,12,5,12,185,8,12,10,12,12,12,188,
        9,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,198,8,14,1,15,
        1,15,1,16,1,16,1,16,1,16,3,16,206,8,16,1,17,1,17,1,17,1,18,1,18,
        1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,4,21,222,8,21,11,21,
        12,21,223,1,21,1,21,1,21,1,21,4,21,230,8,21,11,21,12,21,231,1,21,
        1,21,3,21,236,8,21,1,22,1,22,1,22,3,22,241,8,22,1,22,1,22,1,23,1,
        23,5,23,247,8,23,10,23,12,23,250,9,23,1,23,3,23,253,8,23,1,23,5,
        23,256,8,23,10,23,12,23,259,9,23,1,24,1,24,5,24,263,8,24,10,24,12,
        24,266,9,24,1,24,3,24,269,8,24,1,24,5,24,272,8,24,10,24,12,24,275,
        9,24,1,25,1,25,5,25,279,8,25,10,25,12,25,282,9,25,1,25,3,25,285,
        8,25,1,25,5,25,288,8,25,10,25,12,25,291,9,25,1,26,1,26,5,26,295,
        8,26,10,26,12,26,298,9,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,
        1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,0,0,31,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,0,2,2,0,20,22,24,24,2,0,1,1,6,8,331,0,62,1,0,0,0,2,91,1,
        0,0,0,4,95,1,0,0,0,6,102,1,0,0,0,8,111,1,0,0,0,10,117,1,0,0,0,12,
        128,1,0,0,0,14,136,1,0,0,0,16,144,1,0,0,0,18,148,1,0,0,0,20,170,
        1,0,0,0,22,172,1,0,0,0,24,176,1,0,0,0,26,189,1,0,0,0,28,197,1,0,
        0,0,30,199,1,0,0,0,32,205,1,0,0,0,34,207,1,0,0,0,36,210,1,0,0,0,
        38,213,1,0,0,0,40,216,1,0,0,0,42,235,1,0,0,0,44,237,1,0,0,0,46,244,
        1,0,0,0,48,260,1,0,0,0,50,276,1,0,0,0,52,292,1,0,0,0,54,299,1,0,
        0,0,56,303,1,0,0,0,58,307,1,0,0,0,60,311,1,0,0,0,62,86,3,2,1,0,63,
        65,5,17,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,
        0,0,67,71,1,0,0,0,68,70,3,6,3,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,
        1,0,0,0,71,72,1,0,0,0,72,77,1,0,0,0,73,71,1,0,0,0,74,76,3,48,24,
        0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,83,
        1,0,0,0,79,77,1,0,0,0,80,82,3,46,23,0,81,80,1,0,0,0,82,85,1,0,0,
        0,83,81,1,0,0,0,83,84,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,86,64,
        1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,89,5,0,0,1,89,1,1,0,0,0,90,
        92,3,4,2,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,
        0,94,3,1,0,0,0,95,97,5,1,0,0,96,98,3,16,8,0,97,96,1,0,0,0,97,98,
        1,0,0,0,98,99,1,0,0,0,99,100,5,17,0,0,100,5,1,0,0,0,101,103,3,8,
        4,0,102,101,1,0,0,0,103,104,1,0,0,0,104,102,1,0,0,0,104,105,1,0,
        0,0,105,107,1,0,0,0,106,108,5,17,0,0,107,106,1,0,0,0,107,108,1,0,
        0,0,108,7,1,0,0,0,109,112,3,10,5,0,110,112,3,14,7,0,111,109,1,0,
        0,0,111,110,1,0,0,0,112,9,1,0,0,0,113,114,5,25,0,0,114,116,5,25,
        0,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,
        0,0,118,120,1,0,0,0,119,117,1,0,0,0,120,123,5,2,0,0,121,122,5,25,
        0,0,122,124,3,12,6,0,123,121,1,0,0,0,123,124,1,0,0,0,124,125,1,0,
        0,0,125,126,3,16,8,0,126,127,5,17,0,0,127,11,1,0,0,0,128,129,5,3,
        0,0,129,130,5,18,0,0,130,131,5,4,0,0,131,13,1,0,0,0,132,133,5,25,
        0,0,133,135,5,25,0,0,134,132,1,0,0,0,135,138,1,0,0,0,136,134,1,0,
        0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,136,1,0,0,0,139,140,5,20,
        0,0,140,141,3,16,8,0,141,142,5,17,0,0,142,15,1,0,0,0,143,145,3,18,
        9,0,144,143,1,0,0,0,145,146,1,0,0,0,146,144,1,0,0,0,146,147,1,0,
        0,0,147,17,1,0,0,0,148,150,5,25,0,0,149,151,5,26,0,0,150,149,1,0,
        0,0,150,151,1,0,0,0,151,154,1,0,0,0,152,155,3,20,10,0,153,155,3,
        42,21,0,154,152,1,0,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,159,
        1,0,0,0,156,158,3,28,14,0,157,156,1,0,0,0,158,161,1,0,0,0,159,157,
        1,0,0,0,159,160,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,162,164,
        5,27,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,19,1,0,0,0,165,171,
        3,30,15,0,166,171,3,32,16,0,167,171,3,44,22,0,168,171,3,22,11,0,
        169,171,3,24,12,0,170,165,1,0,0,0,170,166,1,0,0,0,170,167,1,0,0,
        0,170,168,1,0,0,0,170,169,1,0,0,0,171,21,1,0,0,0,172,173,5,18,0,
        0,173,174,5,5,0,0,174,175,3,24,12,0,175,23,1,0,0,0,176,186,5,18,
        0,0,177,179,3,26,13,0,178,177,1,0,0,0,179,180,1,0,0,0,180,178,1,
        0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,5,18,0,0,183,185,1,
        0,0,0,184,178,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,
        0,0,0,187,25,1,0,0,0,188,186,1,0,0,0,189,190,7,0,0,0,190,27,1,0,
        0,0,191,198,5,19,0,0,192,198,5,26,0,0,193,198,5,27,0,0,194,198,5,
        23,0,0,195,198,3,26,13,0,196,198,3,30,15,0,197,191,1,0,0,0,197,192,
        1,0,0,0,197,193,1,0,0,0,197,194,1,0,0,0,197,195,1,0,0,0,197,196,
        1,0,0,0,198,29,1,0,0,0,199,200,7,1,0,0,200,31,1,0,0,0,201,206,3,
        34,17,0,202,206,3,36,18,0,203,206,3,38,19,0,204,206,3,40,20,0,205,
        201,1,0,0,0,205,202,1,0,0,0,205,203,1,0,0,0,205,204,1,0,0,0,206,
        33,1,0,0,0,207,208,5,1,0,0,208,209,5,18,0,0,209,35,1,0,0,0,210,211,
        5,6,0,0,211,212,5,18,0,0,212,37,1,0,0,0,213,214,5,7,0,0,214,215,
        5,18,0,0,215,39,1,0,0,0,216,217,5,8,0,0,217,218,5,18,0,0,218,41,
        1,0,0,0,219,221,5,9,0,0,220,222,3,20,10,0,221,220,1,0,0,0,222,223,
        1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,226,
        5,9,0,0,226,236,1,0,0,0,227,229,5,10,0,0,228,230,3,20,10,0,229,228,
        1,0,0,0,230,231,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,233,
        1,0,0,0,233,234,5,10,0,0,234,236,1,0,0,0,235,219,1,0,0,0,235,227,
        1,0,0,0,236,43,1,0,0,0,237,240,5,11,0,0,238,241,3,24,12,0,239,241,
        3,22,11,0,240,238,1,0,0,0,240,239,1,0,0,0,241,242,1,0,0,0,242,243,
        5,12,0,0,243,45,1,0,0,0,244,248,3,54,27,0,245,247,3,6,3,0,246,245,
        1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,257,
        1,0,0,0,250,248,1,0,0,0,251,253,5,17,0,0,252,251,1,0,0,0,252,253,
        1,0,0,0,253,254,1,0,0,0,254,256,3,48,24,0,255,252,1,0,0,0,256,259,
        1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,0,258,47,1,0,0,0,259,257,1,
        0,0,0,260,264,3,56,28,0,261,263,3,6,3,0,262,261,1,0,0,0,263,266,
        1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,273,1,0,0,0,266,264,
        1,0,0,0,267,269,5,17,0,0,268,267,1,0,0,0,268,269,1,0,0,0,269,270,
        1,0,0,0,270,272,3,50,25,0,271,268,1,0,0,0,272,275,1,0,0,0,273,271,
        1,0,0,0,273,274,1,0,0,0,274,49,1,0,0,0,275,273,1,0,0,0,276,280,3,
        58,29,0,277,279,3,6,3,0,278,277,1,0,0,0,279,282,1,0,0,0,280,278,
        1,0,0,0,280,281,1,0,0,0,281,289,1,0,0,0,282,280,1,0,0,0,283,285,
        5,17,0,0,284,283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,288,
        3,52,26,0,287,284,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,
        1,0,0,0,290,51,1,0,0,0,291,289,1,0,0,0,292,296,3,60,30,0,293,295,
        3,6,3,0,294,293,1,0,0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,
        1,0,0,0,297,53,1,0,0,0,298,296,1,0,0,0,299,300,5,13,0,0,300,301,
        3,16,8,0,301,302,5,17,0,0,302,55,1,0,0,0,303,304,5,14,0,0,304,305,
        3,16,8,0,305,306,5,17,0,0,306,57,1,0,0,0,307,308,5,15,0,0,308,309,
        3,16,8,0,309,310,5,17,0,0,310,59,1,0,0,0,311,312,5,16,0,0,312,313,
        3,16,8,0,313,314,5,17,0,0,314,61,1,0,0,0,37,66,71,77,83,86,93,97,
        104,107,111,117,123,136,146,150,154,159,163,170,180,186,197,205,
        223,231,235,240,248,252,257,264,268,273,280,284,289,296
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


        def h2_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.H2_sectionContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.H2_sectionContext,i)


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
            self.state = 86
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
                while _la==14:
                    self.state = 74
                    self.h2_section()
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 80
                    self.h1_section()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 88
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
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                self.comment()
                self.state = 93 
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
            self.state = 95
            self.match(ZorgFileParser.T__0)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 96
                self.space_atoms()


            self.state = 99
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
            self.state = 102 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 101
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 104 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 106
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
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 109
                self.todo()
                pass

            elif la_ == 2:
                self.state = 110
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
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 113
                self.match(ZorgFileParser.SPACE)
                self.state = 114
                self.match(ZorgFileParser.SPACE)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(ZorgFileParser.T__1)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 121
                self.match(ZorgFileParser.SPACE)
                self.state = 122
                self.priority()


            self.state = 125
            self.space_atoms()
            self.state = 126
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
            self.state = 128
            self.match(ZorgFileParser.T__2)
            self.state = 129
            self.match(ZorgFileParser.ID)
            self.state = 130
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
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 132
                self.match(ZorgFileParser.SPACE)
                self.state = 133
                self.match(ZorgFileParser.SPACE)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(ZorgFileParser.DASH)
            self.state = 140
            self.space_atoms()
            self.state = 141
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
            self.state = 144 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 143
                self.space_atom()
                self.state = 146 
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
            self.state = 148
            self.match(ZorgFileParser.SPACE)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 149
                self.match(ZorgFileParser.LPAREN)


            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 152
                self.atom()

            elif la_ == 2:
                self.state = 153
                self.quoted()


            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 156
                    self.any_symbol() 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 162
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
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 165
                self.tag_symbol()
                pass

            elif la_ == 2:
                self.state = 166
                self.tag()
                pass

            elif la_ == 3:
                self.state = 167
                self.link()
                pass

            elif la_ == 4:
                self.state = 168
                self.property_()
                pass

            elif la_ == 5:
                self.state = 169
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
            self.state = 172
            self.match(ZorgFileParser.ID)
            self.state = 173
            self.match(ZorgFileParser.T__4)
            self.state = 174
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
            self.state = 176
            self.match(ZorgFileParser.ID)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 178 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 177
                        self.id_symbol()
                        self.state = 180 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 24117248) != 0)):
                            break

                    self.state = 182
                    self.match(ZorgFileParser.ID) 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24117248) != 0)):
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

        def UNDERSCORE(self):
            return self.getToken(ZorgFileParser.UNDERSCORE, 0)

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
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 191
                self.match(ZorgFileParser.SYMBOL)
                pass
            elif token in [26]:
                self.state = 192
                self.match(ZorgFileParser.LPAREN)
                pass
            elif token in [27]:
                self.state = 193
                self.match(ZorgFileParser.RPAREN)
                pass
            elif token in [23]:
                self.state = 194
                self.match(ZorgFileParser.UNDERSCORE)
                pass
            elif token in [20, 21, 22, 24]:
                self.state = 195
                self.id_symbol()
                pass
            elif token in [1, 6, 7, 8]:
                self.state = 196
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
            self.state = 199
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
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 201
                self.area()
                pass
            elif token in [6]:
                self.state = 202
                self.context()
                pass
            elif token in [7]:
                self.state = 203
                self.person()
                pass
            elif token in [8]:
                self.state = 204
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
            self.state = 207
            self.match(ZorgFileParser.T__0)
            self.state = 208
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
            self.state = 210
            self.match(ZorgFileParser.T__5)
            self.state = 211
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
            self.state = 213
            self.match(ZorgFileParser.T__6)
            self.state = 214
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
            self.state = 216
            self.match(ZorgFileParser.T__7)
            self.state = 217
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
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 219
                self.match(ZorgFileParser.T__8)
                self.state = 221 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 220
                    self.atom()
                    self.state = 223 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 264642) != 0)):
                        break

                self.state = 225
                self.match(ZorgFileParser.T__8)
                pass
            elif token in [10]:
                self.state = 227
                self.match(ZorgFileParser.T__9)
                self.state = 229 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 228
                    self.atom()
                    self.state = 231 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 264642) != 0)):
                        break

                self.state = 233
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
            self.state = 237
            self.match(ZorgFileParser.T__10)
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 238
                self.id_group()
                pass

            elif la_ == 2:
                self.state = 239
                self.property_()
                pass


            self.state = 242
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
            self.state = 244
            self.h1_header()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                self.state = 245
                self.block()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==17:
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 251
                    self.match(ZorgFileParser.NL)


                self.state = 254
                self.h2_section()
                self.state = 259
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
            self.state = 260
            self.h2_header()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                self.state = 261
                self.block()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 268
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 267
                        self.match(ZorgFileParser.NL)


                    self.state = 270
                    self.h3_section() 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
            self.state = 276
            self.h3_header()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                self.state = 277
                self.block()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 284
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 283
                        self.match(ZorgFileParser.NL)


                    self.state = 286
                    self.h4_section() 
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
            self.state = 292
            self.h4_header()
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34603012) != 0):
                self.state = 293
                self.block()
                self.state = 298
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
            self.state = 299
            self.match(ZorgFileParser.T__12)
            self.state = 300
            self.space_atoms()
            self.state = 301
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
            self.state = 303
            self.match(ZorgFileParser.T__13)
            self.state = 304
            self.space_atoms()
            self.state = 305
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
            self.state = 307
            self.match(ZorgFileParser.T__14)
            self.state = 308
            self.space_atoms()
            self.state = 309
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
            self.state = 311
            self.match(ZorgFileParser.T__15)
            self.state = 312
            self.space_atoms()
            self.state = 313
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





