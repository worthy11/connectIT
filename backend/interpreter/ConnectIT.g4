grammar ConnectIT;

program:
	NEWLINE* (statement ( NEWLINE+ statement)*)* NEWLINE* EOF;

statement: ('?')? (
		declarationList
		| assignment
		| showStatement
		| whileStmt
		| forStmt
		| ifStmt
		| functionDeclaration
		| returnExpr
	);

declarationList: dataType declaration (',' declaration)*;
declaration: ID | assignment;
assignment: ID '=' expression;
extension: expression '-->' ID;
dataType:
	'UNIT'
	| 'LAYER'
	| 'SHAPE'
	| 'MODEL'
	| 'NUMBER'
	| 'BOOLEAN';

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
PATTERN: '*' ( 'striped' | 'dotted' | 'gradient') '*';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: '-'? [0-9]+;
BOOLEAN: 'TRUE' | 'FALSE';

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

expression: logicExpr (arrowOperator logicExpr)* 'CLOSED'?;
logicExpr: andExpr (OR andExpr)*;
andExpr: compExpr (AND compExpr)*;
compExpr: numExpr (COMPARATOR numExpr)?;
numExpr: mulExpr ((PLUS | MINUS) mulExpr)*;
mulExpr: invExpr ((MUL | DIV)? invExpr)*;
invExpr: (NOT | MINUS)? baseExpr;
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
showStatement: 'SHOW' ID;

// TODO: Update IF / ELSE, WHILE / FOR, FUNCTION
ifStmt:
	'IF' condition NEWLINE? '[' statementBlock NEWLINE? ']' (
		NEWLINE? 'ELSE IF' condition NEWLINE? '[' statementBlock NEWLINE? ']'
	)* (NEWLINE? 'ELSE' NEWLINE? '[' statementBlock NEWLINE? ']')?;

whileStmt:
	'REPEAT WHILE' condition NEWLINE? '[' statementBlock NEWLINE? ']';

condition: expression COMPARATOR expression;

statementBlock: statement (NEWLINE statement)*;

forStmt: 'REPEAT' NUMBER 'TIMES' NEWLINE? statementBlock;

functionDeclaration:
	'METHOD' ID '(' (dataType ID ( ',' dataType ID)*)? ')' 'RETURNS' dataType '[' statementBlock
		returnExpr NEWLINE? ']';
returnExpr: 'RETURN' (ID | expression);