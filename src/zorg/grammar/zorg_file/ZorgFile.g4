grammar ZorgFile;

//// parser rules
prog       : head (NL+ block* h2_section* h1_section*)? EOF ;

// header
head       : comment+ ;
comment    : HASH space_atoms? NL ;

// block
block      : item+ NL* ;
item       : todo | note | footnote | comment ;
todo       : base_todo subnote* ;
base_todo  : (LOWER_O | x_or_tilde | LANGLE | RANGLE) (' ' priority)? note_body NL ;
x_or_tilde : (LOWER_X | TILDE) (COLON time)? ;
priority   : '[' HASH ID ']' ;
note       : DASH base_note subnote* ;
base_note  : note_body NL ;
subnote    : TWO_SPACE_DASH base_note subsubnote*;
subsubnote : FOUR_SPACE_DASH base_note ;
note_body  : space_atoms (NL SPACE+ space_atoms)* ;
footnote   : ref COLON space_atoms ;

// atoms
space_atoms : space_atom+ ;
space_atom  : SPACE (SQUOTE non_tag_symbol)? (non_tag_symbol | DQUOTE)* (atom | quoted)? (any_symbol (any_symbol | id)*)? ref? ;
atom        : tag_symbol | tag | link | property | id_group | ref ;

// property
property    : ID COLON COLON id_group ;
id_group    : id (id_symbol+ id)* ;
id          : ID | NUM_ID | date | time | LOWER_O | LOWER_X ;
date        : DATE ;
time        : TIME ;

// symbols
any_symbol     : SQUOTE | DQUOTE | non_tag_symbol | tag_symbol | id_symbol ;
non_tag_symbol : LANGLE | RANGLE | STAR | TILDE | SYMBOL | LPAREN | RPAREN | UNDERSCORE ;
id_symbol      : DASH | DOT | FSLASH | COLON ;
tag_symbol     : HASH | AT_SIGN | PERCENT | PLUS ;

// tag
tag        : area | context | person | project ;
area       : HASH ID ;
context    : AT_SIGN ID ;
person     : PERCENT ID ;
project    : PLUS ID ;

// quotes and links
quoted     : (SQUOTE (atom | priority | '[[' | ']]')+ SQUOTE | DQUOTE atom+ DQUOTE) ;
link       : '[[' id_group ']]' ;
ref        : '[' id_group ']' ;

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
LOWER_O      : 'o' ;
LOWER_X      : 'x' ;
ID           : ALPHA (ALPHANUM|UNDERSCORE)* ;
DATE         : '2' NUM NUM NUM DASH ('0' | '1') NUM DASH ('0' | '1' | '2' | '3') NUM ;
TIME         : ('0' | '1' | '2') NUM ('0' | '1' | '2' | '3' | '4' | '5') NUM ;
NUM_ID       : NUM (ALPHANUM|UNDERSCORE)* ;
TWO_SPACE_DASH : '  -' ;
FOUR_SPACE_DASH : '    -' ;
SYMBOL       : [^[\],?!;|=\\`{}$&] ;
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
TILDE        : '~' ;
STAR         : '*' ;
LANGLE       : '<' ;
RANGLE       : '>' ;

//// fragments
fragment UPPER_LETTER : 'A'..'Z' ;
fragment LOWER_LETTER : 'a'..'z' ;
fragment NUM          : '0'..'9' ;
fragment ALPHA        : UPPER_LETTER | LOWER_LETTER ;
fragment ALPHANUM     : ALPHA | NUM ;
