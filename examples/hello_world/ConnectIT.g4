grammar ConnectIT;

program     : NEWLINE* ( statement ( NEWLINE+ statement )* )* NEWLINE* EOF ;

statement   : declaration 
            | assignment 
            | shapeDef 
            | modelDef 
            | showStatement
            | whileStmt
            | forStmt
            | ifStmt
            | functionDeclaration
            | returnExpr
            ;

declaration : 'UNIT' unitAssigmentList        # unitDeclaration
            | 'LAYER' layerAssigmentList      # layerDeclaration
            | 'SHAPE' idList                  # shapeDeclaration
            | 'MODEL' idList                  # modelDeclaration
            ;

unitAssigmentList   : unitAssignment (',' unitAssignment)* ;

unitAssignment  : ID ( '=' unitExpr )? ;

layerAssigmentList  : layerAssignment ( ',' layerAssignment )* ;

layerAssignment : ID ( '=' layerExpr )? ;

idList  : ID ( ',' ID )* ;

assignment  : ID '=' expression         # standardAssignment
            | layerChain '-->' ID       # shapeAssignment
            | shapeChain '-->' ID       # modelAssignment
            ;

expression  : unitExpr
            | layerExpr
            | ID
            ;

unitExpr    : COLOR
            | PATTERN
            | // Empty for uninitialized units
            ;

layerExpr   : ID '*' NUMBER
            | layerExpr '+' layerExpr
            |
            ;

shapeDef    : layerChain '-->' 'SHAPE' ID ;

layerChain  : ( layerExpr | ID ) ( '<-' layerChain )?
            | ( layerExpr | ID ) ( '<<-' layerChain )?
            | ( layerExpr | ID ) ( '<-' NUMBER '-' layerChain )?
            | ( layerExpr | ID ) ( '<<-' NUMBER '-' layerChain )?
            ; 

modelDef    : shapeChain '-->' 'MODEL' ID ;

shapeChain  : ID ('<-' shapeChain)? ; // Only SHAPE IDs allowed

showStatement   : 'SHOW' ID ; 

ifStmt  : 'IF' condition NEWLINE? '[' statementBlock NEWLINE? ']'
        ( NEWLINE? 'ELSE IF' condition NEWLINE? '[' statementBlock NEWLINE? ']' )*
        ( NEWLINE? 'ELSE' NEWLINE? '[' statementBlock NEWLINE? ']' )? ;

whileStmt   : 'REPEAT WHILE' condition NEWLINE? '[' statementBlock NEWLINE? ']' ;

// To trzeba zdecydowanie zmienić jakoś, dałem tak na odpierdol póki co xd
condition   : expression ( '<' | '<=' | '>' | '>=' | '==' | '!=' ) expression ; 

statementBlock  : statement (NEWLINE statement)* ;

forStmt : 'REPEAT' NUMBER 'TIMES' NEWLINE? statementBlock ;

functionDeclaration : 'METHOD' ID '('( type ID ( ',' type ID )* )?')' 'RETURNS' type '[' statementBlock returnExpr NEWLINE? ']' ;

returnExpr  : 'RETURN' (ID | expression);

type    : 'UNIT'
        | 'LAYER'
        | 'SHAPE'
        | 'MODEL'
        | 'NUMBER'
        ;

ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER      : [0-9]+('.'[0-9]+)? ;

COLOR       : '*' ( 'red' | 'blue' | 'green' | 'white' | 'black' ) '*';
PATTERN     : '*' ( 'striped' | 'dotted' | 'gradient' ) '*';

WS          : [ \t]+ -> skip ;
NEWLINE     : '\r'? '\n' ;