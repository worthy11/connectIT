grammar ConnectIT;

program:
	NEWLINE* (statement ( NEWLINE+ statement)*)* NEWLINE* EOF;

statement: ('?')? (
		declarationList
		| assignment
		| expression
		| extension
		| showStmt
		| bendStmt
		| outStmt
		| whileStmt
		| forStmt
		| ifStmt
		| funcDec
		| funcCall
		| returnStmt
	);

declarationList: dataType declaration (',' declaration)*;
declaration: ID | assignment;
assignment: expression '=' expression;
extension: expression extensionOperator expression;
extensionOperator:
	'+='
	| '-='
	| '*='
	| '/='
	| '<+->'
	| '<+-'
	| '<<+-'
	| '<+-(' expression ')-'
	| '<<+-(' expression ')-';

expression: logicExpr (arrowOperator logicExpr)*? 'CLOSED'?;
logicExpr: andExpr (OR andExpr)*;
andExpr: compExpr (AND compExpr)*;
compExpr: numExpr (COMPARATOR numExpr)?;
numExpr: mulExpr ((PLUS | MINUS) mulExpr)*;
mulExpr: signExpr ((MUL | DIV) signExpr)*;
signExpr: (PLUS | MINUS)* negExpr;
negExpr: (NOT)* baseExpr;
baseExpr:
	('^')* ID
	| unitExpr
	| NUMBER
	| BOOLEAN
	| '(' expression ')'
	| '[' expression ']';
unitExpr: COLOR (PATTERN)?; 

WS: [ \t]+ -> skip;
NEWLINE: '\r'? '\n';

bendStmt:
	'BEND' ID ('IN' | 'OUT') 'BY' numExpr (
		'AT' numExpr 'TO' numExpr
	);
showStmt: 'SHOW' expression;
outStmt: 'OUTPUT' expression;

stmtBlock: '[' NEWLINE* (statement NEWLINE+)* NEWLINE* ']';
ifStmt:
	'IF' logicExpr NEWLINE* stmtBlock (
		NEWLINE* 'ELSE IF' logicExpr NEWLINE* stmtBlock
	)* (NEWLINE* 'ELSE' NEWLINE* stmtBlock)?;

whileStmt: 'REPEAT WHILE' logicExpr NEWLINE* stmtBlock;
forStmt: 'REPEAT' numExpr 'TIMES' NEWLINE* stmtBlock;

funcDec:
	'METHOD' ID '(' paramList? ')' 'RETURNS' dataType stmtBlock;
paramList: dataType ID (',' dataType ID)*;
funcCall: 'PERFORM' ID '(' argList ')';
argList: expression (',' expression)*;
returnStmt: 'RETURN' (ID | expression);

dataType:
	'UNIT'
	| 'LAYER'
	| 'SHAPE'
	| 'MODEL'
	| 'NUMBER'
	| 'BOOLEAN';

arrowOperator:
	'<->'
	| '<-'
	| '<<-'
	| '<-(' expression ')-'
	| '<<-(' expression ')-';

PLUS: '+';
MINUS: '-';
NOT: 'NOT';
OR: 'OR';
AND: 'AND';
MUL: '*';
DIV: '/';
COMPARATOR: '<' | '<=' | '>' | '>=' | '==' | '!=';

COLOR:
	'*' (
		'red'
		| 'blue'
		| 'green'
		| 'white'
		| 'black'
		| 'yellow'
		| 'lilac'
	) '*';
PATTERN: '*' ('striped' | 'dotted' | 'gradient') '*';
BOOLEAN: 'TRUE' | 'FALSE';
NUMBER: [0-9]+;

ID: [a-zA-Z_][a-zA-Z0-9_]*;