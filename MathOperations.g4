// GROUP: RA1 18
// AUTHOR: Guilherme Ribeiro Thomaz
// COURSE: Fundamentos de Sistemas Ciberfísicos


grammar MathOperations;

expr
    : '(' operationExpr ')'       // For regular operations
    | '(' memExpr ')'             // For expressions ending with MEM
    | '(' resExpr ')'             // For expressions with RES, correctly followed
    | '(' 'MEM' item op ')'             // For expressions with RES, correctly followed
    ;

operationExpr
    : item item op                // For two inputs and an operation
    | item 'RES' item op          // Adjustment to handle RES correctly
    ;

memExpr
    : item 'MEM'         // For an operation followed by MEM
    | resExpr 'MEM'               // For a RES expression followed by MEM
    ;

resExpr
    : '(' item 'RES' ')' item op  // For RES in parentheses, followed by an item and operation
    | item '(' item 'RES' ')' op  // For RES in parentheses, directly followed by MEM
    | '(' item 'RES' ')' 'MEM'  // For RES in parentheses, directly followed by MEM
    |  item 'RES'  // For RES in parentheses, directly followed by MEM
    ;

item
    : NUMBER                      // For numbers
    | '(' operationExpr ')'                         // For nested expressions, allowing recursion
    | '(' resExpr ')'                        // For nested expressions, allowing recursion
    | '(' 'MEM' item op ')'                        // For nested expressions, allowing recursion
    ;

op
    : '+' | '-' | '*' | '/' | '^' | '%' | '|'// For operations
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?        // For integer and floating-point numbers
    ;

MEM    : 'MEM' ;                 // Definition of MEM
RES    : 'RES' ;                 // Definition of RES

WS     : [ \t\r\n]+ -> skip ;    // To ignore whitespace