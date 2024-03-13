grammar ZorgFile;

// parser rules
prog       : head NL+ block* h1_section* EOF ;

head       : comment+ ;
comment    : '#' atoms? NL ;

block      : item+ NL? ;
item       : (todo|note) ;
todo       : 'o' atoms NL ;
note       : '-' atoms NL ;
atom       : (' ' tag|WORD) ;
atoms      : atom+ ;

tag        : (context|hash|person|project) SYMBOL?;
context    : '@' ID ;
hash       : '#' ID ;
person     : '%' ID ;
project    : '+' ID ;

h1_section : h1_header block+ (NL? h2_section)* ;
h2_section : h2_header block+ (NL? h3_section)* ;
h3_section : h3_header block+ (NL? h4_section)* ;
h4_section : h4_header block+ ;
h1_header  : '#########' atoms NL ;
h2_header  : '=======' atoms NL ;
h3_header  : '*****' atoms NL ;
h4_header  : '---' atoms NL ;

// lexer rules
NL     : '\r'? '\n' ;
WORD   : ' ' ~[@#%+\r\n ] NON_WS_CHAR* ;
ID     : (LETTER | DIGIT | SLASH)+ ;
SYMBOL : [),.?!;:] ;

// fragments
fragment NON_WS_CHAR : ~[\r\n ] ;
fragment LETTER      : [A-Za-z] ;
fragment DIGIT       : [0-9] ;
fragment SLASH       : '/' ;
