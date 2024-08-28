grammar ZorgFile;

import CommonLexerRules;

//// parser rules
prog : head body? EOF ;

// header and body
head    : comment+ ;
comment : HASH space_atoms? NL ;
body    : NL+ block* h2_section* h1_section* ;

// blocks
block : item+ NL* ;
item  : todo | note | comment ;

// notes
note      : DASH base_note ;
base_note : note_body NL ;
note_body : space_atoms (NL SPACE+ space_atoms)* ;

// todos
todo        : base_todo ;
base_todo   : todo_prefix (SPACE priority)? note_body NL ;
todo_prefix : LOWER_O | LOWER_X | TILDE | LANGLE | RANGLE ;
priority    : PRIORITY ;

// atoms
space_atoms : space_atom+ ;
space_atom  : SPACE atom ;
atom        : tag_sym | word_group ;
word_group  : before_word* word? after_word* ;
before_word : non_tag_sym | DASH ;
word        : quoted_word | unquoted_word ;
after_word  : any_sym (any_sym | id)* ;

// quoted and unquoted words
unquoted_word    : tag
                 | link
                 | property
                 | url
                 | id_group
                 | global_link
                 | local_link
                 | zid_link
                 | embedded_link
                 | ref_link
                 | priority
                 ;
quoted_word      : SQUOTE quoted_word_body+ SQUOTE? | DQUOTE quoted_word_body+ DQUOTE? ;
quoted_word_body : any_sym | unquoted_word | '[[' | ']]';

// Zorg YYMMDD#XX IDs
zid : ZID  ;

// property
property          : simple_prop | inline_prop ;
simple_prop       : id COLON COLON simple_prop_value ;
simple_prop_value : id | url ;
inline_prop       : '[' id COLON COLON SPACE? id_group (SPACE id_group)* ']';
id_group          : id (any_sym+ | id)* ;
id                : ID | NUM_ID | PRIORITY | date | time | zid | url | LOWER_O | LOWER_X ;
date              : DATE ;
time              : TIME ;

// symbols
any_sym     : SQUOTE | DQUOTE | HAT | DOLLAR | non_tag_sym | tag_sym | id_sym | '[' | ']' ;
non_tag_sym : SYMBOL
            | AMP
            | EQUAL
            | LANGLE
            | LPAREN
            | QMARK
            | RANGLE
            | RPAREN
            | STAR
            | TILDE
            | UNDERSCORE
            ;
id_sym      : HASH | DASH | DOT | FSLASH | COLON ;
tag_sym     : HASH | AT_SIGN | PERCENT | PLUS ;

// tag
tag     : area | context | person | project ;
area    : HASH id ;
context : AT_SIGN id ;
person  : PERCENT id ;
project : PLUS id ;

// links
link          : '[[' id_group ']]' ;
global_link   : '[#' ID ']' ;
local_link    : '[^' ID ']' ;
zid_link      : '[' zid ']' ;
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

// URL
url : ('https://' | 'http://') ID ('.' ID)* (':' NUM_ID)? ('/' ID ((AMP | COLON | DASH | EQUAL | QMARK) (ID | FSLASH))*)* ;
