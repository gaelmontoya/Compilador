grammar grammar;

program: (statement NEWLINE)*EOF;

statement : assing | print | if_statement | for_statement;

/* Definicion de la asigancion*/
assing: ID '=' expr;

/* Definicion de print*/
print: 'print' '('expr')';

/*Definicion del if*/
if_statement: 'if' '('expr')' block;

/*Definicion de for*/
for_statement: 'for' '('assing';'expr';'assing';'')'block;

/*Definicion de block*/
block: '{'(statement NEWLINE)*'}';

/*Definicion de epresion*/
expr: expr op =('*'|'/')expr
    | expr op =('-'|'+')expr
    | expr op =('>'|'<'|'>='|'<=')expr
    | expr op =('=='|'!=')expr
    | ID 
    | '('expr')'
    ;

/*Definicion de elementos finales*/

ID: [a-zA-Z][a-zA-Z_0-9]*;
NEWLINE: [\n\r];
WS: [\t]->skip;
SEMI:';';
