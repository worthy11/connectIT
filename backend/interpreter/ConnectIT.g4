grammar ConnectIT;

program:
	NEWLINE* (statement ( NEWLINE+ statement)*)* NEWLINE* EOF;

statement	: declaration
			| assignment
			| showStatement
			| whileStmt
			| forStmt
			| ifStmt
			| functionDeclaration
			| returnExpr
			;

declaration	: 'UNIT' unitDeclarationList		# newUnit
			| 'LAYER' layerDeclarationList		# newLayer
			| 'SHAPE' shapeDeclarationList		# newShape
			| 'MODEL' modelDeclarationList		# newModel
    		| 'NUMBER' numberDeclarationList 	# newNumber
    		| 'BOOLEAN' booleanDeclarationList 	# newBoolean
			;

// DECLARATION TYPES
unitDeclarationList	: unitDeclaration (',' unitDeclaration)*;
unitDeclaration		: ID '=' (unitExpr | ID);
unitExpr			: COLOR (PATTERN)? | (COLOR)? PATTERN;

layerDeclarationList: layerDeclaration (',' layerDeclaration)*;
layerDeclaration	: ID '=' (layerExpr | ID) ('CLOSED')?;
layerExpr			: ID '*' (NUMBER | ID) | layerExpr '+' layerExpr;

shapeDeclarationList: shapeDeclaration (',' shapeDeclaration)*;
shapeDeclaration	: ID '<--' shapeExpr | ID ('=' ID)?;							
shapeExpr			: (layerExpr | ID) ('<-' shapeExpr)?
					| (layerExpr | ID) ('<<-' shapeExpr)?
					| (layerExpr | ID) ('<-' (NUMBER | ID) '-' shapeExpr)?
					| (layerExpr | ID) ('<<-' (NUMBER | ID) '-' shapeExpr)?;

modelDeclarationList: modelDeclaration (',' modelDeclarationList)*;
modelDeclaration	: ID '<--' modelExpr | ID ('=' ID)?;
modelExpr			: (shapeExpr | ID) ('<-' modelExpr)?
					| (shapeExpr | ID) ('<<-' modelExpr)?
					| (shapeExpr | ID) ('<-' (NUMBER | ID) '-' modelExpr)?
					| (shapeExpr | ID) ('<<-' (NUMBER | ID) '-' modelExpr)?;

numberDeclarationList	: numberDeclaration (',' numberDeclaration)*;
numberDeclaration		: ID ('=' (NUMBER | ID))?;

booleanDeclarationList	: booleanDeclaration (',' booleanDeclaration)*;
booleanDeclaration		: ID ('=' (BOOLEAN | ID))?;

// ASSIGNMENTS
assignment	: ID ('=' | '<--') expression | expression '-->' (type)? ID;
expression	: unitExpr | layerExpr | shapeExpr | modelExpr;

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

type: 'UNIT'
	| 'LAYER'
	| 'SHAPE'
	| 'MODEL'
	| 'NUMBER'
	| 'BOOLEAN';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: ('-')? [0-9]+ ('.' [0-9]+)?;
BOOLEAN: 'TRUE' | 'FALSE' | '1' | '0';

COLOR:
	'*' ( 'red'
		| 'blue'
		| 'green'
		| 'white'
		| 'black'
		| 'yellow'
		| 'lilac' ) '*';

PATTERN: '*' ( 'striped' | 'dotted' | 'gradient') '*';

WS: [ \t]+ -> skip;
NEWLINE: '\r'? '\n';