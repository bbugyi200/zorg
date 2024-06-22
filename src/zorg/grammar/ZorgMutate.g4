grammar ZorgMutate;

import CommonLexerRules;

//// parser rules
prog : mut_tag ;

mut_tag : DASH? (area | context | person | project) ;
area    : HASH id ;
context : AT_SIGN id ;
person  : PERCENT id ;
project : PLUS id ;

id   : ID | NUM_ID | PRIORITY | DATE | TIME | ZID | LOWER_O | LOWER_X ;
