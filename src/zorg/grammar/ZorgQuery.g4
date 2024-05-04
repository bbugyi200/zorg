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
order_by : 'O' ;
group_by : 'G' group_by_body ;

// SELECT
select_body : 'file' | 'note' | AT_SIGN | HASH | PLUS | PERCENT ;

// WHERE
where_body : where_atom (SPACE where_atom)* ;
where_atom : note_status | priority_range ;
note_status : note_status_char+ ;
note_status_char : DASH | LOWER_O | LOWER_X | TILDE | LANGLE | RANGLE ;
priority_range : '[' HASH ID ']' ;

// GROUP BY
group_by_body : 'file' ;
