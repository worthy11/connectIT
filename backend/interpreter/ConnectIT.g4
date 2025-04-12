grammar ConnectIT;

program:
	NEWLINE* (statement ( NEWLINE+ statement)*)* NEWLINE* EOF;

statement:
	declaration
	| assignment
	| showStatement
	| whileStmt
	| forStmt
	| ifStmt
	| functionDeclaration
	| returnExpr;

declaration:
	'UNIT' unitDeclarationList		# newUnit
	| 'LAYER' layerDeclarationList	# newLayer
	| 'SHAPE' shapeDeclarationList	# newShape
	| 'MODEL' modelDeclarationList	# newModel;

// DECLARATION TYPES
unitDeclarationList: unitDeclaration (',' unitDeclaration)*;
unitDeclaration: ID ( '=' unitExpr)?;
unitExpr: (PATTERN)? COLOR | (COLOR)? PATTERN;

layerDeclarationList: layerDeclaration ( ',' layerDeclaration)*;
layerDeclaration: ID ( '=' layerExpr)? ( 'CLOSED')?;
layerExpr: ID '*' NUMBER | layerExpr '+' layerExpr |;

shapeDeclarationList:
	shapeDeclaration (',' shapeDeclarationList)*;
shapeDeclaration: ID ('=' ID | shapeExpr);
shapeExpr: (layerExpr | ID) ('<-' shapeExpr)?
	| ( layerExpr | ID) ( '<<-' shapeExpr)?
	| ( layerExpr | ID) ( '<-' NUMBER '-' shapeExpr)?
	| ( layerExpr | ID) ( '<<-' NUMBER '-' shapeExpr)?;

modelDeclarationList:
	modelDeclaration (',' modelDeclarationList)*;
modelDeclaration: ID ('=' ID | modelExpr);
modelExpr: (shapeExpr | ID) ('<-' shapeExpr)?
	| ( layerExpr | ID) ( '<<-' shapeExpr)?
	| ( layerExpr | ID) ( '<-' NUMBER '-' shapeExpr)?
	| ( layerExpr | ID) ( '<<-' NUMBER '-' shapeExpr)?;

// ASSIGNMENTS
assignment: ID ('=' | '-->') expression;
expression: unitExpr | layerExpr | shapeExpr | modelExpr;

showStatement: 'SHOW' ID;

ifStmt:
	'IF' condition NEWLINE? '[' statementBlock NEWLINE? ']' (
		NEWLINE? 'ELSE IF' condition NEWLINE? '[' statementBlock NEWLINE? ']'
	)* (NEWLINE? 'ELSE' NEWLINE? '[' statementBlock NEWLINE? ']')?;

whileStmt:
	'REPEAT WHILE' condition NEWLINE? '[' statementBlock NEWLINE? ']';

condition:
	expression ('<' | '<=' | '>' | '>=' | '==' | '!=') expression;

statementBlock: statement (NEWLINE statement)*;

forStmt: 'REPEAT' NUMBER 'TIMES' NEWLINE? statementBlock;

functionDeclaration:
	'METHOD' ID '(' (type ID ( ',' type ID)*)? ')' 'RETURNS' type '[' statementBlock returnExpr
		NEWLINE? ']';
returnExpr: 'RETURN' (ID | expression);

type: 'UNIT' | 'LAYER' | 'SHAPE' | 'MODEL' | 'NUMBER';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: ('-')? [0-9]+ ('.' [0-9]+)?;

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

WS: [ \t]+ -> skip;
NEWLINE: '\r'? '\n';