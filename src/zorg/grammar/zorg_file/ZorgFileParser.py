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
        4,1,28,363,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,4,0,73,8,0,11,0,12,0,74,1,0,5,0,78,8,0,10,
        0,12,0,81,9,0,1,0,5,0,84,8,0,10,0,12,0,87,9,0,1,0,5,0,90,8,0,10,
        0,12,0,93,9,0,3,0,95,8,0,1,0,1,0,1,1,4,1,100,8,1,11,1,12,1,101,1,
        2,1,2,3,2,106,8,2,1,2,1,2,1,3,4,3,111,8,3,11,3,12,3,112,1,3,3,3,
        116,8,3,1,4,1,4,3,4,120,8,4,1,5,1,5,5,5,124,8,5,10,5,12,5,127,9,
        5,1,5,1,5,1,5,3,5,132,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,5,7,144,8,7,10,7,12,7,147,9,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,4,8,
        156,8,8,11,8,12,8,157,1,8,5,8,161,8,8,10,8,12,8,164,9,8,1,9,4,9,
        167,8,9,11,9,12,9,168,1,10,1,10,1,10,5,10,174,8,10,10,10,12,10,177,
        9,10,1,10,1,10,3,10,181,8,10,1,10,1,10,1,10,5,10,186,8,10,10,10,
        12,10,189,9,10,3,10,191,8,10,1,11,1,11,1,11,1,11,1,11,3,11,198,8,
        11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,4,13,207,8,13,11,13,12,13,
        208,1,13,1,13,5,13,213,8,13,10,13,12,13,216,9,13,1,14,1,14,1,14,
        3,14,221,8,14,1,15,1,15,1,16,1,16,1,16,1,16,3,16,229,8,16,1,17,1,
        17,1,17,1,17,1,17,3,17,236,8,17,1,18,1,18,1,19,1,19,1,20,1,20,1,
        20,1,20,3,20,246,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,
        23,1,24,1,24,1,24,1,25,1,25,4,25,262,8,25,11,25,12,25,263,1,25,1,
        25,1,25,1,25,4,25,270,8,25,11,25,12,25,271,1,25,1,25,3,25,276,8,
        25,1,26,1,26,1,26,1,26,1,27,1,27,5,27,284,8,27,10,27,12,27,287,9,
        27,1,27,3,27,290,8,27,1,27,5,27,293,8,27,10,27,12,27,296,9,27,1,
        28,1,28,5,28,300,8,28,10,28,12,28,303,9,28,1,28,3,28,306,8,28,1,
        28,5,28,309,8,28,10,28,12,28,312,9,28,1,29,1,29,5,29,316,8,29,10,
        29,12,29,319,9,29,1,29,3,29,322,8,29,1,29,5,29,325,8,29,10,29,12,
        29,328,9,29,1,30,1,30,5,30,332,8,30,10,30,12,30,335,9,30,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,
        32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,0,
        0,35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,0,3,1,0,1,3,2,0,15,17,19,
        19,1,0,23,26,381,0,70,1,0,0,0,2,99,1,0,0,0,4,103,1,0,0,0,6,110,1,
        0,0,0,8,119,1,0,0,0,10,125,1,0,0,0,12,136,1,0,0,0,14,145,1,0,0,0,
        16,152,1,0,0,0,18,166,1,0,0,0,20,170,1,0,0,0,22,197,1,0,0,0,24,199,
        1,0,0,0,26,204,1,0,0,0,28,220,1,0,0,0,30,222,1,0,0,0,32,228,1,0,
        0,0,34,235,1,0,0,0,36,237,1,0,0,0,38,239,1,0,0,0,40,245,1,0,0,0,
        42,247,1,0,0,0,44,250,1,0,0,0,46,253,1,0,0,0,48,256,1,0,0,0,50,275,
        1,0,0,0,52,277,1,0,0,0,54,281,1,0,0,0,56,297,1,0,0,0,58,313,1,0,
        0,0,60,329,1,0,0,0,62,336,1,0,0,0,64,348,1,0,0,0,66,352,1,0,0,0,
        68,356,1,0,0,0,70,94,3,2,1,0,71,73,5,10,0,0,72,71,1,0,0,0,73,74,
        1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,79,1,0,0,0,76,78,3,6,3,0,
        77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,85,1,
        0,0,0,81,79,1,0,0,0,82,84,3,56,28,0,83,82,1,0,0,0,84,87,1,0,0,0,
        85,83,1,0,0,0,85,86,1,0,0,0,86,91,1,0,0,0,87,85,1,0,0,0,88,90,3,
        54,27,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,
        92,95,1,0,0,0,93,91,1,0,0,0,94,72,1,0,0,0,94,95,1,0,0,0,95,96,1,
        0,0,0,96,97,5,0,0,1,97,1,1,0,0,0,98,100,3,4,2,0,99,98,1,0,0,0,100,
        101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,3,1,0,0,0,103,105,
        5,23,0,0,104,106,3,18,9,0,105,104,1,0,0,0,105,106,1,0,0,0,106,107,
        1,0,0,0,107,108,5,10,0,0,108,5,1,0,0,0,109,111,3,8,4,0,110,109,1,
        0,0,0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,1,
        0,0,0,114,116,5,10,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,7,1,0,
        0,0,117,120,3,10,5,0,118,120,3,14,7,0,119,117,1,0,0,0,119,118,1,
        0,0,0,120,9,1,0,0,0,121,122,5,20,0,0,122,124,5,20,0,0,123,121,1,
        0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,
        0,0,0,127,125,1,0,0,0,128,131,7,0,0,0,129,130,5,20,0,0,130,132,3,
        12,6,0,131,129,1,0,0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,134,3,
        16,8,0,134,135,5,10,0,0,135,11,1,0,0,0,136,137,5,4,0,0,137,138,5,
        23,0,0,138,139,5,11,0,0,139,140,5,5,0,0,140,13,1,0,0,0,141,142,5,
        20,0,0,142,144,5,20,0,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,
        1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,
        5,15,0,0,149,150,3,16,8,0,150,151,5,10,0,0,151,15,1,0,0,0,152,162,
        3,18,9,0,153,155,5,10,0,0,154,156,5,20,0,0,155,154,1,0,0,0,156,157,
        1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,161,
        3,18,9,0,160,153,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,
        1,0,0,0,163,17,1,0,0,0,164,162,1,0,0,0,165,167,3,20,10,0,166,165,
        1,0,0,0,167,168,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,19,1,
        0,0,0,170,175,5,20,0,0,171,174,3,34,17,0,172,174,5,28,0,0,173,171,
        1,0,0,0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,
        1,0,0,0,176,180,1,0,0,0,177,175,1,0,0,0,178,181,3,22,11,0,179,181,
        3,50,25,0,180,178,1,0,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,190,
        1,0,0,0,182,187,3,32,16,0,183,186,3,32,16,0,184,186,3,28,14,0,185,
        183,1,0,0,0,185,184,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,
        188,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,190,182,1,0,0,0,190,
        191,1,0,0,0,191,21,1,0,0,0,192,198,3,38,19,0,193,198,3,40,20,0,194,
        198,3,52,26,0,195,198,3,24,12,0,196,198,3,26,13,0,197,192,1,0,0,
        0,197,193,1,0,0,0,197,194,1,0,0,0,197,195,1,0,0,0,197,196,1,0,0,
        0,198,23,1,0,0,0,199,200,5,11,0,0,200,201,5,19,0,0,201,202,5,19,
        0,0,202,203,3,26,13,0,203,25,1,0,0,0,204,214,3,28,14,0,205,207,3,
        36,18,0,206,205,1,0,0,0,207,208,1,0,0,0,208,206,1,0,0,0,208,209,
        1,0,0,0,209,210,1,0,0,0,210,211,3,28,14,0,211,213,1,0,0,0,212,206,
        1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,27,1,
        0,0,0,216,214,1,0,0,0,217,221,5,11,0,0,218,221,5,13,0,0,219,221,
        3,30,15,0,220,217,1,0,0,0,220,218,1,0,0,0,220,219,1,0,0,0,221,29,
        1,0,0,0,222,223,5,12,0,0,223,31,1,0,0,0,224,229,5,27,0,0,225,229,
        5,28,0,0,226,229,3,34,17,0,227,229,3,38,19,0,228,224,1,0,0,0,228,
        225,1,0,0,0,228,226,1,0,0,0,228,227,1,0,0,0,229,33,1,0,0,0,230,236,
        5,14,0,0,231,236,5,21,0,0,232,236,5,22,0,0,233,236,5,18,0,0,234,
        236,3,36,18,0,235,230,1,0,0,0,235,231,1,0,0,0,235,232,1,0,0,0,235,
        233,1,0,0,0,235,234,1,0,0,0,236,35,1,0,0,0,237,238,7,1,0,0,238,37,
        1,0,0,0,239,240,7,2,0,0,240,39,1,0,0,0,241,246,3,42,21,0,242,246,
        3,44,22,0,243,246,3,46,23,0,244,246,3,48,24,0,245,241,1,0,0,0,245,
        242,1,0,0,0,245,243,1,0,0,0,245,244,1,0,0,0,246,41,1,0,0,0,247,248,
        5,23,0,0,248,249,5,11,0,0,249,43,1,0,0,0,250,251,5,24,0,0,251,252,
        5,11,0,0,252,45,1,0,0,0,253,254,5,26,0,0,254,255,5,11,0,0,255,47,
        1,0,0,0,256,257,5,25,0,0,257,258,5,11,0,0,258,49,1,0,0,0,259,261,
        5,27,0,0,260,262,3,22,11,0,261,260,1,0,0,0,262,263,1,0,0,0,263,261,
        1,0,0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,266,5,27,0,0,266,276,
        1,0,0,0,267,269,5,28,0,0,268,270,3,22,11,0,269,268,1,0,0,0,270,271,
        1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,273,1,0,0,0,273,274,
        5,28,0,0,274,276,1,0,0,0,275,259,1,0,0,0,275,267,1,0,0,0,276,51,
        1,0,0,0,277,278,5,6,0,0,278,279,3,26,13,0,279,280,5,7,0,0,280,53,
        1,0,0,0,281,285,3,62,31,0,282,284,3,6,3,0,283,282,1,0,0,0,284,287,
        1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,294,1,0,0,0,287,285,
        1,0,0,0,288,290,5,10,0,0,289,288,1,0,0,0,289,290,1,0,0,0,290,291,
        1,0,0,0,291,293,3,56,28,0,292,289,1,0,0,0,293,296,1,0,0,0,294,292,
        1,0,0,0,294,295,1,0,0,0,295,55,1,0,0,0,296,294,1,0,0,0,297,301,3,
        64,32,0,298,300,3,6,3,0,299,298,1,0,0,0,300,303,1,0,0,0,301,299,
        1,0,0,0,301,302,1,0,0,0,302,310,1,0,0,0,303,301,1,0,0,0,304,306,
        5,10,0,0,305,304,1,0,0,0,305,306,1,0,0,0,306,307,1,0,0,0,307,309,
        3,58,29,0,308,305,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,311,
        1,0,0,0,311,57,1,0,0,0,312,310,1,0,0,0,313,317,3,66,33,0,314,316,
        3,6,3,0,315,314,1,0,0,0,316,319,1,0,0,0,317,315,1,0,0,0,317,318,
        1,0,0,0,318,326,1,0,0,0,319,317,1,0,0,0,320,322,5,10,0,0,321,320,
        1,0,0,0,321,322,1,0,0,0,322,323,1,0,0,0,323,325,3,60,30,0,324,321,
        1,0,0,0,325,328,1,0,0,0,326,324,1,0,0,0,326,327,1,0,0,0,327,59,1,
        0,0,0,328,326,1,0,0,0,329,333,3,68,34,0,330,332,3,6,3,0,331,330,
        1,0,0,0,332,335,1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,61,1,
        0,0,0,335,333,1,0,0,0,336,337,5,23,0,0,337,338,5,23,0,0,338,339,
        5,23,0,0,339,340,5,23,0,0,340,341,5,23,0,0,341,342,5,23,0,0,342,
        343,5,23,0,0,343,344,5,23,0,0,344,345,5,23,0,0,345,346,3,18,9,0,
        346,347,5,10,0,0,347,63,1,0,0,0,348,349,5,8,0,0,349,350,3,18,9,0,
        350,351,5,10,0,0,351,65,1,0,0,0,352,353,5,9,0,0,353,354,3,18,9,0,
        354,355,5,10,0,0,355,67,1,0,0,0,356,357,5,15,0,0,357,358,5,15,0,
        0,358,359,5,15,0,0,359,360,3,18,9,0,360,361,5,10,0,0,361,69,1,0,
        0,0,42,74,79,85,91,94,101,105,112,115,119,125,131,145,157,162,168,
        173,175,180,185,187,190,197,208,214,220,228,235,245,263,271,275,
        285,289,294,301,305,310,317,321,326,333
    ]

class ZorgFileParser ( Parser ):

    grammarFileName = "ZorgFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'o'", "'x'", "'~'", "'['", "']'", "'[['", 
                     "']]'", "'======='", "'*****'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'-'", "'.'", 
                     "'/'", "'_'", "':'", "' '", "'('", "')'", "'#'", "'@'", 
                     "'+'", "'%'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NL", "ID", "DATE", "NUM_ID", 
                      "SYMBOL", "DASH", "DOT", "FSLASH", "UNDERSCORE", "COLON", 
                      "SPACE", "LPAREN", "RPAREN", "HASH", "AT_SIGN", "PLUS", 
                      "PERCENT", "SQUOTE", "DQUOTE" ]

    RULE_prog = 0
    RULE_head = 1
    RULE_comment = 2
    RULE_block = 3
    RULE_item = 4
    RULE_todo = 5
    RULE_priority = 6
    RULE_note = 7
    RULE_item_body = 8
    RULE_space_atoms = 9
    RULE_space_atom = 10
    RULE_atom = 11
    RULE_property = 12
    RULE_id_group = 13
    RULE_id = 14
    RULE_date = 15
    RULE_any_symbol = 16
    RULE_non_tag_symbol = 17
    RULE_id_symbol = 18
    RULE_tag_symbol = 19
    RULE_tag = 20
    RULE_area = 21
    RULE_context = 22
    RULE_person = 23
    RULE_project = 24
    RULE_quoted = 25
    RULE_link = 26
    RULE_h1_section = 27
    RULE_h2_section = 28
    RULE_h3_section = 29
    RULE_h4_section = 30
    RULE_h1_header = 31
    RULE_h2_header = 32
    RULE_h3_header = 33
    RULE_h4_header = 34

    ruleNames =  [ "prog", "head", "comment", "block", "item", "todo", "priority", 
                   "note", "item_body", "space_atoms", "space_atom", "atom", 
                   "property", "id_group", "id", "date", "any_symbol", "non_tag_symbol", 
                   "id_symbol", "tag_symbol", "tag", "area", "context", 
                   "person", "project", "quoted", "link", "h1_section", 
                   "h2_section", "h3_section", "h4_section", "h1_header", 
                   "h2_header", "h3_header", "h4_header" ]

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
    NL=10
    ID=11
    DATE=12
    NUM_ID=13
    SYMBOL=14
    DASH=15
    DOT=16
    FSLASH=17
    UNDERSCORE=18
    COLON=19
    SPACE=20
    LPAREN=21
    RPAREN=22
    HASH=23
    AT_SIGN=24
    PLUS=25
    PERCENT=26
    SQUOTE=27
    DQUOTE=28

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
            self.state = 70
            self.head()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 71
                    self.match(ZorgFileParser.NL)
                    self.state = 74 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==10):
                        break

                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1081358) != 0):
                    self.state = 76
                    self.block()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 82
                    self.h2_section()
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 88
                    self.h1_section()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 96
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
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.comment()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==23):
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

        def HASH(self):
            return self.getToken(ZorgFileParser.HASH, 0)

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
            self.state = 103
            self.match(ZorgFileParser.HASH)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 104
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
            self.state = 110 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 109
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 112 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 114
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.todo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
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

        def item_body(self):
            return self.getTypedRuleContext(ZorgFileParser.Item_bodyContext,0)


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
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 121
                self.match(ZorgFileParser.SPACE)
                self.state = 122
                self.match(ZorgFileParser.SPACE)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 129
                self.match(ZorgFileParser.SPACE)
                self.state = 130
                self.priority()


            self.state = 133
            self.item_body()
            self.state = 134
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

        def HASH(self):
            return self.getToken(ZorgFileParser.HASH, 0)

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
            self.state = 136
            self.match(ZorgFileParser.T__3)
            self.state = 137
            self.match(ZorgFileParser.HASH)
            self.state = 138
            self.match(ZorgFileParser.ID)
            self.state = 139
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

        def DASH(self):
            return self.getToken(ZorgFileParser.DASH, 0)

        def item_body(self):
            return self.getTypedRuleContext(ZorgFileParser.Item_bodyContext,0)


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
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 141
                self.match(ZorgFileParser.SPACE)
                self.state = 142
                self.match(ZorgFileParser.SPACE)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.match(ZorgFileParser.DASH)
            self.state = 149
            self.item_body()
            self.state = 150
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_atoms(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Space_atomsContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.NL)
            else:
                return self.getToken(ZorgFileParser.NL, i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SPACE)
            else:
                return self.getToken(ZorgFileParser.SPACE, i)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_item_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_body" ):
                listener.enterItem_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_body" ):
                listener.exitItem_body(self)




    def item_body(self):

        localctx = ZorgFileParser.Item_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_item_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.space_atoms()
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 153
                    self.match(ZorgFileParser.NL)
                    self.state = 155 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 154
                            self.match(ZorgFileParser.SPACE)

                        else:
                            raise NoViableAltException(self)
                        self.state = 157 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                    self.state = 159
                    self.space_atoms() 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_space_atoms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 165
                self.space_atom()
                self.state = 168 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
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

        def non_tag_symbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Non_tag_symbolContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Non_tag_symbolContext,i)


        def DQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.DQUOTE)
            else:
                return self.getToken(ZorgFileParser.DQUOTE, i)

        def atom(self):
            return self.getTypedRuleContext(ZorgFileParser.AtomContext,0)


        def quoted(self):
            return self.getTypedRuleContext(ZorgFileParser.QuotedContext,0)


        def any_symbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Any_symbolContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Any_symbolContext,i)


        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.IdContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.IdContext,i)


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
        self.enterRule(localctx, 20, self.RULE_space_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ZorgFileParser.SPACE)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 173
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [14, 15, 16, 17, 18, 19, 21, 22]:
                        self.state = 171
                        self.non_tag_symbol()
                        pass
                    elif token in [28]:
                        self.state = 172
                        self.match(ZorgFileParser.DQUOTE)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 178
                self.atom()

            elif la_ == 2:
                self.state = 179
                self.quoted()


            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 535805952) != 0):
                self.state = 182
                self.any_symbol()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 535820288) != 0):
                    self.state = 185
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28]:
                        self.state = 183
                        self.any_symbol()
                        pass
                    elif token in [11, 12, 13]:
                        self.state = 184
                        self.id_()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 189
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
        self.enterRule(localctx, 22, self.RULE_atom)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.tag_symbol()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.tag()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.link()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.property_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
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

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.COLON)
            else:
                return self.getToken(ZorgFileParser.COLON, i)

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
        self.enterRule(localctx, 24, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ZorgFileParser.ID)
            self.state = 200
            self.match(ZorgFileParser.COLON)
            self.state = 201
            self.match(ZorgFileParser.COLON)
            self.state = 202
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

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.IdContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.IdContext,i)


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
        self.enterRule(localctx, 26, self.RULE_id_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.id_()
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 205
                        self.id_symbol()
                        self.state = 208 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 753664) != 0)):
                            break

                    self.state = 210
                    self.id_() 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            return self.getToken(ZorgFileParser.ID, 0)

        def NUM_ID(self):
            return self.getToken(ZorgFileParser.NUM_ID, 0)

        def date(self):
            return self.getTypedRuleContext(ZorgFileParser.DateContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)




    def id_(self):

        localctx = ZorgFileParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_id)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(ZorgFileParser.ID)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(ZorgFileParser.NUM_ID)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.date()
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


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(ZorgFileParser.DATE, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)




    def date(self):

        localctx = ZorgFileParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(ZorgFileParser.DATE)
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

        def SQUOTE(self):
            return self.getToken(ZorgFileParser.SQUOTE, 0)

        def DQUOTE(self):
            return self.getToken(ZorgFileParser.DQUOTE, 0)

        def non_tag_symbol(self):
            return self.getTypedRuleContext(ZorgFileParser.Non_tag_symbolContext,0)


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
        self.enterRule(localctx, 32, self.RULE_any_symbol)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(ZorgFileParser.SQUOTE)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(ZorgFileParser.DQUOTE)
                pass
            elif token in [14, 15, 16, 17, 18, 19, 21, 22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.non_tag_symbol()
                pass
            elif token in [23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 227
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


    class Non_tag_symbolContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return ZorgFileParser.RULE_non_tag_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_tag_symbol" ):
                listener.enterNon_tag_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_tag_symbol" ):
                listener.exitNon_tag_symbol(self)




    def non_tag_symbol(self):

        localctx = ZorgFileParser.Non_tag_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_non_tag_symbol)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(ZorgFileParser.SYMBOL)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(ZorgFileParser.LPAREN)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.match(ZorgFileParser.RPAREN)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.match(ZorgFileParser.UNDERSCORE)
                pass
            elif token in [15, 16, 17, 19]:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.id_symbol()
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
        self.enterRule(localctx, 36, self.RULE_id_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 753664) != 0)):
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


    class Tag_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(ZorgFileParser.HASH, 0)

        def AT_SIGN(self):
            return self.getToken(ZorgFileParser.AT_SIGN, 0)

        def PERCENT(self):
            return self.getToken(ZorgFileParser.PERCENT, 0)

        def PLUS(self):
            return self.getToken(ZorgFileParser.PLUS, 0)

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
        self.enterRule(localctx, 38, self.RULE_tag_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_tag)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.area()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.context()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.person()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
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
            return self.getToken(ZorgFileParser.HASH, 0)

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
        self.enterRule(localctx, 42, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ZorgFileParser.HASH)
            self.state = 248
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

        def AT_SIGN(self):
            return self.getToken(ZorgFileParser.AT_SIGN, 0)

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
        self.enterRule(localctx, 44, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ZorgFileParser.AT_SIGN)
            self.state = 251
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

        def PERCENT(self):
            return self.getToken(ZorgFileParser.PERCENT, 0)

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
        self.enterRule(localctx, 46, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ZorgFileParser.PERCENT)
            self.state = 254
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

        def PLUS(self):
            return self.getToken(ZorgFileParser.PLUS, 0)

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
        self.enterRule(localctx, 48, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ZorgFileParser.PLUS)
            self.state = 257
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

        def SQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SQUOTE)
            else:
                return self.getToken(ZorgFileParser.SQUOTE, i)

        def DQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.DQUOTE)
            else:
                return self.getToken(ZorgFileParser.DQUOTE, i)

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
        self.enterRule(localctx, 50, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 259
                self.match(ZorgFileParser.SQUOTE)
                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 260
                    self.atom()
                    self.state = 263 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 125843520) != 0)):
                        break

                self.state = 265
                self.match(ZorgFileParser.SQUOTE)
                pass
            elif token in [28]:
                self.state = 267
                self.match(ZorgFileParser.DQUOTE)
                self.state = 269 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 268
                    self.atom()
                    self.state = 271 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 125843520) != 0)):
                        break

                self.state = 273
                self.match(ZorgFileParser.DQUOTE)
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
        self.enterRule(localctx, 52, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(ZorgFileParser.T__5)
            self.state = 278
            self.id_group()
            self.state = 279
            self.match(ZorgFileParser.T__6)
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
        self.enterRule(localctx, 54, self.RULE_h1_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.h1_header()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1081358) != 0):
                self.state = 282
                self.block()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==10:
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 288
                    self.match(ZorgFileParser.NL)


                self.state = 291
                self.h2_section()
                self.state = 296
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
        self.enterRule(localctx, 56, self.RULE_h2_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.h2_header()
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1081358) != 0):
                self.state = 298
                self.block()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 305
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 304
                        self.match(ZorgFileParser.NL)


                    self.state = 307
                    self.h3_section() 
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_h3_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.h3_header()
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 314
                    self.block() 
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 320
                        self.match(ZorgFileParser.NL)


                    self.state = 323
                    self.h4_section() 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_h4_section)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.h4_header()
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 330
                    self.block() 
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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

        def HASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.HASH)
            else:
                return self.getToken(ZorgFileParser.HASH, i)

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
        self.enterRule(localctx, 62, self.RULE_h1_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ZorgFileParser.HASH)
            self.state = 337
            self.match(ZorgFileParser.HASH)
            self.state = 338
            self.match(ZorgFileParser.HASH)
            self.state = 339
            self.match(ZorgFileParser.HASH)
            self.state = 340
            self.match(ZorgFileParser.HASH)
            self.state = 341
            self.match(ZorgFileParser.HASH)
            self.state = 342
            self.match(ZorgFileParser.HASH)
            self.state = 343
            self.match(ZorgFileParser.HASH)
            self.state = 344
            self.match(ZorgFileParser.HASH)
            self.state = 345
            self.space_atoms()
            self.state = 346
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
        self.enterRule(localctx, 64, self.RULE_h2_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(ZorgFileParser.T__7)
            self.state = 349
            self.space_atoms()
            self.state = 350
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
        self.enterRule(localctx, 66, self.RULE_h3_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ZorgFileParser.T__8)
            self.state = 353
            self.space_atoms()
            self.state = 354
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

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.DASH)
            else:
                return self.getToken(ZorgFileParser.DASH, i)

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
        self.enterRule(localctx, 68, self.RULE_h4_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ZorgFileParser.DASH)
            self.state = 357
            self.match(ZorgFileParser.DASH)
            self.state = 358
            self.match(ZorgFileParser.DASH)
            self.state = 359
            self.space_atoms()
            self.state = 360
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





