# GROUP: RA1 18
# AUTHOR: Guilherme Ribeiro Thomaz
# COURSE: Fundamentos de Sistemas Ciberfísicos

import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from output.MathOperationsLexer import MathOperationsLexer
from output.MathOperationsParser import MathOperationsParser

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = f"Error: {msg}"
        self.errors.append(error)

    # Other error handling methods...

def evaluate_expression(expression):
    input_stream = InputStream(expression)
    lexer = MathOperationsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathOperationsParser(stream)
    
    errorListener = CustomErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(errorListener)
    parser.removeErrorListeners()
    parser.addErrorListener(errorListener)
    
    tree = parser.expr()
    return tree.toStringTree(recog=parser), errorListener.errors

def main():
    print("Reading expressions from file...\n")
    reports_dir = './tests/reports'
    os.makedirs(reports_dir, exist_ok=True)  # Create the directory if it doesn't exist
    
    for file in os.listdir('./tests'):
        if file.endswith('.txt'):
            valid_file_path = os.path.join(reports_dir, f'{file}_valid.txt')
            invalid_file_path = os.path.join(reports_dir, f'{file}_invalid.txt')

            with open(valid_file_path, 'w') as valid_file, open(invalid_file_path, 'w') as invalid_file:
                with open(f'./tests/{file}', 'r') as test_file:
                    for line in test_file:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            tree, errors = evaluate_expression(line)
                            if errors:
                                invalid_file.write(f"Expression: {line}\n{'\n'.join(errors)}\n\n")
                            else:
                                valid_file.write(f"Expression: {line}\nTree: {tree}\n\n")

if __name__ == '__main__':
    main()
