grammar ZorgQuery;

//// parser rules
prog : query NL ;

query : where_query | select_query ;
where_query : (select SPACE)? where (SPACE order_by)? (SPACE group_by)? ;
select_query : select ;

select : 'S' SPACE select_body ;
where : 'W' SPACE where_body ;
order_by : 'O' ;
group_by : 'G' ;

select_body : 'file' | 'note' | '@' | '#' | '+' | '%' ;
where_body : 'o' ;

//// lexer rules
NL : '\r'? '\n' ;
SPACE : ' ' ;

//// fragments
