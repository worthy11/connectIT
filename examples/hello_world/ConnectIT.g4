grammar ConnectIT;

program     : NEWLINE* (statement (NEWLINE+ statement)*)* NEWLINE* EOF ;
statement   : declaration 
            | assignment 
            | shapeDef 
            | modelDef 
            | showStatement
            | returnExpr
            ;

declaration : 'UNIT' ID ( '=' unitExpr )?           # unitDeclaration
            | 'LAYER' ID ( '=' layerExpr )?         # layerDeclaration
            | 'SHAPE' ID                            # shapeDeclaration
            | 'MODEL' ID                            # modelDeclaration
            ;

assignment  : ID '=' expression
            | layerChain '-->' ID
            | shapeChain '-->' ID
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

shapeDef    : layerChain '-->' ( SHAPE )? ID ;
layerChain  : ( layerExpr | ID ) ('<-' layerChain)?
            | ( layerExpr | ID ) ('<<-' layerChain)?
            | ( layerExpr | ID ) ('<' NUMBER '-' layerChain)?
            | ID '<-' (layerChain)?
            ; 

modelDef    : shapeChain '-->' ID ;
shapeChain  : ID ('<-' shapeChain)? ; // Only SHAPE IDs allowed

showStatement : 'SHOW' ID ; 

whileStmt -> 'REPEAT WHILE' condition NEWLINE? '[' statementBlock NEWLINE? ']'  
condition -> expr  
statementBlock -> statement (NEWLINE statement)*

forStmt -> 'REPEAT' NUMBER 'TIMES' NEWLINE? statementBlock

functionDeclaration -> 'METHOD' ID '(' ( 'NUMBER'
                                        | 'COLOR'
                                        | 'PATTERN'
                                        | 'UNIT'
                                        | 'LAYER'
                                        | 'SHAPE'
                                        | 'MODEL'
                                        )*
                        ')' RETURNS ( 'NUMBER'
                                    | 'COLOR'
                                    | 'PATTERN'
                                    | 'UNIT'
                                    | 'LAYER'
                                    | 'SHAPE'
                                    | 'MODEL'
                                    | 'NOTHING'
                                    ) 
                        '[' statementBlock returnExpr NEWLINE? ']';
returnExpr -> 'RETURN' (ID | expr);

ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER      : [0-9]+('.'[0-9]+)? ;

COLOR       : '*' ('red' | 'blue' | 'green' | 'white' | 'black') '*';
PATTERN     : '*' ('striped' | 'dotted' | 'gradient') '*';

WS          : [ \t]+ -> skip ;
NEWLINE     : '\r'? '\n' ;