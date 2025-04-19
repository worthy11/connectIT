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
expression:
	| idCast
	| unitExpr
	| layerExpr
	| shapeExpr
	| modelExpr
	| numericExpr
	| booleanExpr;

unitExpr: (PATTERN)? COLOR | (COLOR)? PATTERN;

layerExpr: layerTerm ('+' layerTerm)* ('CLOSED')?;
layerTerm:
	idCast
	| '[' unitExpr ']'
	| numericExpr (idCast | '[' unitExpr ']');

shapeExpr: shapeTerm shapeConnector*;
shapeTerm: (idCast | '[' layerExpr ']');
shapeConnector:
	'<-' shapeTerm
	| '<<-' shapeTerm
	| '<-' '(' numericExpr ')' '-' shapeTerm
	| '<<-' '(' numericExpr ')' '-' shapeTerm;

modelExpr: modelTerm modelConnector*;
modelTerm: (idCast | '[' shapeExpr ']');
modelConnector:
	'<-' modelTerm
	| '<<-' modelTerm
	| '<-' '(' numericExpr ')' '-' modelTerm
	| '<<-' '(' numericExpr ')' '-' modelTerm;
idCast: '[' idCast ']' | ID;

numericExpr: ID | NUMBER; // placeholder
booleanExpr: ID | BOOLEAN; // placeholder

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

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: '-'? [0-9]+;
BOOLEAN: 'TRUE' | 'FALSE' | '1' | '0';

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