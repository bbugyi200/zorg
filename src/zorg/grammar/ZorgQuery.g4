grammar ZorgQuery;

import CommonLexerRules;

//// parser rules
prog : query NL? ;

// query
query           : where_query | select_query ;
where_query     : (select SPACE)? where order_and_group ;
order_and_group : (SPACE order_by)? (SPACE group_by)?
                | (SPACE group_by)? (SPACE order_by)?
                ;
select_query    : select order_and_group ;

// S W O G
select   : 'S' SPACE select_body ;
where    : 'W' SPACE where_body ;
order_by : 'O' SPACE order_by_body ;
group_by : 'G' SPACE group_by_body ;

// --- SELECT
select_body  : select_field
             | select_agg
             ;
select_field : file | note | prop | prop_values | links | AT_SIGN | HASH | PLUS | PERCENT ;
select_agg   : func_name '(' select_field ')' ;
prop         : 'prop' ;
prop_values  : prop COLON id ;
links        : 'links' ;
note         : 'note' ;

// functions
func_name : 'count' ;

// --- WHERE
where_body     : or_filter ;
or_filter      : and_filter (SPACE '|' SPACE and_filter)* ;
and_filter     : where_atom (SPACE where_atom)* ;
where_atom     : note_type
               | priority_range
               | tag
               | subfilter
               | create_range
               | modify_range
               | prop_filter
               | desc_filter
               | file_filter
               | link_filter
               ;
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
prop_filter    : not_op? id COLON prop_op? (id | STAR) ;
prop_op        : '<' | '<=' | '>=' | '>' ;
desc_filter    : not_op? 'c'? (s_desc_filter | d_desc_filter) ;
s_desc_filter  : SQUOTE any_non_squote (SPACE any_non_squote)* SQUOTE ;
d_desc_filter  : DQUOTE any_non_dquote (SPACE any_non_dquote)* DQUOTE ;
file_filter    : not_op? 'f=' (id FSLASH)* (STAR UNDERSCORE?)? id STAR? ;
link_filter    : not_op? '[[' (id FSLASH)* id ']]' ;

zid  : ZID  ;
id   : ID | NUM_ID | DATE_RANGE_TAIL | PRIORITY | date | time | zid | keyword | LOWER_O | LOWER_X ;
date : DATE ;
time : TIME ;

// symbols
any_non_squote     : (any_non_squote_sym | id)+ ;
any_non_dquote     : (any_non_dquote_sym | id)+ ;
any_non_squote_sym : DQUOTE | desc_symbol ;
any_non_dquote_sym : SQUOTE | desc_symbol ;
desc_symbol        : HAT | DOLLAR | non_tag_symbol | tag_symbol | id_symbol ;
non_tag_symbol     : LANGLE | RANGLE | STAR | TILDE | SYMBOL | LPAREN | RPAREN | UNDERSCORE ;
id_symbol          : DASH | DOT | FSLASH | COLON ;
tag_symbol         : HASH | AT_SIGN | PERCENT | PLUS ;

// --- GROUP BY
group_by_body : group_by_atom (SPACE group_by_atom)? (SPACE group_by_atom)? (SPACE group_by_atom)? ;
group_by_atom : file | section | type | priority | none | AT_SIGN | HASH | PERCENT | PLUS ;

// --- ORDER BY
order_by_body : order_by_atom (SPACE order_by_atom)* ;
order_by_atom : alpha | create | modify | priority | type | none ;

// keywords
keyword  : file | none | type | priority | alpha | create | modify | section ;
file     : 'file' ;
none     : 'none' ;
type     : 'type' ;
priority : 'priority' ;
alpha    : 'alpha' ;
create   : 'create' ;
modify   : 'modify' ;
section  : 'section' ;

//// lexer rules
CREATE_RANGE_HEAD : HAT ZDATE ;
MODIFY_RANGE_HEAD : DOLLAR ZDATE ;
DATE_RANGE_TAIL   : COLON ZDATE ;
ZDATE             : SHORT_DATE | RELATIVE_DATE ;
RELATIVE_DATE     : DASH? NUM+ ('d' | 'm' | 'y') ;
