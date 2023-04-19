/* 参考设计, SQL, MLSQL
 * 
 * MLSQL:
 * https://github.com/byzer-org/byzer-lang/blob/master/streamingpro-dsl/src/main/resources/DSLSQL_v2
 */
grammar FGL;
// options { caseInsensitive = true; } Rules
prog: (sqlStatement ender+)* sqlStatement? EOF;
sqlStatement: ddlStatement | dmlStatement | dqlStatement;
dqlStatement: show | showAlls;
ddlStatement: create;
dmlStatement:
	load
	| config
	| save
	| train
	| predict
	| call
	| ret
	| delete;

load:
	LOAD FORMAT '.' STRING_LITERAL setArguments? (AS identifier)?;
save:
	SAVE FORMAT '.' STRING_LITERAL setArguments? (AS identifier)?;

connect: CONNECT FORMAT '.' STRING_LITERAL setArguments? (AS identifier)?;
disconnect: DISCONNECT FORMAT '.' STRING_LITERAL setArguments? (AS identifier)?;

config: connect | disconnect;

create: createParadigm | createDatamodel | createJob;

// run: RUN expr? module '.' STRING_LITERAL setArguments? ( AS identifier )?;
train:
	TRAIN (expr ',')* expr? module ('.' STRING_LITERAL)? setArguments? (
		AS (identifier ',')* identifier?
	)?;
// predict: PREDICT (expr ',')* expr? module ('.' STRING_LITERAL)? setArguments? ( AS (identifier
// ',')* identifier? )?;
predict:
	PREDICT (expr ',')* expr? module '.' STRING_LITERAL? setArguments? (
		AS (identifier ',')* identifier?
	)?;
setArguments: WHERE setArgument*;
setArgument: (parameter checkOp expr AND?);
conditions: WHERE (expr checkOp expr conditionOp?)*;
macro_key: (PARADIGM | DATAMODEL | JOB);
call: (CALL|TRAIN|PREDICT) macro_key? macro_name argument? setArguments? (AS identifier)?;
ret: RETURN expr;
module: IDENTIFIER;
checkOp: '=' | '!=' | '==';
conditionOp: AND | OR;
contextKey: '.'(CALL|TRAIN|PREDICT);
createParadigm:
	CREATE (OR REPLACE)? PARADIGM contextKey? IDENTIFIER argument_typing begin_block;

createDatamodel:
	CREATE (OR REPLACE)? DATAMODEL IDENTIFIER argument_typing begin_block;

createJob:
	CREATE (OR REPLACE)? JOB IDENTIFIER  begin_block setArguments?;
showAlls: SHOW (PARADIGMS | JOBS | DATAMODELS);
showMacro: SHOW (PARADIGM | JOB | DATAMODEL) identifier;
show: showMacro;
deleteMacro: DELETE (PARADIGM | JOB | DATAMODEL) identifier;
delete: deleteMacro;
// showParadigm: SHOW PARADIGM identifier?;
begin_block: BEGIN block_content END;
block_content: .*?;
argument_typing: '(' (expr TYPING ','?)* ')';
argument: '(' (expr ','?)* ')';
expr:
	expr ('*' | '/') expr
	| expr ('+' | '-') expr
	| identifier
	| constant
	| function
	| '(' expr ')';
function: identifier argument;
ender: ';';
identifier: IDENTIFIER_TEMPLATE | IDENTIFIER | FORMAT;
parameter: IDENTIFIER_TEMPLATE | IDENTIFIER | FORMAT;
macro_name: IDENTIFIER | FORMAT;
json:
	'{' (STRING_LITERAL ':' constant ',')* (
		STRING_LITERAL ':' constant
	)? '}';
array: '[' (constant ',')* (constant)? ']';
constant: (NUMBER | STRING_LITERAL | BOOLEAN | json | array);
// Ignore Case 

fragment DOT: '.';
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
fragment DQUOTA_STRING:
	'"' ('\\' .  | '""' | ~('"' | '\\'))* '"';
fragment SQUOTA_STRING:
	'\'' ('\\' .  | '\'\'' | ~('\'' | '\\'))* '\'';
fragment BQUOTA_STRING:
	'`' ('\\' .  | '``' | ~('`' | '\\'))* '`';
fragment FALSE: 'false' | 'FALSE' | 'False';
fragment TRUE: 'true' | 'TRUE' | 'True';

// Lexer 

// keywords
AS: 'as' | 'AS';
LOAD: 'load' | 'LOAD';
SAVE: 'save' | 'SAVE';
// SELECT: 'select' | 'SELECT';
INSERT: 'insert' | 'INSERT';
CREATE: 'create' | 'CREATE';
DROP: 'drop' | 'DROP';
REFRESH: 'refresh' | 'REFRESH';
SET: 'set' | 'SET';
CONNECT: 'connect' | 'CONNECT';
DISCONNECT: 'disconnect' | 'DISCONNECT';
TRAIN: 'train' | 'TRAIN' | 'run' | 'RUN';
// RUN: 'run' | 'RUN';
PREDICT: 'predict' | 'PREDICT';
REGISTER: 'register' | 'REGISTER';
UNREGISTER: 'unregister' | 'UNREGISTER';
INCLUDE: 'include' | 'INCLUDE';
OPTIONS: 'options' | 'OPTIONS';
WHERE: 'where' | 'WHERE';
PARTITIONBY: 'partitionBy' | 'partitionby' | 'PARTITIONBY';
OVERWRITE: 'overwrite' | 'OVERWRITE';
APPEND: 'append' | 'APPEND';
SHOW: 'show' | 'SHOW';
ERRORIfExists:
	'errorifexists'
	| 'errorIfExists'
	| 'ERRORIFEXISTS';
IGNORE: 'ignore' | 'IGNORE';
// Relation Keywords
AND: 'and' | 'AND';
OR: 'or' | 'OR';
NOT: 'not' | 'NOT';

// Custom Keywords
REPLACE: 'replace' | 'REPLACE';
DELETE: 'delete' | 'DELETE';

PARADIGM: 'paradigm' | 'PARADIGM' | 'function' | 'FUNCTION';
JOB: 'job' | 'JOB';
DATAMODEL: 'datamodel' | 'DATAMODEL';

PARADIGMS:
	'paradigms'
	| 'PARADIGMS'
	| 'functions'
	| 'FUNCTIONs';
JOBS: 'jobs' | 'JOBS';
DATAMODELS: 'datamodels' | 'DATAMODELS';

BEGIN: 'begin' | 'BEGIN';
END: 'end' | 'END';
CALL: 'call' | 'CALL' | 'select' | 'SELECT';
RETURN: 'return' | 'RETURN';
// 
FORMAT: 'hdfs' | 'csv' | 'parquet' | 'jdbc' | 'dataset' | 'ftp' | 'mysql' | 'kafka' | 'postgres';
TYPING:
	'string'
	| 'str'
	| 'int'
	| 'number'
	| 'float'
	| 'bool'
	| 'boolean'
	| 'json'
	| 'array';
NUMBER: (DIGIT|'.')+;
// BLOCK: BEGIN .*? END;
BOOLEAN: TRUE | FALSE;

STRING_LITERAL: DQUOTA_STRING | SQUOTA_STRING | BQUOTA_STRING;
NEWLINE: [\r\n]+ -> skip;
WS: [ \t\n\r\f]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
CLINE_COMMENT: '//' ~[\r\n]* -> skip;
PLINE_COMMENT: '#' ~[\r\n]* -> skip;
SLINE_COMMENT: '--' ~[\r\n]* -> skip;
IDENTIFIER: (LETTER | DIGIT | '_')+;
IDENTIFIER_TEMPLATE: '$' (LETTER | DIGIT | '_' | '.')*;
// ENDER: ';';

