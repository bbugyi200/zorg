grammar ZorgMutate;

import CommonLexerRules;

//// parser rules
prog : mut_cmd (SPACE mut_cmd)* NL? ;

// mutate command
mut_cmd : mut_note_type | mut_tag | mut_prop | mut_link ;

// mutate note type
mut_note_type : DASH | TILDE | LOWER_X | OPEN_TODO_MUT ;

// mutate tags
mut_tag : DASH? tag ;
tag : area | context | person | project ;
area    : HASH id ;
context : AT_SIGN id ;
person  : PERCENT id ;
project : PLUS id ;

// mutate properties
mut_prop : key COLON value
         | DASH key
         ;
key : id ;
value : id ;

// mutate links
mut_link : DASH? '[[' id ']]' ;

id : ID | NUM_ID | PRIORITY | DATE | TIME | ZID | LOWER_O | LOWER_X ;

//// lexer rules
S_EQUAL : 's=' ;
OPEN_TODO_MUT : DIGIT? OPEN_TODO_CHAR ;
OPEN_TODO_CHAR : ('o' | '<' | '>') ;
DIGIT : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
