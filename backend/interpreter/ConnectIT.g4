grammar ConnectIT;

program:
	NEWLINE* (statement ( NEWLINE+ statement)*)* NEWLINE* EOF;

statement: ('?')? (
		declarationList
		| assignment
		| expression
		| extension
		| showStatement
		| bendStatement
		| outStatement
		| whileStmt
		| forStmt
		| ifStmt
		| functionDeclaration
		| returnExpr
	);

declarationList: dataType declaration (',' declaration)*;
declaration: ID | assignment;
assignment: ID '=' expression;
extension: ID extensionOperator expression;
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
	ID
	| unitExpr
	| NUMBER
	| BOOLEAN
	| '(' expression ')'
	| '[' expression ']';
unitExpr: COLOR (PATTERN)?;

WS: [ \t]+ -> skip;
NEWLINE: '\r'? '\n';

bendStatement:
	'BEND' ID ('IN' | 'OUT') 'BY' numExpr (
		'AT' numExpr 'TO' numExpr
	);
showStatement: 'SHOW' expression;
outStatement: 'OUTPUT' expression;

// TODO: WHILE / FOR, FUNCTION
ifStmt:
	'IF' logicExpr NEWLINE? '[' NEWLINE* statementBlock NEWLINE* ']' (
		NEWLINE* 'ELSE IF' logicExpr NEWLINE* '[' NEWLINE* statementBlock NEWLINE* ']'
	)* (
		NEWLINE* 'ELSE' NEWLINE* '[' NEWLINE* statementBlock NEWLINE* ']'
	)?;

whileStmt:
	'REPEAT WHILE' logicExpr NEWLINE? '[' statementBlock NEWLINE? ']';

statementBlock: (NEWLINE | statement NEWLINE)*;

forStmt: 'REPEAT' NUMBER 'TIMES' NEWLINE? statementBlock;

functionDeclaration:
	'METHOD' ID '(' (dataType ID ( ',' dataType ID)*)? ')' 'RETURNS' dataType '[' statementBlock
		returnExpr NEWLINE? ']';
returnExpr: 'RETURN' (ID | expression);

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