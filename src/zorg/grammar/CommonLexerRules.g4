lexer grammar CommonLexerRules;

//// lexer rules
NL : '\r'? '\n' ;
LOWER_O : 'o' ;
LOWER_X : 'x' ;
DATE : '2' NUM NUM NUM DASH FIRST_M_NUM NUM DASH FIRST_D_NUM NUM ;
TIME : ('0' | '1' | '2') NUM ('0' | '1' | '2' | '3' | '4' | '5') NUM ;
ID : ALPHANUM (ALPHANUM|UNDERSCORE)* ;
ZID : NUM NUM FIRST_M_NUM NUM FIRST_D_NUM NUM HASH ZID_CHAR ZID_CHAR ZID_CHAR? ;
NUM_ID : NUM (ALPHANUM|UNDERSCORE)* ;
TWO_SPACE_DASH : '  -' ;
FOUR_SPACE_DASH : '    -' ;
SYMBOL : [^[\],?!;|=\\`{}$&] ;
DASH : '-' ;
DOT : '.' ;
FSLASH : '/' ;
UNDERSCORE : '_' ;
COLON : ':' ;
SPACE : ' ' ;
LPAREN : '(' ;
RPAREN : ')' ;
HASH : '#' ;
AT_SIGN : '@' ;
PLUS : '+' ;
PERCENT : '%' ;
SQUOTE : '\'' ;
DQUOTE : '"' ;
TILDE : '~' ;
STAR : '*' ;
LANGLE : '<' ;
RANGLE : '>' ;

//// fragments
fragment UPPER_LETTER : 'A'..'Z' ;
fragment LOWER_LETTER : 'a'..'z' ;
// ZID_CHAR: Any digit OR any letter NOT in ('I', 'O', 'j', 'l')
fragment ZID_CHAR : NUM | 'A'..'H' | 'J'..'N' | 'P'..'Z' | 'a'..'i' | 'k' | 'm'..'z' ;
fragment NUM          : '0'..'9' ;
fragment FIRST_D_NUM : '0' | '1' | '2' | '3' ;
fragment FIRST_M_NUM : '0' | '1' ;
fragment ALPHA        : UPPER_LETTER | LOWER_LETTER ;
fragment ALPHANUM     : ALPHA | NUM ;
