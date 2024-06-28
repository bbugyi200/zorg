# Generated from ZorgFile.g4 by ANTLR 4.13.1
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
        4,1,46,502,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,1,0,1,0,3,
        0,107,8,0,1,0,1,0,1,1,4,1,112,8,1,11,1,12,1,113,1,2,1,2,3,2,118,
        8,2,1,2,1,2,1,3,4,3,123,8,3,11,3,12,3,124,1,3,5,3,128,8,3,10,3,12,
        3,131,9,3,1,3,5,3,134,8,3,10,3,12,3,137,9,3,1,3,5,3,140,8,3,10,3,
        12,3,143,9,3,1,4,4,4,146,8,4,11,4,12,4,147,1,4,5,4,151,8,4,10,4,
        12,4,154,9,4,1,5,1,5,1,5,1,5,3,5,160,8,5,1,6,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,4,9,176,8,9,11,9,12,9,177,1,9,5,
        9,181,8,9,10,9,12,9,184,9,9,1,10,1,10,1,11,1,11,1,11,3,11,191,8,
        11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,200,8,12,1,13,1,13,1,
        13,3,13,205,8,13,1,14,1,14,1,15,4,15,210,8,15,11,15,12,15,211,1,
        16,1,16,1,16,3,16,217,8,16,1,16,1,16,5,16,221,8,16,10,16,12,16,224,
        9,16,1,16,1,16,3,16,228,8,16,1,16,1,16,1,16,5,16,233,8,16,10,16,
        12,16,236,9,16,3,16,238,8,16,1,16,3,16,241,8,16,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,255,8,17,1,18,1,
        18,1,19,1,19,3,19,261,8,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,
        21,1,21,1,21,3,21,273,8,21,1,21,1,21,1,21,5,21,278,8,21,10,21,12,
        21,281,9,21,1,21,1,21,1,22,1,22,4,22,287,8,22,11,22,12,22,288,1,
        22,1,22,5,22,293,8,22,10,22,12,22,296,9,22,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,3,23,306,8,23,1,24,1,24,1,25,1,25,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,3,26,319,8,26,1,27,1,27,1,28,1,28,1,29,1,
        29,1,30,1,30,1,30,1,30,3,30,331,8,30,1,31,1,31,1,31,1,32,1,32,1,
        32,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,4,35,350,
        8,35,11,35,12,35,351,1,35,1,35,1,35,4,35,357,8,35,11,35,12,35,358,
        1,35,1,35,3,35,363,8,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,
        1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,
        1,41,1,41,1,41,1,42,1,42,1,42,1,42,5,42,393,8,42,10,42,12,42,396,
        9,42,1,42,1,42,1,42,1,42,1,42,3,42,403,8,42,1,43,1,43,5,43,407,8,
        43,10,43,12,43,410,9,43,1,43,5,43,413,8,43,10,43,12,43,416,9,43,
        1,43,3,43,419,8,43,1,43,5,43,422,8,43,10,43,12,43,425,9,43,1,44,
        1,44,5,44,429,8,44,10,44,12,44,432,9,44,1,44,5,44,435,8,44,10,44,
        12,44,438,9,44,1,44,3,44,441,8,44,1,44,5,44,444,8,44,10,44,12,44,
        447,9,44,1,45,1,45,5,45,451,8,45,10,45,12,45,454,9,45,1,45,5,45,
        457,8,45,10,45,12,45,460,9,45,1,45,3,45,463,8,45,1,45,5,45,466,8,
        45,10,45,12,45,469,9,45,1,46,1,46,5,46,473,8,46,10,46,12,46,476,
        9,46,1,46,5,46,479,8,46,10,46,12,46,482,9,46,1,47,1,47,1,47,1,47,
        1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,51,
        1,51,1,51,0,0,52,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,92,94,96,98,100,102,0,5,2,0,12,12,42,42,4,0,26,
        26,32,32,34,35,42,45,3,0,29,31,36,36,46,46,1,0,36,39,1,1,10,10,532,
        0,104,1,0,0,0,2,111,1,0,0,0,4,115,1,0,0,0,6,122,1,0,0,0,8,145,1,
        0,0,0,10,159,1,0,0,0,12,161,1,0,0,0,14,166,1,0,0,0,16,169,1,0,0,
        0,18,172,1,0,0,0,20,185,1,0,0,0,22,187,1,0,0,0,24,199,1,0,0,0,26,
        201,1,0,0,0,28,206,1,0,0,0,30,209,1,0,0,0,32,213,1,0,0,0,34,254,
        1,0,0,0,36,256,1,0,0,0,38,260,1,0,0,0,40,262,1,0,0,0,42,267,1,0,
        0,0,44,284,1,0,0,0,46,305,1,0,0,0,48,307,1,0,0,0,50,309,1,0,0,0,
        52,318,1,0,0,0,54,320,1,0,0,0,56,322,1,0,0,0,58,324,1,0,0,0,60,330,
        1,0,0,0,62,332,1,0,0,0,64,335,1,0,0,0,66,338,1,0,0,0,68,341,1,0,
        0,0,70,362,1,0,0,0,72,364,1,0,0,0,74,368,1,0,0,0,76,372,1,0,0,0,
        78,376,1,0,0,0,80,380,1,0,0,0,82,384,1,0,0,0,84,402,1,0,0,0,86,404,
        1,0,0,0,88,426,1,0,0,0,90,448,1,0,0,0,92,470,1,0,0,0,94,483,1,0,
        0,0,96,487,1,0,0,0,98,491,1,0,0,0,100,495,1,0,0,0,102,499,1,0,0,
        0,104,106,3,2,1,0,105,107,3,6,3,0,106,105,1,0,0,0,106,107,1,0,0,
        0,107,108,1,0,0,0,108,109,5,0,0,1,109,1,1,0,0,0,110,112,3,4,2,0,
        111,110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,
        114,3,1,0,0,0,115,117,5,36,0,0,116,118,3,30,15,0,117,116,1,0,0,0,
        117,118,1,0,0,0,118,119,1,0,0,0,119,120,5,10,0,0,120,5,1,0,0,0,121,
        123,5,10,0,0,122,121,1,0,0,0,123,124,1,0,0,0,124,122,1,0,0,0,124,
        125,1,0,0,0,125,129,1,0,0,0,126,128,3,8,4,0,127,126,1,0,0,0,128,
        131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,135,1,0,0,0,131,
        129,1,0,0,0,132,134,3,88,44,0,133,132,1,0,0,0,134,137,1,0,0,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,141,1,0,0,0,137,135,1,0,0,0,138,
        140,3,86,43,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,
        142,1,0,0,0,142,7,1,0,0,0,143,141,1,0,0,0,144,146,3,10,5,0,145,144,
        1,0,0,0,146,147,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,152,
        1,0,0,0,149,151,5,10,0,0,150,149,1,0,0,0,151,154,1,0,0,0,152,150,
        1,0,0,0,152,153,1,0,0,0,153,9,1,0,0,0,154,152,1,0,0,0,155,160,3,
        20,10,0,156,160,3,14,7,0,157,160,3,12,6,0,158,160,3,4,2,0,159,155,
        1,0,0,0,159,156,1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,11,1,
        0,0,0,161,162,3,84,42,0,162,163,5,46,0,0,163,164,3,30,15,0,164,165,
        5,10,0,0,165,13,1,0,0,0,166,167,5,29,0,0,167,168,3,16,8,0,168,15,
        1,0,0,0,169,170,3,18,9,0,170,171,5,10,0,0,171,17,1,0,0,0,172,182,
        3,30,15,0,173,175,5,10,0,0,174,176,5,33,0,0,175,174,1,0,0,0,176,
        177,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,
        181,3,30,15,0,180,173,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,
        183,1,0,0,0,183,19,1,0,0,0,184,182,1,0,0,0,185,186,3,22,11,0,186,
        21,1,0,0,0,187,190,3,24,12,0,188,189,5,33,0,0,189,191,3,28,14,0,
        190,188,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,3,18,9,0,
        193,194,5,10,0,0,194,23,1,0,0,0,195,200,5,11,0,0,196,200,3,26,13,
        0,197,200,5,44,0,0,198,200,5,45,0,0,199,195,1,0,0,0,199,196,1,0,
        0,0,199,197,1,0,0,0,199,198,1,0,0,0,200,25,1,0,0,0,201,204,7,0,0,
        0,202,203,5,46,0,0,203,205,3,50,25,0,204,202,1,0,0,0,204,205,1,0,
        0,0,205,27,1,0,0,0,206,207,5,15,0,0,207,29,1,0,0,0,208,210,3,32,
        16,0,209,208,1,0,0,0,210,211,1,0,0,0,211,209,1,0,0,0,211,212,1,0,
        0,0,212,31,1,0,0,0,213,216,5,33,0,0,214,215,5,40,0,0,215,217,3,54,
        27,0,216,214,1,0,0,0,216,217,1,0,0,0,217,222,1,0,0,0,218,221,3,54,
        27,0,219,221,5,41,0,0,220,218,1,0,0,0,220,219,1,0,0,0,221,224,1,
        0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,227,1,0,0,0,224,222,1,
        0,0,0,225,228,3,34,17,0,226,228,3,70,35,0,227,225,1,0,0,0,227,226,
        1,0,0,0,227,228,1,0,0,0,228,237,1,0,0,0,229,234,3,52,26,0,230,233,
        3,52,26,0,231,233,3,46,23,0,232,230,1,0,0,0,232,231,1,0,0,0,233,
        236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,238,1,0,0,0,236,
        234,1,0,0,0,237,229,1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,
        241,3,84,42,0,240,239,1,0,0,0,240,241,1,0,0,0,241,33,1,0,0,0,242,
        255,3,58,29,0,243,255,3,60,30,0,244,255,3,72,36,0,245,255,3,38,19,
        0,246,255,3,44,22,0,247,255,3,74,37,0,248,255,3,76,38,0,249,255,
        3,78,39,0,250,255,3,80,40,0,251,255,3,82,41,0,252,255,3,84,42,0,
        253,255,3,28,14,0,254,242,1,0,0,0,254,243,1,0,0,0,254,244,1,0,0,
        0,254,245,1,0,0,0,254,246,1,0,0,0,254,247,1,0,0,0,254,248,1,0,0,
        0,254,249,1,0,0,0,254,250,1,0,0,0,254,251,1,0,0,0,254,252,1,0,0,
        0,254,253,1,0,0,0,255,35,1,0,0,0,256,257,5,17,0,0,257,37,1,0,0,0,
        258,261,3,40,20,0,259,261,3,42,21,0,260,258,1,0,0,0,260,259,1,0,
        0,0,261,39,1,0,0,0,262,263,3,46,23,0,263,264,5,46,0,0,264,265,5,
        46,0,0,265,266,3,44,22,0,266,41,1,0,0,0,267,268,5,1,0,0,268,269,
        3,46,23,0,269,270,5,46,0,0,270,272,5,46,0,0,271,273,5,33,0,0,272,
        271,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,0,274,279,3,44,22,0,275,
        276,5,33,0,0,276,278,3,44,22,0,277,275,1,0,0,0,278,281,1,0,0,0,279,
        277,1,0,0,0,279,280,1,0,0,0,280,282,1,0,0,0,281,279,1,0,0,0,282,
        283,5,2,0,0,283,43,1,0,0,0,284,294,3,46,23,0,285,287,3,52,26,0,286,
        285,1,0,0,0,287,288,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,
        290,1,0,0,0,290,291,3,46,23,0,291,293,1,0,0,0,292,286,1,0,0,0,293,
        296,1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,45,1,0,0,0,296,294,
        1,0,0,0,297,306,5,16,0,0,298,306,5,18,0,0,299,306,5,15,0,0,300,306,
        3,48,24,0,301,306,3,50,25,0,302,306,3,36,18,0,303,306,5,11,0,0,304,
        306,5,12,0,0,305,297,1,0,0,0,305,298,1,0,0,0,305,299,1,0,0,0,305,
        300,1,0,0,0,305,301,1,0,0,0,305,302,1,0,0,0,305,303,1,0,0,0,305,
        304,1,0,0,0,306,47,1,0,0,0,307,308,5,13,0,0,308,49,1,0,0,0,309,310,
        5,14,0,0,310,51,1,0,0,0,311,319,5,40,0,0,312,319,5,41,0,0,313,319,
        5,28,0,0,314,319,5,27,0,0,315,319,3,54,27,0,316,319,3,58,29,0,317,
        319,3,56,28,0,318,311,1,0,0,0,318,312,1,0,0,0,318,313,1,0,0,0,318,
        314,1,0,0,0,318,315,1,0,0,0,318,316,1,0,0,0,318,317,1,0,0,0,319,
        53,1,0,0,0,320,321,7,1,0,0,321,55,1,0,0,0,322,323,7,2,0,0,323,57,
        1,0,0,0,324,325,7,3,0,0,325,59,1,0,0,0,326,331,3,62,31,0,327,331,
        3,64,32,0,328,331,3,66,33,0,329,331,3,68,34,0,330,326,1,0,0,0,330,
        327,1,0,0,0,330,328,1,0,0,0,330,329,1,0,0,0,331,61,1,0,0,0,332,333,
        5,36,0,0,333,334,3,46,23,0,334,63,1,0,0,0,335,336,5,37,0,0,336,337,
        3,46,23,0,337,65,1,0,0,0,338,339,5,39,0,0,339,340,3,46,23,0,340,
        67,1,0,0,0,341,342,5,38,0,0,342,343,3,46,23,0,343,69,1,0,0,0,344,
        349,5,40,0,0,345,350,3,34,17,0,346,350,3,28,14,0,347,350,5,3,0,0,
        348,350,5,4,0,0,349,345,1,0,0,0,349,346,1,0,0,0,349,347,1,0,0,0,
        349,348,1,0,0,0,350,351,1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,
        352,353,1,0,0,0,353,363,5,40,0,0,354,356,5,41,0,0,355,357,3,34,17,
        0,356,355,1,0,0,0,357,358,1,0,0,0,358,356,1,0,0,0,358,359,1,0,0,
        0,359,360,1,0,0,0,360,361,5,41,0,0,361,363,1,0,0,0,362,344,1,0,0,
        0,362,354,1,0,0,0,363,71,1,0,0,0,364,365,5,3,0,0,365,366,3,44,22,
        0,366,367,5,4,0,0,367,73,1,0,0,0,368,369,5,5,0,0,369,370,5,16,0,
        0,370,371,5,2,0,0,371,75,1,0,0,0,372,373,5,6,0,0,373,374,5,16,0,
        0,374,375,5,2,0,0,375,77,1,0,0,0,376,377,5,1,0,0,377,378,3,36,18,
        0,378,379,5,2,0,0,379,79,1,0,0,0,380,381,5,7,0,0,381,382,3,44,22,
        0,382,383,5,8,0,0,383,81,1,0,0,0,384,385,5,9,0,0,385,386,5,16,0,
        0,386,387,5,2,0,0,387,83,1,0,0,0,388,389,5,1,0,0,389,394,3,44,22,
        0,390,391,5,33,0,0,391,393,3,44,22,0,392,390,1,0,0,0,393,396,1,0,
        0,0,394,392,1,0,0,0,394,395,1,0,0,0,395,397,1,0,0,0,396,394,1,0,
        0,0,397,398,5,2,0,0,398,403,1,0,0,0,399,400,5,1,0,0,400,401,5,33,
        0,0,401,403,5,2,0,0,402,388,1,0,0,0,402,399,1,0,0,0,403,85,1,0,0,
        0,404,408,3,94,47,0,405,407,5,10,0,0,406,405,1,0,0,0,407,410,1,0,
        0,0,408,406,1,0,0,0,408,409,1,0,0,0,409,414,1,0,0,0,410,408,1,0,
        0,0,411,413,3,8,4,0,412,411,1,0,0,0,413,416,1,0,0,0,414,412,1,0,
        0,0,414,415,1,0,0,0,415,423,1,0,0,0,416,414,1,0,0,0,417,419,5,10,
        0,0,418,417,1,0,0,0,418,419,1,0,0,0,419,420,1,0,0,0,420,422,3,88,
        44,0,421,418,1,0,0,0,422,425,1,0,0,0,423,421,1,0,0,0,423,424,1,0,
        0,0,424,87,1,0,0,0,425,423,1,0,0,0,426,430,3,96,48,0,427,429,5,10,
        0,0,428,427,1,0,0,0,429,432,1,0,0,0,430,428,1,0,0,0,430,431,1,0,
        0,0,431,436,1,0,0,0,432,430,1,0,0,0,433,435,3,8,4,0,434,433,1,0,
        0,0,435,438,1,0,0,0,436,434,1,0,0,0,436,437,1,0,0,0,437,445,1,0,
        0,0,438,436,1,0,0,0,439,441,5,10,0,0,440,439,1,0,0,0,440,441,1,0,
        0,0,441,442,1,0,0,0,442,444,3,90,45,0,443,440,1,0,0,0,444,447,1,
        0,0,0,445,443,1,0,0,0,445,446,1,0,0,0,446,89,1,0,0,0,447,445,1,0,
        0,0,448,452,3,98,49,0,449,451,5,10,0,0,450,449,1,0,0,0,451,454,1,
        0,0,0,452,450,1,0,0,0,452,453,1,0,0,0,453,458,1,0,0,0,454,452,1,
        0,0,0,455,457,3,8,4,0,456,455,1,0,0,0,457,460,1,0,0,0,458,456,1,
        0,0,0,458,459,1,0,0,0,459,467,1,0,0,0,460,458,1,0,0,0,461,463,5,
        10,0,0,462,461,1,0,0,0,462,463,1,0,0,0,463,464,1,0,0,0,464,466,3,
        92,46,0,465,462,1,0,0,0,466,469,1,0,0,0,467,465,1,0,0,0,467,468,
        1,0,0,0,468,91,1,0,0,0,469,467,1,0,0,0,470,474,3,100,50,0,471,473,
        5,10,0,0,472,471,1,0,0,0,473,476,1,0,0,0,474,472,1,0,0,0,474,475,
        1,0,0,0,475,480,1,0,0,0,476,474,1,0,0,0,477,479,3,8,4,0,478,477,
        1,0,0,0,479,482,1,0,0,0,480,478,1,0,0,0,480,481,1,0,0,0,481,93,1,
        0,0,0,482,480,1,0,0,0,483,484,5,20,0,0,484,485,3,30,15,0,485,486,
        3,102,51,0,486,95,1,0,0,0,487,488,5,21,0,0,488,489,3,30,15,0,489,
        490,3,102,51,0,490,97,1,0,0,0,491,492,5,22,0,0,492,493,3,30,15,0,
        493,494,3,102,51,0,494,99,1,0,0,0,495,496,5,23,0,0,496,497,3,30,
        15,0,497,498,3,102,51,0,498,101,1,0,0,0,499,500,7,4,0,0,500,103,
        1,0,0,0,53,106,113,117,124,129,135,141,147,152,159,177,182,190,199,
        204,211,216,220,222,227,232,234,237,240,254,260,272,279,288,294,
        305,318,330,349,351,358,362,394,402,408,414,418,423,430,436,440,
        445,452,458,462,467,474,480
    ]

class ZorgFileParser ( Parser ):

    grammarFileName = "ZorgFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'[['", "']]'", "'[#'", 
                     "'[^'", "'(('", "'))'", "'[@'", "<INVALID>", "'o'", 
                     "'x'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'################################'", 
                     "'========================'", "'++++++++++++++++'", 
                     "'--------'", "'  -'", "'    -'", "<INVALID>", "'$'", 
                     "'^'", "'-'", "'.'", "'/'", "'_'", "' '", "'('", "')'", 
                     "'#'", "'@'", "'+'", "'%'", "'''", "'\"'", "'~'", "'*'", 
                     "'<'", "'>'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NL", "LOWER_O", "LOWER_X", 
                      "DATE", "TIME", "PRIORITY", "ID", "ZID", "NUM_ID", 
                      "SHORT_DATE", "H1_HEADER", "H2_HEADER", "H3_HEADER", 
                      "H4_HEADER", "TWO_SPACE_DASH", "FOUR_SPACE_DASH", 
                      "SYMBOL", "DOLLAR", "HAT", "DASH", "DOT", "FSLASH", 
                      "UNDERSCORE", "SPACE", "LPAREN", "RPAREN", "HASH", 
                      "AT_SIGN", "PLUS", "PERCENT", "SQUOTE", "DQUOTE", 
                      "TILDE", "STAR", "LANGLE", "RANGLE", "COLON" ]

    RULE_prog = 0
    RULE_head = 1
    RULE_comment = 2
    RULE_body = 3
    RULE_block = 4
    RULE_item = 5
    RULE_footnote = 6
    RULE_note = 7
    RULE_base_note = 8
    RULE_note_body = 9
    RULE_todo = 10
    RULE_base_todo = 11
    RULE_todo_prefix = 12
    RULE_x_or_tilde = 13
    RULE_priority = 14
    RULE_space_atoms = 15
    RULE_space_atom = 16
    RULE_atom = 17
    RULE_zid = 18
    RULE_property = 19
    RULE_simple_prop = 20
    RULE_inline_prop = 21
    RULE_id_group = 22
    RULE_id = 23
    RULE_date = 24
    RULE_time = 25
    RULE_any_symbol = 26
    RULE_non_tag_symbol = 27
    RULE_id_symbol = 28
    RULE_tag_symbol = 29
    RULE_tag = 30
    RULE_area = 31
    RULE_context = 32
    RULE_person = 33
    RULE_project = 34
    RULE_quoted = 35
    RULE_link = 36
    RULE_global_link = 37
    RULE_local_link = 38
    RULE_zid_link = 39
    RULE_embedded_link = 40
    RULE_ref_link = 41
    RULE_footnote_head = 42
    RULE_h1_section = 43
    RULE_h2_section = 44
    RULE_h3_section = 45
    RULE_h4_section = 46
    RULE_h1_header = 47
    RULE_h2_header = 48
    RULE_h3_header = 49
    RULE_h4_header = 50
    RULE_eol = 51

    ruleNames =  [ "prog", "head", "comment", "body", "block", "item", "footnote", 
                   "note", "base_note", "note_body", "todo", "base_todo", 
                   "todo_prefix", "x_or_tilde", "priority", "space_atoms", 
                   "space_atom", "atom", "zid", "property", "simple_prop", 
                   "inline_prop", "id_group", "id", "date", "time", "any_symbol", 
                   "non_tag_symbol", "id_symbol", "tag_symbol", "tag", "area", 
                   "context", "person", "project", "quoted", "link", "global_link", 
                   "local_link", "zid_link", "embedded_link", "ref_link", 
                   "footnote_head", "h1_section", "h2_section", "h3_section", 
                   "h4_section", "h1_header", "h2_header", "h3_header", 
                   "h4_header", "eol" ]

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
    LOWER_O=11
    LOWER_X=12
    DATE=13
    TIME=14
    PRIORITY=15
    ID=16
    ZID=17
    NUM_ID=18
    SHORT_DATE=19
    H1_HEADER=20
    H2_HEADER=21
    H3_HEADER=22
    H4_HEADER=23
    TWO_SPACE_DASH=24
    FOUR_SPACE_DASH=25
    SYMBOL=26
    DOLLAR=27
    HAT=28
    DASH=29
    DOT=30
    FSLASH=31
    UNDERSCORE=32
    SPACE=33
    LPAREN=34
    RPAREN=35
    HASH=36
    AT_SIGN=37
    PLUS=38
    PERCENT=39
    SQUOTE=40
    DQUOTE=41
    TILDE=42
    STAR=43
    LANGLE=44
    RANGLE=45
    COLON=46

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

        def body(self):
            return self.getTypedRuleContext(ZorgFileParser.BodyContext,0)


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
            self.state = 104
            self.head()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 105
                self.body()


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
                if not (_la==36):
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
            if _la==33:
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return ZorgFileParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = ZorgFileParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self.match(ZorgFileParser.NL)
                self.state = 124 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 57243860998146) != 0):
                self.state = 126
                self.block()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 132
                self.h2_section()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 138
                self.h1_section()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 144
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 147 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 149
                    self.match(ZorgFileParser.NL) 
                self.state = 154
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
        self.enterRule(localctx, 10, self.RULE_item)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 42, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.todo()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.note()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.footnote()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
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


    class FootnoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def footnote_head(self):
            return self.getTypedRuleContext(ZorgFileParser.Footnote_headContext,0)


        def COLON(self):
            return self.getToken(ZorgFileParser.COLON, 0)

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

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
        self.enterRule(localctx, 12, self.RULE_footnote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.footnote_head()
            self.state = 162
            self.match(ZorgFileParser.COLON)
            self.state = 163
            self.space_atoms()
            self.state = 164
            self.match(ZorgFileParser.NL)
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

        def base_note(self):
            return self.getTypedRuleContext(ZorgFileParser.Base_noteContext,0)


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
            self.state = 166
            self.match(ZorgFileParser.DASH)
            self.state = 167
            self.base_note()
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

        def note_body(self):
            return self.getTypedRuleContext(ZorgFileParser.Note_bodyContext,0)


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
            self.state = 169
            self.note_body()
            self.state = 170
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Note_bodyContext(ParserRuleContext):
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
            return ZorgFileParser.RULE_note_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote_body" ):
                listener.enterNote_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote_body" ):
                listener.exitNote_body(self)




    def note_body(self):

        localctx = ZorgFileParser.Note_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_note_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.space_atoms()
            self.state = 182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 173
                    self.match(ZorgFileParser.NL)
                    self.state = 175 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 174
                            self.match(ZorgFileParser.SPACE)

                        else:
                            raise NoViableAltException(self)
                        self.state = 177 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                    self.state = 179
                    self.space_atoms() 
                self.state = 184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_todo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.base_todo()
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

        def todo_prefix(self):
            return self.getTypedRuleContext(ZorgFileParser.Todo_prefixContext,0)


        def note_body(self):
            return self.getTypedRuleContext(ZorgFileParser.Note_bodyContext,0)


        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

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
        self.enterRule(localctx, 22, self.RULE_base_todo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.todo_prefix()
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 188
                self.match(ZorgFileParser.SPACE)
                self.state = 189
                self.priority()


            self.state = 192
            self.note_body()
            self.state = 193
            self.match(ZorgFileParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Todo_prefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWER_O(self):
            return self.getToken(ZorgFileParser.LOWER_O, 0)

        def x_or_tilde(self):
            return self.getTypedRuleContext(ZorgFileParser.X_or_tildeContext,0)


        def LANGLE(self):
            return self.getToken(ZorgFileParser.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(ZorgFileParser.RANGLE, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_todo_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo_prefix" ):
                listener.enterTodo_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo_prefix" ):
                listener.exitTodo_prefix(self)




    def todo_prefix(self):

        localctx = ZorgFileParser.Todo_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_todo_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 195
                self.match(ZorgFileParser.LOWER_O)
                pass
            elif token in [12, 42]:
                self.state = 196
                self.x_or_tilde()
                pass
            elif token in [44]:
                self.state = 197
                self.match(ZorgFileParser.LANGLE)
                pass
            elif token in [45]:
                self.state = 198
                self.match(ZorgFileParser.RANGLE)
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


    class X_or_tildeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWER_X(self):
            return self.getToken(ZorgFileParser.LOWER_X, 0)

        def TILDE(self):
            return self.getToken(ZorgFileParser.TILDE, 0)

        def COLON(self):
            return self.getToken(ZorgFileParser.COLON, 0)

        def time(self):
            return self.getTypedRuleContext(ZorgFileParser.TimeContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_x_or_tilde

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterX_or_tilde" ):
                listener.enterX_or_tilde(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitX_or_tilde" ):
                listener.exitX_or_tilde(self)




    def x_or_tilde(self):

        localctx = ZorgFileParser.X_or_tildeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_x_or_tilde)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==12 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 202
                self.match(ZorgFileParser.COLON)
                self.state = 203
                self.time()


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

        def PRIORITY(self):
            return self.getToken(ZorgFileParser.PRIORITY, 0)

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
        self.enterRule(localctx, 28, self.RULE_priority)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(ZorgFileParser.PRIORITY)
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
        self.enterRule(localctx, 30, self.RULE_space_atoms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 208
                self.space_atom()
                self.state = 211 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==33):
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


        def footnote_head(self):
            return self.getTypedRuleContext(ZorgFileParser.Footnote_headContext,0)


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
        self.enterRule(localctx, 32, self.RULE_space_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ZorgFileParser.SPACE)
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 214
                self.match(ZorgFileParser.SQUOTE)
                self.state = 215
                self.non_tag_symbol()


            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 220
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [26, 32, 34, 35, 42, 43, 44, 45]:
                        self.state = 218
                        self.non_tag_symbol()
                        pass
                    elif token in [41]:
                        self.state = 219
                        self.match(ZorgFileParser.DQUOTE)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 225
                self.atom()

            elif la_ == 2:
                self.state = 226
                self.quoted()


            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140728831311872) != 0):
                self.state = 229
                self.any_symbol()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140728831834112) != 0):
                    self.state = 232
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]:
                        self.state = 230
                        self.any_symbol()
                        pass
                    elif token in [11, 12, 13, 14, 15, 16, 17, 18]:
                        self.state = 231
                        self.id_()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 239
                self.footnote_head()


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


        def global_link(self):
            return self.getTypedRuleContext(ZorgFileParser.Global_linkContext,0)


        def local_link(self):
            return self.getTypedRuleContext(ZorgFileParser.Local_linkContext,0)


        def zid_link(self):
            return self.getTypedRuleContext(ZorgFileParser.Zid_linkContext,0)


        def embedded_link(self):
            return self.getTypedRuleContext(ZorgFileParser.Embedded_linkContext,0)


        def ref_link(self):
            return self.getTypedRuleContext(ZorgFileParser.Ref_linkContext,0)


        def footnote_head(self):
            return self.getTypedRuleContext(ZorgFileParser.Footnote_headContext,0)


        def priority(self):
            return self.getTypedRuleContext(ZorgFileParser.PriorityContext,0)


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
        self.enterRule(localctx, 34, self.RULE_atom)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.tag_symbol()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.tag()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.link()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 245
                self.property_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 246
                self.id_group()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 247
                self.global_link()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 248
                self.local_link()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 249
                self.zid_link()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 250
                self.embedded_link()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 251
                self.ref_link()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 252
                self.footnote_head()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 253
                self.priority()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ZidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZID(self):
            return self.getToken(ZorgFileParser.ZID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_zid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZid" ):
                listener.enterZid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZid" ):
                listener.exitZid(self)




    def zid(self):

        localctx = ZorgFileParser.ZidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_zid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ZorgFileParser.ZID)
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

        def simple_prop(self):
            return self.getTypedRuleContext(ZorgFileParser.Simple_propContext,0)


        def inline_prop(self):
            return self.getTypedRuleContext(ZorgFileParser.Inline_propContext,0)


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
        self.enterRule(localctx, 38, self.RULE_property)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.simple_prop()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.inline_prop()
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


    class Simple_propContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ZorgFileParser.IdContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.COLON)
            else:
                return self.getToken(ZorgFileParser.COLON, i)

        def id_group(self):
            return self.getTypedRuleContext(ZorgFileParser.Id_groupContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_simple_prop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_prop" ):
                listener.enterSimple_prop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_prop" ):
                listener.exitSimple_prop(self)




    def simple_prop(self):

        localctx = ZorgFileParser.Simple_propContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_simple_prop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.id_()
            self.state = 263
            self.match(ZorgFileParser.COLON)
            self.state = 264
            self.match(ZorgFileParser.COLON)
            self.state = 265
            self.id_group()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_propContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ZorgFileParser.IdContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.COLON)
            else:
                return self.getToken(ZorgFileParser.COLON, i)

        def id_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Id_groupContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Id_groupContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SPACE)
            else:
                return self.getToken(ZorgFileParser.SPACE, i)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_inline_prop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_prop" ):
                listener.enterInline_prop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_prop" ):
                listener.exitInline_prop(self)




    def inline_prop(self):

        localctx = ZorgFileParser.Inline_propContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_inline_prop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(ZorgFileParser.T__0)
            self.state = 268
            self.id_()
            self.state = 269
            self.match(ZorgFileParser.COLON)
            self.state = 270
            self.match(ZorgFileParser.COLON)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 271
                self.match(ZorgFileParser.SPACE)


            self.state = 274
            self.id_group()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 275
                self.match(ZorgFileParser.SPACE)
                self.state = 276
                self.id_group()
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
            self.match(ZorgFileParser.T__1)
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


        def any_symbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Any_symbolContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Any_symbolContext,i)


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
        self.enterRule(localctx, 44, self.RULE_id_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.id_()
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 286 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 285
                        self.any_symbol()
                        self.state = 288 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 140728831311872) != 0)):
                            break

                    self.state = 290
                    self.id_() 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def PRIORITY(self):
            return self.getToken(ZorgFileParser.PRIORITY, 0)

        def date(self):
            return self.getTypedRuleContext(ZorgFileParser.DateContext,0)


        def time(self):
            return self.getTypedRuleContext(ZorgFileParser.TimeContext,0)


        def zid(self):
            return self.getTypedRuleContext(ZorgFileParser.ZidContext,0)


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
        self.enterRule(localctx, 46, self.RULE_id)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(ZorgFileParser.ID)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(ZorgFileParser.NUM_ID)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.match(ZorgFileParser.PRIORITY)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 300
                self.date()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 301
                self.time()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 302
                self.zid()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 303
                self.match(ZorgFileParser.LOWER_O)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 8)
                self.state = 304
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
        self.enterRule(localctx, 48, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(ZorgFileParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME(self):
            return self.getToken(ZorgFileParser.TIME, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = ZorgFileParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(ZorgFileParser.TIME)
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

        def HAT(self):
            return self.getToken(ZorgFileParser.HAT, 0)

        def DOLLAR(self):
            return self.getToken(ZorgFileParser.DOLLAR, 0)

        def non_tag_symbol(self):
            return self.getTypedRuleContext(ZorgFileParser.Non_tag_symbolContext,0)


        def tag_symbol(self):
            return self.getTypedRuleContext(ZorgFileParser.Tag_symbolContext,0)


        def id_symbol(self):
            return self.getTypedRuleContext(ZorgFileParser.Id_symbolContext,0)


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
        self.enterRule(localctx, 52, self.RULE_any_symbol)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(ZorgFileParser.SQUOTE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(ZorgFileParser.DQUOTE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 313
                self.match(ZorgFileParser.HAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 314
                self.match(ZorgFileParser.DOLLAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 315
                self.non_tag_symbol()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 316
                self.tag_symbol()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 317
                self.id_symbol()
                pass


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
        self.enterRule(localctx, 54, self.RULE_non_tag_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66026599350272) != 0)):
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


    class Id_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(ZorgFileParser.HASH, 0)

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
        self.enterRule(localctx, 56, self.RULE_id_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70441221750784) != 0)):
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
        self.enterRule(localctx, 58, self.RULE_tag_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1030792151040) != 0)):
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
        self.enterRule(localctx, 60, self.RULE_tag)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.area()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.context()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.person()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 4)
                self.state = 329
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

        def id_(self):
            return self.getTypedRuleContext(ZorgFileParser.IdContext,0)


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
        self.enterRule(localctx, 62, self.RULE_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(ZorgFileParser.HASH)
            self.state = 333
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
            return self.getToken(ZorgFileParser.AT_SIGN, 0)

        def id_(self):
            return self.getTypedRuleContext(ZorgFileParser.IdContext,0)


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
        self.enterRule(localctx, 64, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(ZorgFileParser.AT_SIGN)
            self.state = 336
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
            return self.getToken(ZorgFileParser.PERCENT, 0)

        def id_(self):
            return self.getTypedRuleContext(ZorgFileParser.IdContext,0)


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
        self.enterRule(localctx, 66, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZorgFileParser.PERCENT)
            self.state = 339
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
            return self.getToken(ZorgFileParser.PLUS, 0)

        def id_(self):
            return self.getTypedRuleContext(ZorgFileParser.IdContext,0)


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
        self.enterRule(localctx, 68, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(ZorgFileParser.PLUS)
            self.state = 342
            self.id_()
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
        self.enterRule(localctx, 70, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.state = 344
                self.match(ZorgFileParser.SQUOTE)
                self.state = 349 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 349
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        self.state = 345
                        self.atom()
                        pass

                    elif la_ == 2:
                        self.state = 346
                        self.priority()
                        pass

                    elif la_ == 3:
                        self.state = 347
                        self.match(ZorgFileParser.T__2)
                        pass

                    elif la_ == 4:
                        self.state = 348
                        self.match(ZorgFileParser.T__3)
                        pass


                    self.state = 351 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1030792674042) != 0)):
                        break

                self.state = 353
                self.match(ZorgFileParser.SQUOTE)
                pass
            elif token in [41]:
                self.state = 354
                self.match(ZorgFileParser.DQUOTE)
                self.state = 356 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 355
                    self.atom()
                    self.state = 358 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1030792674026) != 0)):
                        break

                self.state = 360
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
        self.enterRule(localctx, 72, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(ZorgFileParser.T__2)
            self.state = 365
            self.id_group()
            self.state = 366
            self.match(ZorgFileParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_linkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_global_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_link" ):
                listener.enterGlobal_link(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_link" ):
                listener.exitGlobal_link(self)




    def global_link(self):

        localctx = ZorgFileParser.Global_linkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_global_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZorgFileParser.T__4)
            self.state = 369
            self.match(ZorgFileParser.ID)
            self.state = 370
            self.match(ZorgFileParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_linkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_local_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_link" ):
                listener.enterLocal_link(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_link" ):
                listener.exitLocal_link(self)




    def local_link(self):

        localctx = ZorgFileParser.Local_linkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_local_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(ZorgFileParser.T__5)
            self.state = 373
            self.match(ZorgFileParser.ID)
            self.state = 374
            self.match(ZorgFileParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Zid_linkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def zid(self):
            return self.getTypedRuleContext(ZorgFileParser.ZidContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_zid_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZid_link" ):
                listener.enterZid_link(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZid_link" ):
                listener.exitZid_link(self)




    def zid_link(self):

        localctx = ZorgFileParser.Zid_linkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_zid_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(ZorgFileParser.T__0)
            self.state = 377
            self.zid()
            self.state = 378
            self.match(ZorgFileParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Embedded_linkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_group(self):
            return self.getTypedRuleContext(ZorgFileParser.Id_groupContext,0)


        def getRuleIndex(self):
            return ZorgFileParser.RULE_embedded_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmbedded_link" ):
                listener.enterEmbedded_link(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmbedded_link" ):
                listener.exitEmbedded_link(self)




    def embedded_link(self):

        localctx = ZorgFileParser.Embedded_linkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_embedded_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ZorgFileParser.T__6)
            self.state = 381
            self.id_group()
            self.state = 382
            self.match(ZorgFileParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ref_linkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZorgFileParser.ID, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_ref_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRef_link" ):
                listener.enterRef_link(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRef_link" ):
                listener.exitRef_link(self)




    def ref_link(self):

        localctx = ZorgFileParser.Ref_linkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ref_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(ZorgFileParser.T__8)
            self.state = 385
            self.match(ZorgFileParser.ID)
            self.state = 386
            self.match(ZorgFileParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Footnote_headContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.Id_groupContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.Id_groupContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ZorgFileParser.SPACE)
            else:
                return self.getToken(ZorgFileParser.SPACE, i)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_footnote_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFootnote_head" ):
                listener.enterFootnote_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFootnote_head" ):
                listener.exitFootnote_head(self)




    def footnote_head(self):

        localctx = ZorgFileParser.Footnote_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_footnote_head)
        self._la = 0 # Token type
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(ZorgFileParser.T__0)
                self.state = 389
                self.id_group()
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==33:
                    self.state = 390
                    self.match(ZorgFileParser.SPACE)
                    self.state = 391
                    self.id_group()
                    self.state = 396
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 397
                self.match(ZorgFileParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.match(ZorgFileParser.T__0)
                self.state = 400
                self.match(ZorgFileParser.SPACE)
                self.state = 401
                self.match(ZorgFileParser.T__1)
                pass


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
        self.enterRule(localctx, 86, self.RULE_h1_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.h1_header()
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 405
                    self.match(ZorgFileParser.NL) 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 57243860998146) != 0):
                self.state = 411
                self.block()
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==21:
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 417
                    self.match(ZorgFileParser.NL)


                self.state = 420
                self.h2_section()
                self.state = 425
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


        def h3_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.H3_sectionContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.H3_sectionContext,i)


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
        self.enterRule(localctx, 88, self.RULE_h2_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.h2_header()
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 427
                    self.match(ZorgFileParser.NL) 
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 57243860998146) != 0):
                self.state = 433
                self.block()
                self.state = 438
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 445
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 440
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 439
                        self.match(ZorgFileParser.NL)


                    self.state = 442
                    self.h3_section() 
                self.state = 447
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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


        def h4_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZorgFileParser.H4_sectionContext)
            else:
                return self.getTypedRuleContext(ZorgFileParser.H4_sectionContext,i)


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
        self.enterRule(localctx, 90, self.RULE_h3_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.h3_header()
            self.state = 452
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 449
                    self.match(ZorgFileParser.NL) 
                self.state = 454
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 57243860998146) != 0):
                self.state = 455
                self.block()
                self.state = 460
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 467
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 462
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 461
                        self.match(ZorgFileParser.NL)


                    self.state = 464
                    self.h4_section() 
                self.state = 469
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        self.enterRule(localctx, 92, self.RULE_h4_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.h4_header()
            self.state = 474
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 471
                    self.match(ZorgFileParser.NL) 
                self.state = 476
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 57243860998146) != 0):
                self.state = 477
                self.block()
                self.state = 482
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

        def H1_HEADER(self):
            return self.getToken(ZorgFileParser.H1_HEADER, 0)

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def eol(self):
            return self.getTypedRuleContext(ZorgFileParser.EolContext,0)


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
        self.enterRule(localctx, 94, self.RULE_h1_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(ZorgFileParser.H1_HEADER)
            self.state = 484
            self.space_atoms()
            self.state = 485
            self.eol()
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

        def H2_HEADER(self):
            return self.getToken(ZorgFileParser.H2_HEADER, 0)

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def eol(self):
            return self.getTypedRuleContext(ZorgFileParser.EolContext,0)


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
        self.enterRule(localctx, 96, self.RULE_h2_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(ZorgFileParser.H2_HEADER)
            self.state = 488
            self.space_atoms()
            self.state = 489
            self.eol()
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

        def H3_HEADER(self):
            return self.getToken(ZorgFileParser.H3_HEADER, 0)

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def eol(self):
            return self.getTypedRuleContext(ZorgFileParser.EolContext,0)


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
        self.enterRule(localctx, 98, self.RULE_h3_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(ZorgFileParser.H3_HEADER)
            self.state = 492
            self.space_atoms()
            self.state = 493
            self.eol()
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

        def H4_HEADER(self):
            return self.getToken(ZorgFileParser.H4_HEADER, 0)

        def space_atoms(self):
            return self.getTypedRuleContext(ZorgFileParser.Space_atomsContext,0)


        def eol(self):
            return self.getTypedRuleContext(ZorgFileParser.EolContext,0)


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
        self.enterRule(localctx, 100, self.RULE_h4_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(ZorgFileParser.H4_HEADER)
            self.state = 496
            self.space_atoms()
            self.state = 497
            self.eol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(ZorgFileParser.NL, 0)

        def EOF(self):
            return self.getToken(ZorgFileParser.EOF, 0)

        def getRuleIndex(self):
            return ZorgFileParser.RULE_eol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEol" ):
                listener.enterEol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEol" ):
                listener.exitEol(self)




    def eol(self):

        localctx = ZorgFileParser.EolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_eol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            _la = self._input.LA(1)
            if not(_la==-1 or _la==10):
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





