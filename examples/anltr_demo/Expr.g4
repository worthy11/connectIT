grammar Expr;

expr   : expr ('+'|'-') term   # AddSub
       | term                  # SingleTerm
       ;

term   : term ('*'|'/') factor  # MulDiv
       | factor                 # SingleFactor
       ;

factor : NUMBER                 # Number
       | '(' expr ')'           # Parens
       ;

NUMBER : [0-9]+ ;
WS     : [ \t\r\n]+ -> skip ;
