grammar ZorgFile;

// parser rules
prog       : head NL+ block* h1_section* EOF ;

head       : comment+ ;
comment    : '#' (' ' words)? NL ;

block      : (todo|note)+ NL? ;
todo       : 'o ' words NL ;
note       : '- ' words NL ;
words      : ((WORD|CHAR) ' '?)+ ;

h1_section : h1_header block+ (NL? h2_section)* ;
h2_section : h2_header block+ (NL? h3_section)* ;
h3_section : h3_header block+ (NL? h4_section)* ;
h4_section : h4_header block+ (NL? h5_section)* ;
h5_section : h5_header block+ ;
h1_header  : '######### ' words NL ;
h2_header  : '======= ' words NL ;
h3_header  : '***** ' words NL ;
h4_header  : '@@@ ' words NL ;
h5_header  : '-- ' words NL ;

// lexer rules
NL             : '\r'? '\n' ;
CHAR           : ~[\r\n ] ;
WORD           : CHAR+ ;
