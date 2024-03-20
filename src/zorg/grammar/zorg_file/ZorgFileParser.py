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
        4,1,17,214,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,4,0,51,8,0,11,0,12,0,
        52,1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,5,0,62,8,0,10,0,12,0,65,9,
        0,1,0,1,0,1,1,4,1,70,8,1,11,1,12,1,71,1,2,1,2,3,2,76,8,2,1,2,1,2,
        1,3,4,3,81,8,3,11,3,12,3,82,1,3,3,3,86,8,3,1,4,1,4,3,4,90,8,4,1,
        5,1,5,1,5,3,5,95,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,8,4,8,109,8,8,11,8,12,8,110,1,9,1,9,1,9,1,9,3,9,117,8,9,1,9,5,
        9,120,8,9,10,9,12,9,123,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        11,3,11,133,8,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,
        15,1,15,1,15,1,16,1,16,4,16,149,8,16,11,16,12,16,150,1,16,3,16,154,
        8,16,1,16,5,16,157,8,16,10,16,12,16,160,9,16,1,17,1,17,4,17,164,
        8,17,11,17,12,17,165,1,17,3,17,169,8,17,1,17,5,17,172,8,17,10,17,
        12,17,175,9,17,1,18,1,18,4,18,179,8,18,11,18,12,18,180,1,18,3,18,
        184,8,18,1,18,5,18,187,8,18,10,18,12,18,190,9,18,1,19,1,19,4,19,
        194,8,19,11,19,12,19,195,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,
        1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,0,216,0,
        48,1,0,0,0,2,69,1,0,0,0,4,73,1,0,0,0,6,80,1,0,0,0,8,89,1,0,0,0,10,
        91,1,0,0,0,12,99,1,0,0,0,14,103,1,0,0,0,16,108,1,0,0,0,18,112,1,
        0,0,0,20,124,1,0,0,0,22,132,1,0,0,0,24,134,1,0,0,0,26,137,1,0,0,
        0,28,140,1,0,0,0,30,143,1,0,0,0,32,146,1,0,0,0,34,161,1,0,0,0,36,
        176,1,0,0,0,38,191,1,0,0,0,40,197,1,0,0,0,42,201,1,0,0,0,44,205,
        1,0,0,0,46,209,1,0,0,0,48,50,3,2,1,0,49,51,5,15,0,0,50,49,1,0,0,
        0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,57,1,0,0,0,54,56,
        3,6,3,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,
        58,63,1,0,0,0,59,57,1,0,0,0,60,62,3,32,16,0,61,60,1,0,0,0,62,65,
        1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,
        66,67,5,0,0,1,67,1,1,0,0,0,68,70,3,4,2,0,69,68,1,0,0,0,70,71,1,0,
        0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,3,1,0,0,0,73,75,5,1,0,0,74,76,
        3,16,8,0,75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,15,0,
        0,78,5,1,0,0,0,79,81,3,8,4,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,
        0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,86,5,15,0,0,85,84,1,0,0,0,85,
        86,1,0,0,0,86,7,1,0,0,0,87,90,3,10,5,0,88,90,3,14,7,0,89,87,1,0,
        0,0,89,88,1,0,0,0,90,9,1,0,0,0,91,94,5,2,0,0,92,93,5,3,0,0,93,95,
        3,12,6,0,94,92,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,3,16,8,
        0,97,98,5,15,0,0,98,11,1,0,0,0,99,100,5,4,0,0,100,101,5,16,0,0,101,
        102,5,5,0,0,102,13,1,0,0,0,103,104,5,6,0,0,104,105,3,16,8,0,105,
        106,5,15,0,0,106,15,1,0,0,0,107,109,3,18,9,0,108,107,1,0,0,0,109,
        110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,17,1,0,0,0,112,116,
        5,3,0,0,113,117,3,22,11,0,114,117,3,20,10,0,115,117,5,16,0,0,116,
        113,1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,116,117,1,0,0,0,117,
        121,1,0,0,0,118,120,5,17,0,0,119,118,1,0,0,0,120,123,1,0,0,0,121,
        119,1,0,0,0,121,122,1,0,0,0,122,19,1,0,0,0,123,121,1,0,0,0,124,125,
        5,16,0,0,125,126,5,7,0,0,126,127,5,16,0,0,127,21,1,0,0,0,128,133,
        3,24,12,0,129,133,3,26,13,0,130,133,3,28,14,0,131,133,3,30,15,0,
        132,128,1,0,0,0,132,129,1,0,0,0,132,130,1,0,0,0,132,131,1,0,0,0,
        133,23,1,0,0,0,134,135,5,1,0,0,135,136,5,16,0,0,136,25,1,0,0,0,137,
        138,5,8,0,0,138,139,5,16,0,0,139,27,1,0,0,0,140,141,5,9,0,0,141,
        142,5,16,0,0,142,29,1,0,0,0,143,144,5,10,0,0,144,145,5,16,0,0,145,
        31,1,0,0,0,146,148,3,40,20,0,147,149,3,6,3,0,148,147,1,0,0,0,149,
        150,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,158,1,0,0,0,152,
        154,5,15,0,0,153,152,1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,
        157,3,34,17,0,156,153,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,
        159,1,0,0,0,159,33,1,0,0,0,160,158,1,0,0,0,161,163,3,42,21,0,162,
        164,3,6,3,0,163,162,1,0,0,0,164,165,1,0,0,0,165,163,1,0,0,0,165,
        166,1,0,0,0,166,173,1,0,0,0,167,169,5,15,0,0,168,167,1,0,0,0,168,
        169,1,0,0,0,169,170,1,0,0,0,170,172,3,36,18,0,171,168,1,0,0,0,172,
        175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,35,1,0,0,0,175,173,
        1,0,0,0,176,178,3,44,22,0,177,179,3,6,3,0,178,177,1,0,0,0,179,180,
        1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,188,1,0,0,0,182,184,
        5,15,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,187,
        3,38,19,0,186,183,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,
        1,0,0,0,189,37,1,0,0,0,190,188,1,0,0,0,191,193,3,46,23,0,192,194,
        3,6,3,0,193,192,1,0,0,0,194,195,1,0,0,0,195,193,1,0,0,0,195,196,
        1,0,0,0,196,39,1,0,0,0,197,198,5,11,0,0,198,199,3,16,8,0,199,200,
        5,15,0,0,200,41,1,0,0,0,201,202,5,12,0,0,202,203,3,16,8,0,203,204,
        5,15,0,0,204,43,1,0,0,0,205,206,5,13,0,0,206,207,3,16,8,0,207,208,
        5,15,0,0,208,45,1,0,0,0,209,210,5,14,0,0,210,211,3,16,8,0,211,212,
        5,15,0,0,212,47,1,0,0,0,23,52,57,63,71,75,82,85,89,94,110,116,121,
        132,150,153,158,165,168,173,180,183,188,195
    ]

class ZorgFileParser ( Parser ):

    grammarFileName = "ZorgFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'o'", "' '", "'[#'", "']'", "'-'", 
                     "'::'", "'@'", "'%'", "'+'", "'#########'", "'======='", 
                     "'*****'", "'---'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_property = 10
    RULE_tag = 11
    RULE_area = 12
    RULE_context = 13
    RULE_person = 14
    RULE_project = 15
    RULE_h1_section = 16
    RULE_h2_section = 17
    RULE_h3_section = 18
    RULE_h4_section = 19
    RULE_h1_header = 20
    RULE_h2_header = 21
    RULE_h3_header = 22
    RULE_h4_header = 23

    ruleNames =  [ "prog", "head", "comment", "block", "item", "todo", "priority", 
                   "note", "space_atoms", "space_atom", "property", "tag", 
                   "area", "context", "person", "project", "h1_section", 
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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    NL=15
    ID=16
    SYMBOL=17

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
            self.state = 48
            self.head()
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.match(ZorgFileParser.NL)
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 54
                self.block()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 60
                self.h1_section()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.comment()
                self.state = 71 
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
            self.state = 73
            self.match(ZorgFileParser.T__0)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 74
                self.space_atoms()


            self.state = 77
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
            self.state = 80 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 79
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 82 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 84
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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 87
                self.todo()
                pass
            elif token in [6]:
                self.state = 88
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
            self.state = 91
            self.match(ZorgFileParser.T__1)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 92
                self.match(ZorgFileParser.T__2)
                self.state = 93
                self.priority()


            self.state = 96
            self.space_atoms()
            self.state = 97
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
            self.state = 99
            self.match(ZorgFileParser.T__3)
            self.state = 100
            self.match(ZorgFileParser.ID)
            self.state = 101
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
            self.state = 103
            self.match(ZorgFileParser.T__5)
            self.state = 104
            self.space_atoms()
            self.state = 105
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
            self.state = 108 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self.space_atom()
                self.state = 110 
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
            self.state = 112
            self.match(ZorgFileParser.T__2)
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 113
                self.tag()

            elif la_ == 2:
                self.state = 114
                self.property_()

            elif la_ == 3:
                self.state = 115
                self.match(ZorgFileParser.ID)


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 118
                self.match(ZorgFileParser.SYMBOL)
                self.state = 123
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
            self.state = 124
            self.match(ZorgFileParser.ID)
            self.state = 125
            self.match(ZorgFileParser.T__6)
            self.state = 126
            self.match(ZorgFileParser.ID)
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
        self.enterRule(localctx, 22, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 128
                self.area()
                pass
            elif token in [8]:
                self.state = 129
                self.context()
                pass
            elif token in [9]:
                self.state = 130
                self.person()
                pass
            elif token in [10]:
                self.state = 131
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
        self.enterRule(localctx, 24, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ZorgFileParser.T__0)
            self.state = 135
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
        self.enterRule(localctx, 26, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ZorgFileParser.T__7)
            self.state = 138
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
        self.enterRule(localctx, 28, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ZorgFileParser.T__8)
            self.state = 141
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
        self.enterRule(localctx, 30, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ZorgFileParser.T__9)
            self.state = 144
            self.match(ZorgFileParser.ID)
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
        self.enterRule(localctx, 32, self.RULE_h1_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.h1_header()
            self.state = 148 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 147
                self.block()
                self.state = 150 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==6):
                    break

            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==15:
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 152
                    self.match(ZorgFileParser.NL)


                self.state = 155
                self.h2_section()
                self.state = 160
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
        self.enterRule(localctx, 34, self.RULE_h2_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.h2_header()
            self.state = 163 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 162
                self.block()
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==6):
                    break

            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==15:
                        self.state = 167
                        self.match(ZorgFileParser.NL)


                    self.state = 170
                    self.h3_section() 
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_h3_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.h3_header()
            self.state = 178 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 177
                self.block()
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==6):
                    break

            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==15:
                        self.state = 182
                        self.match(ZorgFileParser.NL)


                    self.state = 185
                    self.h4_section() 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_h4_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.h4_header()
            self.state = 193 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 192
                self.block()
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==6):
                    break

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
        self.enterRule(localctx, 40, self.RULE_h1_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ZorgFileParser.T__10)
            self.state = 198
            self.space_atoms()
            self.state = 199
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
        self.enterRule(localctx, 42, self.RULE_h2_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(ZorgFileParser.T__11)
            self.state = 202
            self.space_atoms()
            self.state = 203
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
        self.enterRule(localctx, 44, self.RULE_h3_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ZorgFileParser.T__12)
            self.state = 206
            self.space_atoms()
            self.state = 207
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
        self.enterRule(localctx, 46, self.RULE_h4_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(ZorgFileParser.T__13)
            self.state = 210
            self.space_atoms()
            self.state = 211
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





