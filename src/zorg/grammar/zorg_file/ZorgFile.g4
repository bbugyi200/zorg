grammar ZorgFile;

//// parser rules
prog       : head (NL+ block* h2_section* h1_section*)? EOF ;

// header
head       : comment+ ;
comment    : HASH space_atoms? NL ;

// block
block      : item+ NL? ;
item       : todo | note ;
todo       : (SPACE SPACE)* 'o' (' ' priority)? space_atoms NL ;
priority   : '[' HASH ID ']' ;
note       : (SPACE SPACE)* DASH space_atoms NL ;

// atoms
space_atoms : space_atom+ ;
space_atom  : SPACE (non_tag_symbol | DQUOTE)* (atom | quoted)? (any_symbol (any_symbol | ID)*)? ;
atom        : tag_symbol | tag | link | property | id_group ;

// property
property    : ID '::' id_group ;
id_group    : ID (id_symbol+ ID)* ;

// symbols
any_symbol     : SQUOTE | DQUOTE | non_tag_symbol | tag_symbol ;
non_tag_symbol : SYMBOL | LPAREN | RPAREN | UNDERSCORE | id_symbol ;
id_symbol      : DASH | DOT | FSLASH | COLON ;
tag_symbol     : HASH | AT_SIGN | PERCENT | PLUS ;

// tag
tag        : area | context | person | project ;
area       : HASH ID ;
context    : AT_SIGN ID ;
person     : PERCENT ID ;
project    : PLUS ID ;

// quotes and links
quoted     : (SQUOTE atom+ SQUOTE | DQUOTE atom+ DQUOTE) ;
link       : '[[' (id_group|property) ']]' ;

// sections
h1_section : h1_header block* (NL? h2_section)* ;
h2_section : h2_header block* (NL? h3_section)* ;
h3_section : h3_header block* (NL? h4_section)* ;
h4_section : h4_header block* ;
h1_header  : HASH HASH HASH HASH HASH HASH HASH HASH HASH space_atoms NL ;
h2_header  : '=======' space_atoms NL ;
h3_header  : '*****' space_atoms NL ;
h4_header  : DASH DASH DASH space_atoms NL ;

//// lexer rules
NL           : '\r'? '\n' ;
ID           : (ALPHANUM|UNDERSCORE)+ ;
SYMBOL       : [^[\]<>,?!;|=\\] ;
DASH         : '-' ;
DOT          : '.' ;
FSLASH       : '/' ;
UNDERSCORE   : '_' ;
COLON        : ':' ;
SPACE        : ' ' ;
LPAREN       : '(' ;
RPAREN       : ')' ;
HASH         : '#' ;
AT_SIGN      : '@' ;
PLUS         : '+' ;
PERCENT      : '%' ;
SQUOTE       : '\'' ;
DQUOTE       : '"' ;

//// fragments
fragment UPPER_LETTER : 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J'|'K'|'L'|'M'|'N'|'O'|'P'|'Q'|'R'|'S'|'T'|'U'|'V'|'W'|'X'|'Y'|'Z' ;
fragment LOWER_LETTER : 'a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'|'i'|'j'|'k'|'l'|'m'|'n'|'o'|'p'|'q'|'r'|'s'|'t'|'u'|'v'|'w'|'x'|'y'|'z' ;
fragment DIGIT        : '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' ;
fragment LETTER       : UPPER_LETTER | LOWER_LETTER ;
fragment ALPHANUM     : LETTER | DIGIT ;
