grammar ZorgFile;

prog      : head NL+ block* section* EOF ;
head      : comment+ ;
comment   : '# ' (WORD ' '?)+ NL
          | '#' NL
          ;
block     : (todo|note)+ NL? ;
section   : h1_header block+ ;
todo      : 'o ' (WORD ' '?)+ NL ;
note      : '- ' (WORD ' '?)+ NL ;
h1_header : '######### ' (WORD ' '?)+ NL ;

NL             : '\r'? '\n' ;
CHAR           : ~[\r\n ] ;
WORD           : CHAR+ ;
