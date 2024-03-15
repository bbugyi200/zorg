grammar ZorgFile;

// parser rules
prog       : head NL+ block* h1_section* EOF ;

head       : comment+ ;
comment    : '#' space_atoms? NL ;

block      : item+ NL? ;
item       : (todo|note) ;
todo       : 'o' (' ' priority)? space_atoms NL ;
priority   : '[#' ID ']' ;
note       : '-' space_atoms NL ;

space_atoms : space_atom+ ;
space_atom  : ' ' (tag|property|ID)? SYMBOL* ;
property    : ID '::' ID ;

tag        : (area|context|person|project) ;
area       : '#' ID ;
context    : '@' ID ;
person     : '%' ID ;
project    : '+' ID ;

h1_section : h1_header block+ (NL? h2_section)* ;
h2_section : h2_header block+ (NL? h3_section)* ;
h3_section : h3_header block+ (NL? h4_section)* ;
h4_section : h4_header block+ ;
h1_header  : '#########' space_atoms NL ;
h2_header  : '=======' space_atoms NL ;
h3_header  : '*****' space_atoms NL ;
h4_header  : '---' space_atoms NL ;

// lexer rules
NL           : '\r'? '\n' ;
ID           : ALPANUM+ (ID_SYMBOL ALPANUM*)* ;
SYMBOL       : ([(),?!;:|]|ID_SYMBOL) ;

// fragments
fragment UPPER_LETTER : ('A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J'|'K'|'L'|'M'|'N'|'O'|'P'|'Q'|'R'|'S'|'T'|'U'|'V'|'W'|'X'|'Y'|'Z') ;
fragment LOWER_LETTER : ('a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'|'i'|'j'|'k'|'l'|'m'|'n'|'o'|'p'|'q'|'r'|'s'|'t'|'u'|'v'|'w'|'x'|'y'|'z') ;
fragment DIGIT        : ('0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9') ;
fragment LETTER       : (UPPER_LETTER|LOWER_LETTER) ;
fragment ALPANUM      : (LETTER|DIGIT) ;

fragment DASH         : '-' ;
fragment DOT          : '.' ;
fragment SLASH        : '/' ;
fragment UNDERSCORE   : '_' ;
fragment ID_SYMBOL    : (DASH|DOT|SLASH|UNDERSCORE) ;
