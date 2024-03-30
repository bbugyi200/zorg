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
        4,1,31,432,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,1,0,4,0,85,8,0,11,0,12,0,86,1,0,5,0,90,8,0,10,0,12,
        0,93,9,0,1,0,5,0,96,8,0,10,0,12,0,99,9,0,1,0,5,0,102,8,0,10,0,12,
        0,105,9,0,3,0,107,8,0,1,0,1,0,1,1,4,1,112,8,1,11,1,12,1,113,1,2,
        1,2,3,2,118,8,2,1,2,1,2,1,3,4,3,123,8,3,11,3,12,3,124,1,3,5,3,128,
        8,3,10,3,12,3,131,9,3,1,4,1,4,1,4,1,4,3,4,137,8,4,1,5,1,5,5,5,141,
        8,5,10,5,12,5,144,9,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,5,7,153,8,7,10,
        7,12,7,156,9,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,165,8,9,1,9,1,9,1,
        9,1,10,1,10,1,10,1,10,5,10,174,8,10,10,10,12,10,177,9,10,1,11,1,
        11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,4,12,189,8,12,11,12,12,
        12,190,1,12,3,12,194,8,12,1,12,1,12,3,12,198,8,12,1,12,5,12,201,
        8,12,10,12,12,12,204,9,12,5,12,206,8,12,10,12,12,12,209,9,12,1,13,
        1,13,1,13,1,13,1,14,4,14,216,8,14,11,14,12,14,217,1,15,1,15,1,15,
        3,15,223,8,15,1,15,1,15,5,15,227,8,15,10,15,12,15,230,9,15,1,15,
        1,15,3,15,234,8,15,1,15,1,15,1,15,5,15,239,8,15,10,15,12,15,242,
        9,15,3,15,244,8,15,1,15,3,15,247,8,15,1,16,1,16,1,16,1,16,1,16,1,
        16,3,16,255,8,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,4,18,264,8,18,
        11,18,12,18,265,1,18,1,18,5,18,270,8,18,10,18,12,18,273,9,18,1,19,
        1,19,1,19,1,19,1,19,3,19,280,8,19,1,20,1,20,1,21,1,21,1,21,1,21,
        3,21,288,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,
        299,8,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,25,3,25,309,8,25,1,
        26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,
        30,1,30,1,30,1,30,4,30,328,8,30,11,30,12,30,329,1,30,1,30,1,30,4,
        30,335,8,30,11,30,12,30,336,1,30,1,30,3,30,341,8,30,1,31,1,31,1,
        31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,5,33,353,8,33,10,33,12,33,
        356,9,33,1,33,3,33,359,8,33,1,33,5,33,362,8,33,10,33,12,33,365,9,
        33,1,34,1,34,5,34,369,8,34,10,34,12,34,372,9,34,1,34,3,34,375,8,
        34,1,34,5,34,378,8,34,10,34,12,34,381,9,34,1,35,1,35,5,35,385,8,
        35,10,35,12,35,388,9,35,1,35,3,35,391,8,35,1,35,5,35,394,8,35,10,
        35,12,35,397,9,35,1,36,1,36,5,36,401,8,36,10,36,12,36,404,9,36,1,
        37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,
        38,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,0,0,41,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,0,
        3,2,0,8,9,28,31,2,0,14,16,18,18,1,0,22,25,462,0,82,1,0,0,0,2,111,
        1,0,0,0,4,115,1,0,0,0,6,122,1,0,0,0,8,136,1,0,0,0,10,138,1,0,0,0,
        12,145,1,0,0,0,14,150,1,0,0,0,16,157,1,0,0,0,18,161,1,0,0,0,20,169,
        1,0,0,0,22,178,1,0,0,0,24,184,1,0,0,0,26,210,1,0,0,0,28,215,1,0,
        0,0,30,219,1,0,0,0,32,254,1,0,0,0,34,256,1,0,0,0,36,261,1,0,0,0,
        38,279,1,0,0,0,40,281,1,0,0,0,42,287,1,0,0,0,44,298,1,0,0,0,46,300,
        1,0,0,0,48,302,1,0,0,0,50,308,1,0,0,0,52,310,1,0,0,0,54,313,1,0,
        0,0,56,316,1,0,0,0,58,319,1,0,0,0,60,340,1,0,0,0,62,342,1,0,0,0,
        64,346,1,0,0,0,66,350,1,0,0,0,68,366,1,0,0,0,70,382,1,0,0,0,72,398,
        1,0,0,0,74,405,1,0,0,0,76,417,1,0,0,0,78,421,1,0,0,0,80,425,1,0,
        0,0,82,106,3,2,1,0,83,85,5,7,0,0,84,83,1,0,0,0,85,86,1,0,0,0,86,
        84,1,0,0,0,86,87,1,0,0,0,87,91,1,0,0,0,88,90,3,6,3,0,89,88,1,0,0,
        0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,97,1,0,0,0,93,91,
        1,0,0,0,94,96,3,68,34,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,
        0,97,98,1,0,0,0,98,103,1,0,0,0,99,97,1,0,0,0,100,102,3,66,33,0,101,
        100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,
        107,1,0,0,0,105,103,1,0,0,0,106,84,1,0,0,0,106,107,1,0,0,0,107,108,
        1,0,0,0,108,109,5,0,0,1,109,1,1,0,0,0,110,112,3,4,2,0,111,110,1,
        0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,3,1,0,
        0,0,115,117,5,22,0,0,116,118,3,28,14,0,117,116,1,0,0,0,117,118,1,
        0,0,0,118,119,1,0,0,0,119,120,5,7,0,0,120,5,1,0,0,0,121,123,3,8,
        4,0,122,121,1,0,0,0,123,124,1,0,0,0,124,122,1,0,0,0,124,125,1,0,
        0,0,125,129,1,0,0,0,126,128,5,7,0,0,127,126,1,0,0,0,128,131,1,0,
        0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,7,1,0,0,0,131,129,1,0,0,
        0,132,137,3,10,5,0,133,137,3,14,7,0,134,137,3,26,13,0,135,137,3,
        4,2,0,136,132,1,0,0,0,136,133,1,0,0,0,136,134,1,0,0,0,136,135,1,
        0,0,0,137,9,1,0,0,0,138,142,3,18,9,0,139,141,3,20,10,0,140,139,1,
        0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,11,1,0,
        0,0,144,142,1,0,0,0,145,146,5,1,0,0,146,147,5,22,0,0,147,148,5,10,
        0,0,148,149,5,2,0,0,149,13,1,0,0,0,150,154,3,16,8,0,151,153,3,20,
        10,0,152,151,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,
        0,0,155,15,1,0,0,0,156,154,1,0,0,0,157,158,5,14,0,0,158,159,3,24,
        12,0,159,160,5,7,0,0,160,17,1,0,0,0,161,164,7,0,0,0,162,163,5,19,
        0,0,163,165,3,12,6,0,164,162,1,0,0,0,164,165,1,0,0,0,165,166,1,0,
        0,0,166,167,3,24,12,0,167,168,5,7,0,0,168,19,1,0,0,0,169,170,5,19,
        0,0,170,171,5,19,0,0,171,175,3,16,8,0,172,174,3,22,11,0,173,172,
        1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,21,1,
        0,0,0,177,175,1,0,0,0,178,179,5,19,0,0,179,180,5,19,0,0,180,181,
        5,19,0,0,181,182,5,19,0,0,182,183,3,16,8,0,183,23,1,0,0,0,184,207,
        3,28,14,0,185,186,5,7,0,0,186,188,5,19,0,0,187,189,5,19,0,0,188,
        187,1,0,0,0,189,190,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,
        193,1,0,0,0,192,194,5,20,0,0,193,192,1,0,0,0,193,194,1,0,0,0,194,
        195,1,0,0,0,195,197,3,32,16,0,196,198,5,13,0,0,197,196,1,0,0,0,197,
        198,1,0,0,0,198,202,1,0,0,0,199,201,3,30,15,0,200,199,1,0,0,0,201,
        204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,206,1,0,0,0,204,
        202,1,0,0,0,205,185,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,
        208,1,0,0,0,208,25,1,0,0,0,209,207,1,0,0,0,210,211,3,64,32,0,211,
        212,5,18,0,0,212,213,3,28,14,0,213,27,1,0,0,0,214,216,3,30,15,0,
        215,214,1,0,0,0,216,217,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,
        218,29,1,0,0,0,219,222,5,19,0,0,220,221,5,26,0,0,221,223,3,44,22,
        0,222,220,1,0,0,0,222,223,1,0,0,0,223,228,1,0,0,0,224,227,3,44,22,
        0,225,227,5,27,0,0,226,224,1,0,0,0,226,225,1,0,0,0,227,230,1,0,0,
        0,228,226,1,0,0,0,228,229,1,0,0,0,229,233,1,0,0,0,230,228,1,0,0,
        0,231,234,3,32,16,0,232,234,3,60,30,0,233,231,1,0,0,0,233,232,1,
        0,0,0,233,234,1,0,0,0,234,243,1,0,0,0,235,240,3,42,21,0,236,239,
        3,42,21,0,237,239,3,38,19,0,238,236,1,0,0,0,238,237,1,0,0,0,239,
        242,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,244,1,0,0,0,242,
        240,1,0,0,0,243,235,1,0,0,0,243,244,1,0,0,0,244,246,1,0,0,0,245,
        247,3,64,32,0,246,245,1,0,0,0,246,247,1,0,0,0,247,31,1,0,0,0,248,
        255,3,48,24,0,249,255,3,50,25,0,250,255,3,62,31,0,251,255,3,34,17,
        0,252,255,3,36,18,0,253,255,3,64,32,0,254,248,1,0,0,0,254,249,1,
        0,0,0,254,250,1,0,0,0,254,251,1,0,0,0,254,252,1,0,0,0,254,253,1,
        0,0,0,255,33,1,0,0,0,256,257,5,10,0,0,257,258,5,18,0,0,258,259,5,
        18,0,0,259,260,3,36,18,0,260,35,1,0,0,0,261,271,3,38,19,0,262,264,
        3,46,23,0,263,262,1,0,0,0,264,265,1,0,0,0,265,263,1,0,0,0,265,266,
        1,0,0,0,266,267,1,0,0,0,267,268,3,38,19,0,268,270,1,0,0,0,269,263,
        1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,37,1,
        0,0,0,273,271,1,0,0,0,274,280,5,10,0,0,275,280,5,12,0,0,276,280,
        3,40,20,0,277,280,5,8,0,0,278,280,5,9,0,0,279,274,1,0,0,0,279,275,
        1,0,0,0,279,276,1,0,0,0,279,277,1,0,0,0,279,278,1,0,0,0,280,39,1,
        0,0,0,281,282,5,11,0,0,282,41,1,0,0,0,283,288,5,26,0,0,284,288,5,
        27,0,0,285,288,3,44,22,0,286,288,3,48,24,0,287,283,1,0,0,0,287,284,
        1,0,0,0,287,285,1,0,0,0,287,286,1,0,0,0,288,43,1,0,0,0,289,299,5,
        30,0,0,290,299,5,31,0,0,291,299,5,29,0,0,292,299,5,28,0,0,293,299,
        5,13,0,0,294,299,5,20,0,0,295,299,5,21,0,0,296,299,5,17,0,0,297,
        299,3,46,23,0,298,289,1,0,0,0,298,290,1,0,0,0,298,291,1,0,0,0,298,
        292,1,0,0,0,298,293,1,0,0,0,298,294,1,0,0,0,298,295,1,0,0,0,298,
        296,1,0,0,0,298,297,1,0,0,0,299,45,1,0,0,0,300,301,7,1,0,0,301,47,
        1,0,0,0,302,303,7,2,0,0,303,49,1,0,0,0,304,309,3,52,26,0,305,309,
        3,54,27,0,306,309,3,56,28,0,307,309,3,58,29,0,308,304,1,0,0,0,308,
        305,1,0,0,0,308,306,1,0,0,0,308,307,1,0,0,0,309,51,1,0,0,0,310,311,
        5,22,0,0,311,312,5,10,0,0,312,53,1,0,0,0,313,314,5,23,0,0,314,315,
        5,10,0,0,315,55,1,0,0,0,316,317,5,25,0,0,317,318,5,10,0,0,318,57,
        1,0,0,0,319,320,5,24,0,0,320,321,5,10,0,0,321,59,1,0,0,0,322,327,
        5,26,0,0,323,328,3,32,16,0,324,328,3,12,6,0,325,328,5,3,0,0,326,
        328,5,4,0,0,327,323,1,0,0,0,327,324,1,0,0,0,327,325,1,0,0,0,327,
        326,1,0,0,0,328,329,1,0,0,0,329,327,1,0,0,0,329,330,1,0,0,0,330,
        331,1,0,0,0,331,341,5,26,0,0,332,334,5,27,0,0,333,335,3,32,16,0,
        334,333,1,0,0,0,335,336,1,0,0,0,336,334,1,0,0,0,336,337,1,0,0,0,
        337,338,1,0,0,0,338,339,5,27,0,0,339,341,1,0,0,0,340,322,1,0,0,0,
        340,332,1,0,0,0,341,61,1,0,0,0,342,343,5,3,0,0,343,344,3,36,18,0,
        344,345,5,4,0,0,345,63,1,0,0,0,346,347,5,1,0,0,347,348,3,36,18,0,
        348,349,5,2,0,0,349,65,1,0,0,0,350,354,3,74,37,0,351,353,3,6,3,0,
        352,351,1,0,0,0,353,356,1,0,0,0,354,352,1,0,0,0,354,355,1,0,0,0,
        355,363,1,0,0,0,356,354,1,0,0,0,357,359,5,7,0,0,358,357,1,0,0,0,
        358,359,1,0,0,0,359,360,1,0,0,0,360,362,3,68,34,0,361,358,1,0,0,
        0,362,365,1,0,0,0,363,361,1,0,0,0,363,364,1,0,0,0,364,67,1,0,0,0,
        365,363,1,0,0,0,366,370,3,76,38,0,367,369,3,6,3,0,368,367,1,0,0,
        0,369,372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,379,1,0,0,
        0,372,370,1,0,0,0,373,375,5,7,0,0,374,373,1,0,0,0,374,375,1,0,0,
        0,375,376,1,0,0,0,376,378,3,70,35,0,377,374,1,0,0,0,378,381,1,0,
        0,0,379,377,1,0,0,0,379,380,1,0,0,0,380,69,1,0,0,0,381,379,1,0,0,
        0,382,386,3,78,39,0,383,385,3,6,3,0,384,383,1,0,0,0,385,388,1,0,
        0,0,386,384,1,0,0,0,386,387,1,0,0,0,387,395,1,0,0,0,388,386,1,0,
        0,0,389,391,5,7,0,0,390,389,1,0,0,0,390,391,1,0,0,0,391,392,1,0,
        0,0,392,394,3,72,36,0,393,390,1,0,0,0,394,397,1,0,0,0,395,393,1,
        0,0,0,395,396,1,0,0,0,396,71,1,0,0,0,397,395,1,0,0,0,398,402,3,80,
        40,0,399,401,3,6,3,0,400,399,1,0,0,0,401,404,1,0,0,0,402,400,1,0,
        0,0,402,403,1,0,0,0,403,73,1,0,0,0,404,402,1,0,0,0,405,406,5,22,
        0,0,406,407,5,22,0,0,407,408,5,22,0,0,408,409,5,22,0,0,409,410,5,
        22,0,0,410,411,5,22,0,0,411,412,5,22,0,0,412,413,5,22,0,0,413,414,
        5,22,0,0,414,415,3,28,14,0,415,416,5,7,0,0,416,75,1,0,0,0,417,418,
        5,5,0,0,418,419,3,28,14,0,419,420,5,7,0,0,420,77,1,0,0,0,421,422,
        5,6,0,0,422,423,3,28,14,0,423,424,5,7,0,0,424,79,1,0,0,0,425,426,
        5,14,0,0,426,427,5,14,0,0,427,428,5,14,0,0,428,429,3,28,14,0,429,
        430,5,7,0,0,430,81,1,0,0,0,49,86,91,97,103,106,113,117,124,129,136,
        142,154,164,175,190,193,197,202,207,217,222,226,228,233,238,240,
        243,246,254,265,271,279,287,298,308,327,329,336,340,354,358,363,
        370,374,379,386,390,395,402
    ]

class ZorgFileParser ( Parser ):

    grammarFileName = "ZorgFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'[['", "']]'", "'======='", 
                     "'*****'", "<INVALID>", "'o'", "'x'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'-'", "'.'", 
                     "'/'", "'_'", "':'", "' '", "'('", "')'", "'#'", "'@'", 
                     "'+'", "'%'", "'''", "'\"'", "'~'", "'*'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NL", "LOWER_O", 
                      "LOWER_X", "ID", "DATE", "NUM_ID", "SYMBOL", "DASH", 
                      "DOT", "FSLASH", "UNDERSCORE", "COLON", "SPACE", "LPAREN", 
                      "RPAREN", "HASH", "AT_SIGN", "PLUS", "PERCENT", "SQUOTE", 
                      "DQUOTE", "TILDE", "STAR", "LANGLE", "RANGLE" ]

    RULE_prog = 0
    RULE_head = 1
    RULE_comment = 2
    RULE_block = 3
    RULE_item = 4
    RULE_todo = 5
    RULE_priority = 6
    RULE_note = 7
    RULE_base_note = 8
    RULE_base_todo = 9
    RULE_subnote = 10
    RULE_subsubnote = 11
    RULE_item_body = 12
    RULE_footnote = 13
    RULE_space_atoms = 14
    RULE_space_atom = 15
    RULE_atom = 16
    RULE_property = 17
    RULE_id_group = 18
    RULE_id = 19
    RULE_date = 20
    RULE_any_symbol = 21
    RULE_non_tag_symbol = 22
    RULE_id_symbol = 23
    RULE_tag_symbol = 24
    RULE_tag = 25
    RULE_area = 26
    RULE_context = 27
    RULE_person = 28
    RULE_project = 29
    RULE_quoted = 30
    RULE_link = 31
    RULE_ref = 32
    RULE_h1_section = 33
    RULE_h2_section = 34
    RULE_h3_section = 35
    RULE_h4_section = 36
    RULE_h1_header = 37
    RULE_h2_header = 38
    RULE_h3_header = 39
    RULE_h4_header = 40

    ruleNames =  [ "prog", "head", "comment", "block", "item", "todo", "priority", 
                   "note", "base_note", "base_todo", "subnote", "subsubnote", 
                   "item_body", "footnote", "space_atoms", "space_atom", 
                   "atom", "property", "id_group", "id", "date", "any_symbol", 
                   "non_tag_symbol", "id_symbol", "tag_symbol", "tag", "area", 
                   "context", "person", "project", "quoted", "link", "ref", 
                   "h1_section", "h2_section", "h3_section", "h4_section", 
                   "h1_header", "h2_header", "h3_header", "h4_header" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NL=7
    LOWER_O=8
    LOWER_X=9
    ID=10
    DATE=11
    NUM_ID=12
    SYMBOL=13
    DASH=14
    DOT=15
    FSLASH=16
    UNDERSCORE=17
    COLON=18
    SPACE=19
    LPAREN=20
    RPAREN=21
    HASH=22
    AT_SIGN=23
    PLUS=24
    PERCENT=25
    SQUOTE=26
    DQUOTE=27
    TILDE=28
    STAR=29
    LANGLE=30
    RANGLE=31

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
            self.state = 82
            self.head()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 83
                    self.match(ZorgFileParser.NL)
                    self.state = 86 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==7):
                        break

                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 88
                        self.block() 
                    self.state = 93
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 94
                    self.h2_section()
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==22:
                    self.state = 100
                    self.h1_section()
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 108
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
            self.state = 111 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 110
                self.comment()
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
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
            self.state = 115
            self.match(ZorgFileParser.HASH)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 116
                self.space_atoms()


            self.state = 119
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


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.NL)
            else:
                return self.getToken(ZorgFileParser.NL, i)

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
            self.state = 122 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 121
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 124 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 126
                    self.match(ZorgFileParser.NL) 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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


        def footnote(self):
            return self.getTypedRuleContext(ZorgFileParser.FootnoteContext,0)


        def comment(self):
            return self.getTypedRuleContext(ZorgFileParser.CommentContext,0)


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
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.todo()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.note()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.footnote()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.comment()
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

        def base_todo(self):
            return self.getTypedRuleContext(ZorgFileParser.Base_todoContext,0)


        def subnote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.SubnoteContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.SubnoteContext,i)


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
            self.state = 138
            self.base_todo()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 139
                self.subnote()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 145
            self.match(ZorgFileParser.T__0)
            self.state = 146
            self.match(ZorgFileParser.HASH)
            self.state = 147
            self.match(ZorgFileParser.ID)
            self.state = 148
            self.match(ZorgFileParser.T__1)
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

        def base_note(self):
            return self.getTypedRuleContext(ZorgFileParser.Base_noteContext,0)


        def subnote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.SubnoteContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.SubnoteContext,i)


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
            self.state = 150
            self.base_note()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 151
                self.subnote()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_noteContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return ZorgFileParser.RULE_base_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_note" ):
                listener.enterBase_note(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_note" ):
                listener.exitBase_note(self)




    def base_note(self):

        localctx = ZorgFileParser.Base_noteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_base_note)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ZorgFileParser.DASH)
            self.state = 158
            self.item_body()
            self.state = 159
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_todoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item_body(self):
            return self.getTypedRuleContext(ZorgFileParser.Item_bodyContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def LOWER_O(self):
            return self.getToken(ZorgFileParser.LOWER_O, 0)

        def LOWER_X(self):
            return self.getToken(ZorgFileParser.LOWER_X, 0)

        def STAR(self):
            return self.getToken(ZorgFileParser.STAR, 0)

        def TILDE(self):
            return self.getToken(ZorgFileParser.TILDE, 0)

        def LANGLE(self):
            return self.getToken(ZorgFileParser.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(ZorgFileParser.RANGLE, 0)

        def SPACE(self):
            return self.getToken(ZorgFileParser.SPACE, 0)

        def priority(self):
            return self.getTypedRuleContext(ZorgFileParser.PriorityContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_base_todo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_todo" ):
                listener.enterBase_todo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_todo" ):
                listener.exitBase_todo(self)




    def base_todo(self):

        localctx = ZorgFileParser.Base_todoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_base_todo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026532608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 162
                self.match(ZorgFileParser.SPACE)
                self.state = 163
                self.priority()


            self.state = 166
            self.item_body()
            self.state = 167
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubnoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SPACE)
            else:
                return self.getToken(ZorgFileParser.SPACE, i)

        def base_note(self):
            return self.getTypedRuleContext(ZorgFileParser.Base_noteContext,0)


        def subsubnote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.SubsubnoteContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.SubsubnoteContext,i)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_subnote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubnote" ):
                listener.enterSubnote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubnote" ):
                listener.exitSubnote(self)




    def subnote(self):

        localctx = ZorgFileParser.SubnoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_subnote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ZorgFileParser.SPACE)
            self.state = 170
            self.match(ZorgFileParser.SPACE)
            self.state = 171
            self.base_note()
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    self.subsubnote() 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubsubnoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SPACE)
            else:
                return self.getToken(ZorgFileParser.SPACE, i)

        def base_note(self):
            return self.getTypedRuleContext(ZorgFileParser.Base_noteContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_subsubnote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubsubnote" ):
                listener.enterSubsubnote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubsubnote" ):
                listener.exitSubsubnote(self)




    def subsubnote(self):

        localctx = ZorgFileParser.SubsubnoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_subsubnote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ZorgFileParser.SPACE)
            self.state = 179
            self.match(ZorgFileParser.SPACE)
            self.state = 180
            self.match(ZorgFileParser.SPACE)
            self.state = 181
            self.match(ZorgFileParser.SPACE)
            self.state = 182
            self.base_note()
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

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


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

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.AtomContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.AtomContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.LPAREN)
            else:
                return self.getToken(ZorgFileParser.LPAREN, i)

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SYMBOL)
            else:
                return self.getToken(ZorgFileParser.SYMBOL, i)

        def space_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Space_atomContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Space_atomContext,i)


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
        self.enterRule(localctx, 24, self.RULE_item_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.space_atoms()
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    self.match(ZorgFileParser.NL)
                    self.state = 186
                    self.match(ZorgFileParser.SPACE)
                    self.state = 188 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 187
                        self.match(ZorgFileParser.SPACE)
                        self.state = 190 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==19):
                            break

                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 192
                        self.match(ZorgFileParser.LPAREN)


                    self.state = 195
                    self.atom()
                    self.state = 197
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==13:
                        self.state = 196
                        self.match(ZorgFileParser.SYMBOL)


                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==19:
                        self.state = 199
                        self.space_atom()
                        self.state = 204
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
             
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FootnoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ref(self):
            return self.getTypedRuleContext(ZorgFileParser.RefContext,0)


        def COLON(self):
            return self.getToken(ZorgFileParser.COLON, 0)

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_footnote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFootnote" ):
                listener.enterFootnote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFootnote" ):
                listener.exitFootnote(self)




    def footnote(self):

        localctx = ZorgFileParser.FootnoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_footnote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.ref()
            self.state = 211
            self.match(ZorgFileParser.COLON)
            self.state = 212
            self.space_atoms()
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
        self.enterRule(localctx, 28, self.RULE_space_atoms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 214
                self.space_atom()
                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==19):
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

        def SQUOTE(self):
            return self.getToken(ZorgFileParser.SQUOTE, 0)

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


        def ref(self):
            return self.getTypedRuleContext(ZorgFileParser.RefContext,0)


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
        self.enterRule(localctx, 30, self.RULE_space_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(ZorgFileParser.SPACE)
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 220
                self.match(ZorgFileParser.SQUOTE)
                self.state = 221
                self.non_tag_symbol()


            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 226
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [13, 14, 15, 16, 17, 18, 20, 21, 28, 29, 30, 31]:
                        self.state = 224
                        self.non_tag_symbol()
                        pass
                    elif token in [27]:
                        self.state = 225
                        self.match(ZorgFileParser.DQUOTE)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 231
                self.atom()

            elif la_ == 2:
                self.state = 232
                self.quoted()


            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 235
                self.any_symbol()
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 238
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]:
                            self.state = 236
                            self.any_symbol()
                            pass
                        elif token in [8, 9, 10, 11, 12]:
                            self.state = 237
                            self.id_()
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 242
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)



            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 245
                self.ref()


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


        def ref(self):
            return self.getTypedRuleContext(ZorgFileParser.RefContext,0)


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
        self.enterRule(localctx, 32, self.RULE_atom)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.tag_symbol()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.tag()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.link()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.property_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.id_group()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.ref()
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
        self.enterRule(localctx, 34, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ZorgFileParser.ID)
            self.state = 257
            self.match(ZorgFileParser.COLON)
            self.state = 258
            self.match(ZorgFileParser.COLON)
            self.state = 259
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
        self.enterRule(localctx, 36, self.RULE_id_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.id_()
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 263 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 262
                        self.id_symbol()
                        self.state = 265 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 376832) != 0)):
                            break

                    self.state = 267
                    self.id_() 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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


        def LOWER_O(self):
            return self.getToken(ZorgFileParser.LOWER_O, 0)

        def LOWER_X(self):
            return self.getToken(ZorgFileParser.LOWER_X, 0)

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
        self.enterRule(localctx, 38, self.RULE_id)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(ZorgFileParser.ID)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(ZorgFileParser.NUM_ID)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.date()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 277
                self.match(ZorgFileParser.LOWER_O)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 278
                self.match(ZorgFileParser.LOWER_X)
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
        self.enterRule(localctx, 40, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
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
        self.enterRule(localctx, 42, self.RULE_any_symbol)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(ZorgFileParser.SQUOTE)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.match(ZorgFileParser.DQUOTE)
                pass
            elif token in [13, 14, 15, 16, 17, 18, 20, 21, 28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.non_tag_symbol()
                pass
            elif token in [22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
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

        def LANGLE(self):
            return self.getToken(ZorgFileParser.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(ZorgFileParser.RANGLE, 0)

        def STAR(self):
            return self.getToken(ZorgFileParser.STAR, 0)

        def TILDE(self):
            return self.getToken(ZorgFileParser.TILDE, 0)

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
        self.enterRule(localctx, 44, self.RULE_non_tag_symbol)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(ZorgFileParser.LANGLE)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(ZorgFileParser.RANGLE)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.match(ZorgFileParser.STAR)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 292
                self.match(ZorgFileParser.TILDE)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 293
                self.match(ZorgFileParser.SYMBOL)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 6)
                self.state = 294
                self.match(ZorgFileParser.LPAREN)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 7)
                self.state = 295
                self.match(ZorgFileParser.RPAREN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 8)
                self.state = 296
                self.match(ZorgFileParser.UNDERSCORE)
                pass
            elif token in [14, 15, 16, 18]:
                self.enterOuterAlt(localctx, 9)
                self.state = 297
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
        self.enterRule(localctx, 46, self.RULE_id_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 376832) != 0)):
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
        self.enterRule(localctx, 48, self.RULE_tag_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
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
        self.enterRule(localctx, 50, self.RULE_tag)
        try:
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.area()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.context()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.person()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
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
        self.enterRule(localctx, 52, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(ZorgFileParser.HASH)
            self.state = 311
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
        self.enterRule(localctx, 54, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(ZorgFileParser.AT_SIGN)
            self.state = 314
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
        self.enterRule(localctx, 56, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ZorgFileParser.PERCENT)
            self.state = 317
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
        self.enterRule(localctx, 58, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZorgFileParser.PLUS)
            self.state = 320
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


        def priority(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.PriorityContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.PriorityContext,i)


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
        self.enterRule(localctx, 60, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 322
                self.match(ZorgFileParser.SQUOTE)
                self.state = 327 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 327
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 323
                        self.atom()
                        pass

                    elif la_ == 2:
                        self.state = 324
                        self.priority()
                        pass

                    elif la_ == 3:
                        self.state = 325
                        self.match(ZorgFileParser.T__2)
                        pass

                    elif la_ == 4:
                        self.state = 326
                        self.match(ZorgFileParser.T__3)
                        pass


                    self.state = 329 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 62922522) != 0)):
                        break

                self.state = 331
                self.match(ZorgFileParser.SQUOTE)
                pass
            elif token in [27]:
                self.state = 332
                self.match(ZorgFileParser.DQUOTE)
                self.state = 334 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 333
                    self.atom()
                    self.state = 336 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 62922506) != 0)):
                        break

                self.state = 338
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
        self.enterRule(localctx, 62, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZorgFileParser.T__2)
            self.state = 343
            self.id_group()
            self.state = 344
            self.match(ZorgFileParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_group(self):
            return self.getTypedRuleContext(ZorgFileParser.Id_groupContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRef" ):
                listener.enterRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRef" ):
                listener.exitRef(self)




    def ref(self):

        localctx = ZorgFileParser.RefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(ZorgFileParser.T__0)
            self.state = 347
            self.id_group()
            self.state = 348
            self.match(ZorgFileParser.T__1)
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
        self.enterRule(localctx, 66, self.RULE_h1_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.h1_header()
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 351
                    self.block() 
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==7:
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 357
                    self.match(ZorgFileParser.NL)


                self.state = 360
                self.h2_section()
                self.state = 365
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
        self.enterRule(localctx, 68, self.RULE_h2_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.h2_header()
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 367
                    self.block() 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 374
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==7:
                        self.state = 373
                        self.match(ZorgFileParser.NL)


                    self.state = 376
                    self.h3_section() 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_h3_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.h3_header()
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 383
                    self.block() 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 390
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==7:
                        self.state = 389
                        self.match(ZorgFileParser.NL)


                    self.state = 392
                    self.h4_section() 
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        self.enterRule(localctx, 72, self.RULE_h4_section)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.h4_header()
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 399
                    self.block() 
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        self.enterRule(localctx, 74, self.RULE_h1_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(ZorgFileParser.HASH)
            self.state = 406
            self.match(ZorgFileParser.HASH)
            self.state = 407
            self.match(ZorgFileParser.HASH)
            self.state = 408
            self.match(ZorgFileParser.HASH)
            self.state = 409
            self.match(ZorgFileParser.HASH)
            self.state = 410
            self.match(ZorgFileParser.HASH)
            self.state = 411
            self.match(ZorgFileParser.HASH)
            self.state = 412
            self.match(ZorgFileParser.HASH)
            self.state = 413
            self.match(ZorgFileParser.HASH)
            self.state = 414
            self.space_atoms()
            self.state = 415
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
        self.enterRule(localctx, 76, self.RULE_h2_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(ZorgFileParser.T__4)
            self.state = 418
            self.space_atoms()
            self.state = 419
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
        self.enterRule(localctx, 78, self.RULE_h3_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(ZorgFileParser.T__5)
            self.state = 422
            self.space_atoms()
            self.state = 423
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
        self.enterRule(localctx, 80, self.RULE_h4_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(ZorgFileParser.DASH)
            self.state = 426
            self.match(ZorgFileParser.DASH)
            self.state = 427
            self.match(ZorgFileParser.DASH)
            self.state = 428
            self.space_atoms()
            self.state = 429
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





