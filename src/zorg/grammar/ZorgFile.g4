grammar ZorgFile;

import CommonLexerRules;

//// parser rules
prog : head body? EOF ;

// header and body
head    : comment+ ;
comment : HASH space_atoms? NL ;
body    : NL+ block* h2_section* h1_section* ;

// blocks
block    : item+ NL* ;
item     : todo | note | comment ;

// notes
note      : DASH base_note ;
base_note : note_body NL ;
note_body : space_atoms (NL SPACE+ space_atoms)* ;

// todos
todo        : base_todo ;
base_todo   : todo_prefix (SPACE priority)? note_body NL ;
todo_prefix : (LOWER_O | x_or_tilde | LANGLE | RANGLE) ;
x_or_tilde  : (LOWER_X | TILDE) (COLON time)? ;
priority    : PRIORITY ;

// atoms
space_atoms : space_atom+ ;
space_atom  : SPACE (non_tag_sym | DASH | PLUS SPACE | DQUOTE | SQUOTE)* (quoted | atom)? (any_sym (any_sym | id)*)? square_atom? ;
atom        : tag_symbol
            | tag
            | link
            | property
            | id_group
            | global_link
            | local_link
            | zid_link
            | embedded_link
            | ref_link
            | square_atom
            | priority ;

// Zorg YYMMDD#XX IDs
zid : ZID  ;

// property
property    : simple_prop | inline_prop ;
simple_prop : id COLON COLON id_group ;
inline_prop : '[' id COLON COLON SPACE? id_group (SPACE id_group)* ']';
id_group    : id (any_sym+ id)* ;
id          : ID | NUM_ID | PRIORITY | date | time | zid | LOWER_O | LOWER_X ;
date        : DATE ;
time        : TIME ;

// symbols
any_sym     : SQUOTE | DQUOTE | HAT | DOLLAR | non_tag_sym | tag_symbol | id_symbol ;
non_tag_sym : LANGLE | RANGLE | STAR | TILDE | SYMBOL | LPAREN | RPAREN | UNDERSCORE ;
id_symbol   : HASH | DASH | DOT | FSLASH | COLON ;
tag_symbol  : HASH | AT_SIGN | PERCENT | PLUS ;

// tag
tag     : area | context | person | project ;
area    : HASH id ;
context : AT_SIGN id ;
person  : PERCENT id ;
project : PLUS id ;

// quotes and links
quoted        : (SQUOTE quoted_atom+ SQUOTE | DQUOTE quoted_atom+ DQUOTE) ;
quoted_atom   : '[' | ']' | '[[' | ']]' | atom | priority ;
link          : '[[' id_group ']]' ;
global_link   : '[#' ID ']' ;
local_link    : '[^' ID ']' ;
zid_link      : '[' zid ']' ;
square_atom   : '[' (id_group | SPACE) (SPACE id_group)* ']' ;
embedded_link : '((' id_group '))' ;
ref_link      : '[@' ID ']' ;

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
