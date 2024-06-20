grammar ZorgFile;

import CommonLexerRules;

//// parser rules
prog : head body? EOF ;

// header and body
head    : comment+ ;
comment : HASH space_atoms? NL ;
body    : NL+ block* h2_section* h1_section* ;

// blocks
block       : item+ NL* ;
item        : todo | note | footnote | comment ;
footnote    : ref COLON space_atoms NL ;

// notes
note         : DASH base_note subnote* ;
base_note    : note_body NL ;
note_body    : space_atoms (NL SPACE+ space_atoms)* ;
subnote      : TWO_SPACE_DASH base_note subsubnote*;
subsubnote   : FOUR_SPACE_DASH base_note ;

// todos
todo        : base_todo subnote* ;
base_todo   : todo_prefix (SPACE priority)? note_body NL ;
todo_prefix : (LOWER_O | x_or_tilde | LANGLE | RANGLE) ;
x_or_tilde  : (LOWER_X | TILDE) (COLON time)? ;
priority    : PRIORITY ;

// atoms
space_atoms : space_atom+ ;
space_atom  : SPACE (SQUOTE non_tag_symbol)? (non_tag_symbol | DQUOTE)* (atom | quoted)? (any_symbol (any_symbol | id)*)? ref? ;
atom        : tag_symbol | tag | link | property | id_group | global_link | local_link | zid_link | embedded_link | ref | priority ;

// Zorg YYMMDD#XX IDs
zid : ZID  ;

// property
property    : simple_prop | inline_prop ;
simple_prop : id COLON COLON id_group ;
inline_prop : '[' id COLON COLON SPACE? id_group (SPACE id_group)* ']';
id_group    : id (any_symbol+ id)* ;
id          : ID | NUM_ID | PRIORITY | date | time | zid | LOWER_O | LOWER_X ;
date        : DATE ;
time        : TIME ;

// symbols
any_symbol     : SQUOTE | DQUOTE | HAT | DOLLAR | non_tag_symbol | tag_symbol | id_symbol ;
non_tag_symbol : LANGLE | RANGLE | STAR | TILDE | SYMBOL | LPAREN | RPAREN | UNDERSCORE ;
id_symbol      : HASH | DASH | DOT | FSLASH | COLON ;
tag_symbol     : HASH | AT_SIGN | PERCENT | PLUS ;

// tag
tag     : area | context | person | project ;
area    : HASH id ;
context : AT_SIGN id ;
person  : PERCENT id ;
project : PLUS id ;

// quotes and links
quoted        : (SQUOTE (atom | priority | '[[' | ']]')+ SQUOTE | DQUOTE atom+ DQUOTE) ;
link          : '[[' id_group ']]' ;
global_link   : '[#' ID ']' ;
local_link    : '[' ID ']' ;
zid_link      : '[' zid ']' ;
embedded_link : '[(' id_group ')]' ;
ref           : '[' id_group (SPACE id_group)* ']' | '[' SPACE ']';

// sections
h1_section : h1_header NL* block* (NL? h2_section)* ;
h2_section : h2_header NL* block* (NL? h3_section)* ;
h3_section : h3_header NL* block* (NL? h4_section)* ;
h4_section : h4_header NL* block* ;
h1_header  : H1_HEADER space_atoms eol ;
h2_header  : H2_HEADER space_atoms eol ;
h3_header  : H3_HEADER space_atoms eol ;
h4_header  : H4_HEADER space_atoms eol ;
eol        : NL | EOF ;
