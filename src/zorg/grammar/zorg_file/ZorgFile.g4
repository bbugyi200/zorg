grammar ZorgFile;

prog    : head NEWLINE blocks NEWLINE (section)* ;
head    : COMMENT_LINE+ ;
blocks  : ANY_LINE* ;
section : H1_HEADER_LINE (todo|note)* ;
todo    :  ;
note    : '- ' ;

ANY_LINE       : ~([\r\n#]) ~([\r\n])* NEWLINE ;
COMMENT_LINE   : '# ' ~([\r\n])* NEWLINE ;
H1_HEADER_LINE : '######### ' ~([\r\n])* NEWLINE ;
NEWLINE        : [\r\n] ;
