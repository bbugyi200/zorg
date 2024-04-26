grammar ZorgFile;

//// parser rules
prog       : head (NL+ block* h2_section* h1_section*)? EOF ;

// header
head       : comment+ ;
comment    : HASH space_atoms? NL ;

// blocks
block       : item+ NL* ;
item        : todo | note | footnote | comment ;
footnote    : ref COLON space_atoms NL ;

// notes
note        : DASH base_note subnote* ;
base_note   : id_note_body NL ;
id_note_body : (SPACE zid)? note_body ;
note_body   : space_atoms (NL SPACE+ space_atoms)* ;
subnote     : TWO_SPACE_DASH base_note subsubnote*;
subsubnote  : FOUR_SPACE_DASH base_note ;

// todos
todo        : base_todo subnote* ;
base_todo   : todo_prefix (SPACE priority)? id_note_body NL ;
todo_prefix : (LOWER_O | x_or_tilde | LANGLE | RANGLE) ;
x_or_tilde  : (LOWER_X | TILDE) (COLON time)? ;
priority    : '[' HASH ID ']' ;

// Zorg YYMMDD#XX IDs
zid : ZID ;

// atoms
space_atoms : space_atom+ ;
space_atom  : SPACE (SQUOTE non_tag_symbol)? (non_tag_symbol | DQUOTE)* (atom | quoted)? (any_symbol (any_symbol | id)*)? ref? ;
atom        : tag_symbol | tag | link | property | id_group | ref | zid | priority ;

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
h1_section : h1_header NL* block* (NL? h2_section)* ;
h2_section : h2_header NL* block* (NL? h3_section)* ;
h3_section : h3_header NL* block* (NL? h4_section)* ;
h4_section : h4_header NL* block* ;
h1_header  : HASH HASH HASH HASH HASH HASH HASH HASH HASH space_atoms eol ;
h2_header  : '=======' space_atoms eol ;
h3_header  : '*****' space_atoms eol ;
h4_header  : DASH DASH DASH space_atoms eol ;
eol        : NL | EOF ;

//// lexer rules
NL           : '\r'? '\n' ;
LOWER_O      : 'o' ;
LOWER_X      : 'x' ;
ID           : ALPHA (ALPHANUM|UNDERSCORE)* ;
DATE         : '2' NUM NUM NUM DASH FIRST_M_NUM NUM DASH FIRST_D_NUM NUM ;
TIME         : ('0' | '1' | '2') NUM ('0' | '1' | '2' | '3' | '4' | '5') NUM ;
ZID      : NUM NUM FIRST_M_NUM NUM FIRST_D_NUM NUM HASH ZID_CHAR ZID_CHAR ZID_CHAR? ;
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
// ZID_CHAR: Any digit OR any letter NOT in ('I', 'O', 'j', 'l')
fragment ZID_CHAR : NUM | 'A'..'H' | 'J'..'N' | 'P'..'Z' | 'a'..'i' | 'k' | 'm'..'z' ;
fragment NUM          : '0'..'9' ;
fragment FIRST_D_NUM : '0' | '1' | '2' | '3' ;
fragment FIRST_M_NUM : '0' | '1' ;
fragment ALPHA        : UPPER_LETTER | LOWER_LETTER ;
fragment ALPHANUM     : ALPHA | NUM ;
