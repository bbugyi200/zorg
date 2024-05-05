grammar ZorgQuery;

import CommonLexerRules;

//// parser rules
prog : query NL? ;

// query
query : where_query | select_query ;
where_query : (select SPACE)? where (SPACE order_by)? (SPACE group_by)? ;
select_query : select ;

// S W O G
select : 'S' SPACE select_body ;
where : 'W' SPACE where_body ;
order_by : 'O' SPACE order_by_body ;
group_by : 'G' SPACE group_by_body ;

// SELECT
select_body : file | note | AT_SIGN | HASH | PLUS | PERCENT ;
note : 'note' ;

// WHERE
where_body : or_filter ;
or_filter : and_filter (SPACE 'or' SPACE and_filter)* ;
and_filter : where_atom (SPACE where_atom)* ;
where_atom : note_type | priority_range | tag | subfilter;
note_type : note_type_char+ ;
note_type_char : DASH | LOWER_O | LOWER_X | TILDE | LANGLE | RANGLE ;
priority_range : '[' HASH ID ']' ;
tag : not_op? (area | context | person | project) ;
not_op : '!' ;
area : HASH ID ;
context : AT_SIGN ID ;
person : PERCENT ID ;
project : PLUS ID ;
subfilter : '(' or_filter ')' ;

// GROUP BY
group_by_body : group_by_atom (SPACE group_by_atom)? (SPACE group_by_atom)? (SPACE group_by_atom)? ;
group_by_atom : file | type | AT_SIGN | HASH | PERCENT | PLUS ;

// ORDER BY
order_by_body : order_by_atom (SPACE order_by_atom)* ;
order_by_atom : date | priority | type ;
date : 'date' ;
priority : 'priority' ;

// shared subrules
file : 'file' ;
type : 'type' ;
