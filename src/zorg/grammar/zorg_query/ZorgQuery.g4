grammar ZorgQuery;

//// parser rules
prog : query NL? ;

query : where_query | select_query ;
where_query : (select SPACE)? where (SPACE order_by)? (SPACE group_by)? ;
select_query : select ;

select : 'S' SPACE select_body ;
where : 'W' SPACE where_body ;
order_by : 'O' ;
group_by : 'G' ;

select_body : 'file' | 'note' | AT_SIGN | HASH | PLUS | PERCENT ;

where_body : note_status ;
note_status : note_status_char+ ;
note_status_char : DASH | LOWER_O | LOWER_X | TILDE | LANGLE | RANGLE ;

//// lexer rules
NL : '\r'? '\n' ;
SPACE : ' ' ;
PLUS : '+' ;
AT_SIGN : '@' ;
PERCENT : '%' ;
HASH : '#' ;
DASH : '-' ;
LOWER_O : 'o' ;
LOWER_X : 'x' ;
LANGLE : '<' ;
RANGLE : '>' ;
TILDE : '~' ;

//// fragments
