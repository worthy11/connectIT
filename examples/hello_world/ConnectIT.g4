grammar ConnectIT;

// Program structure
program     : statement+ EOF ;
statement   : declaration NEWLINE
            | assignment NEWLINE
            | shapeDef NEWLINE
            | modelDef NEWLINE
            | instruction NEWLINE
            ;

// Variable declarations
declaration : 'UNIT' ID ( '=' unitExpr )?           # UnitDeclaration
            | 'LAYER' ID '=' layerExpr              # LayerDeclaration
            | 'SHAPE' ID                            # ShapeDeclaration
            | 'MODEL' ID                            # ModelDeclaration
            ;

// Assignments (Only for UNITs and LAYERs)
assignment  : ID '=' expression ;

// Expressions
expression  : unitExpr
            | layerExpr
            | ID
            ;

// UNIT expressions (Colors or Patterns)
unitExpr    : COLOR
            | PATTERN
            | // Empty for uninitialized units
            ;

// LAYER expressions (Unit Multiplication and Addition)
layerExpr   : unitExpr '*' NUMBER
            | layerExpr '+' layerExpr
            ;

// Shape assignments using layer chains
shapeDef    : layerChain '-->' ID ;
layerChain  : layerExpr ('<-' layerChain)? ;

// Model assignments using shape chains
modelDef    : shapeChain '-->' ID ;
shapeChain  : ID ('<-' shapeChain)? ; // Only SHAPE IDs allowed

// Other keyword instructions
instruction : keyword ID ; 
keyword     : 'SHOW' ;

// Tokens
ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER      : [0-9]+('.'[0-9]+)? ;

// Colors and Patterns
COLOR       : 'red' | 'blue' | 'green' | 'white' | 'black' ;
PATTERN     : 'striped' | 'dotted' | 'gradient' ;

// Whitespace and Newline
WS          : [ \t]+ -> skip ;
NEWLINE     : '\r'? '\n' ;
