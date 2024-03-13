grammar ZorgFile;

// parser rules
prog       : head NL+ block* h1_section* EOF ;

head       : comment+ ;
comment    : '#' (' ' words)? NL ;

block      : (item)+ NL? ;
item       : (todo|note) ;
todo       : 'o ' words NL ;
note       : '- ' words NL ;
words      : (((WORD|CHAR)) ' '?)+ ;

tag        : (context|hash|person|project) ;
context    : '@' ID ;
hash       : '#' ID ;
person     : '%' ID ;
project    : '+' ID ;

h1_section : h1_header block+ (NL? h2_section)* ;
h2_section : h2_header block+ (NL? h3_section)* ;
h3_section : h3_header block+ (NL? h4_section)* ;
h4_section : h4_header block+ ;
h1_header  : '######### ' words NL ;
h2_header  : '======= ' words NL ;
h3_header  : '***** ' words NL ;
h4_header  : '--- ' words NL ;

// lexer rules
NL   : '\r'? '\n' ;
CHAR : ~[\r\n ] ;
WORD : CHAR+ ;
ID   : [A-Za-z/_.]+ ;
