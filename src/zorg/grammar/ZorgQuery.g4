grammar ZorgQuery;

import CommonLexerRules;

//// parser rules
prog : query NL? ;

// query
query        : where_query | select_query ;
where_query  : (select SPACE)? where (SPACE order_by)? (SPACE group_by)? ;
select_query : select ;

// S W O G
select   : 'S' SPACE select_body ;
where    : 'W' SPACE where_body ;
order_by : 'O' SPACE order_by_body ;
group_by : 'G' SPACE group_by_body ;

// --- SELECT
select_body : file | note | AT_SIGN | HASH | PLUS | PERCENT ;
note        : 'note' ;

// --- WHERE
where_body     : or_filter ;
or_filter      : and_filter (SPACE '|' SPACE and_filter)* ;
and_filter     : where_atom (SPACE where_atom)* ;
where_atom     : note_type | priority_range | tag | subfilter | create_range | modify_range | prop_filter | desc_filter | file_filter | link_filter ;
note_type      : note_type_char+ ;
note_type_char : DASH | LOWER_O | LOWER_X | TILDE | LANGLE | RANGLE ;
priority_range : PRIORITY (DASH ('1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'))? ;
tag            : not_op? (area | context | person | project) ;
not_op         : '!' ;
area           : HASH id ;
context        : AT_SIGN id ;
person         : PERCENT id ;
project        : PLUS id ;
subfilter      : '(' or_filter ')' ;
create_range   : CREATE_RANGE_HEAD DATE_RANGE_TAIL? ;
modify_range   : MODIFY_RANGE_HEAD DATE_RANGE_TAIL? ;
prop_filter    : not_op? id COLON prop_op? (id | ('0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9')+ | STAR) ;
prop_op        : '<' | '<=' | '>=' | '>' ;
desc_filter    : not_op? 'c'? (s_desc_filter | d_desc_filter) ;
s_desc_filter  : SQUOTE any_non_squote* id any_non_squote* (SPACE any_non_squote* id any_non_squote*)* SQUOTE ;
d_desc_filter  : DQUOTE any_non_dquote* id any_non_dquote* (SPACE any_non_dquote* id any_non_dquote*)* DQUOTE ;
file_filter    : not_op? 'f=' (id FSLASH)* (STAR UNDERSCORE?)? id STAR? ;
link_filter    : not_op? '[[' (id FSLASH)* id ']]' ;

zid  : ZID  ;
id   : ID | NUM_ID | DATE_RANGE_TAIL | PRIORITY | date | time | zid | LOWER_O | LOWER_X ;
date : DATE ;
time : TIME ;

// symbols
any_non_squote : DQUOTE | desc_symbol ;
any_non_dquote : SQUOTE | desc_symbol ;
desc_symbol    : HAT | DOLLAR | non_tag_symbol | tag_symbol | id_symbol ;
non_tag_symbol : LANGLE | RANGLE | STAR | TILDE | SYMBOL | LPAREN | RPAREN | UNDERSCORE ;
id_symbol      : DASH | DOT | FSLASH | COLON ;
tag_symbol     : HASH | AT_SIGN | PERCENT | PLUS ;

// --- GROUP BY
group_by_body : group_by_atom (SPACE group_by_atom)? (SPACE group_by_atom)? (SPACE group_by_atom)? ;
group_by_atom : file | type | priority | 'none' | AT_SIGN | HASH | PERCENT | PLUS ;

// --- ORDER BY
order_by_body :  order_by_atom (SPACE order_by_atom)* ;
order_by_atom :  create | modify | priority | type ;
create        :  'create' ;
modify        :  'modify' ;
priority      :  'priority' ;

// shared subrules
file : 'file' ;
type : 'type' ;

//// lexer rules
CREATE_RANGE_HEAD : HAT ZDATE ;
MODIFY_RANGE_HEAD : DOLLAR ZDATE ;
DATE_RANGE_TAIL   : COLON ZDATE ;
ZDATE             : SHORT_DATE | RELATIVE_DATE ;
RELATIVE_DATE     : DASH? NUM+ ('d' | 'm' | 'y') ;
