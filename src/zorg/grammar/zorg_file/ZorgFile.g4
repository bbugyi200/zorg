grammar ZorgFile;

// parser rules
prog      : head NL+ block* section* EOF ;
head      : comment+ ;
comment   : '# ' words NL
          | '#' NL
          ;
block     : (todo|note)+ NL? ;
section   : h1_header block+ ;
todo      : 'o ' words NL ;
note      : '- ' words NL ;
h1_header : '######### ' words NL ;
words     : ((WORD|CHAR) ' '?)+ ;

// lexer rules
NL             : '\r'? '\n' ;
CHAR           : ~[\r\n ] ;
WORD           : CHAR+ ;
