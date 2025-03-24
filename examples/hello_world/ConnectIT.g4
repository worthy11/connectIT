grammar ConnectIT;

program     : NEWLINE* (statement (NEWLINE+ statement)*)* NEWLINE* EOF ;
statement   : declaration 
            | assignment 
            | shapeDef 
            | modelDef 
            | showStatement
            ;

declaration : 'UNIT' ID ( '=' unitExpr )?           # unitDeclaration
            | 'LAYER' ID '=' layerExpr              # layerDeclaration
            | 'SHAPE' ID                            # shapeDeclaration
            | 'MODEL' ID                            # modelDeclaration
            ;

assignment  : ID '=' expression ;

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

shapeDef    : layerChain '-->' ID ;
layerChain  : layerExpr ('<-' layerChain)? ;

modelDef    : shapeChain '-->' ID ;
shapeChain  : ID ('<-' shapeChain)? ; // Only SHAPE IDs allowed

showStatement : 'SHOW' ID ; 

ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER      : [0-9]+('.'[0-9]+)? ;

COLOR       : '*' ('red' | 'blue' | 'green' | 'white' | 'black') '*';
PATTERN     : '*' ('striped' | 'dotted' | 'gradient') '*';

WS          : [ \t]+ -> skip ;
NEWLINE     : '\r'? '\n' ;