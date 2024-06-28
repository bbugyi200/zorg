grammar ZorgMutate;

import CommonLexerRules;

//// parser rules
prog : mut_cmd (SPACE mut_cmd)* ;

// mutate command
mut_cmd : mut_tag | mut_prop ;

// mutate tags
mut_tag : DASH? (area | context | person | project) ;
area    : HASH id ;
context : AT_SIGN id ;
person  : PERCENT id ;
project : PLUS id ;

// mutate properties
mut_prop : id COLON id
         | DASH id
         ;

id : ID | NUM_ID | PRIORITY | DATE | TIME | ZID | LOWER_O | LOWER_X ;
