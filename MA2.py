"""
Solutions to module 2 - A calculator
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""
import math
import statistics
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper
import numpy as np


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class Error(Exception): 
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if not wtok.is_at_end():
        raise SyntaxError(f"Unexpected token '{wtok.get_current()}' after end of statement")
    return result

def arglist(wtok, variables): 
    if wtok.get_current() != "(":
        raise SyntaxError(f"Expected '(' after function")
    args = []
    wtok.next()
    args.append(assignment(wtok, variables)) 
    while wtok.get_current() == ",":
        wtok.next()
        args.append(assignment(wtok,variables))
    if wtok.get_current() != ")":
        raise SyntaxError("Expected ')'")
    return args 

def assignment(wtok, variables):
    """See syntax chart for assignment"""
    result =  expression(wtok, variables)
    while wtok.get_current() == "=":
        wtok.next()
        if not wtok.is_name():  
            raise SyntaxError("Expected variable after '='")
        elif wtok.get_current() == "PI" or wtok.get_current() == "E":
            raise SyntaxError(f"{wtok.get_current()} cannot be assign a value")
        key = wtok.get_current()
        variables[str(key)] = result
        wtok.next() 
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == "-":
        if wtok.get_current() == "+":
            wtok.next()
            if wtok.get_current() == "+": 
                raise SyntaxError("Expected number, word or '('")
            result = result + term(wtok, variables)
        elif wtok.get_current() == "-":
            wtok.next()
            result = result - term(wtok, variables)
    #if wtok.get_current() not in ('+', '-'):
        #raise Error(f"Unexpected token '{wtok.get_current()}'")
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == "/": 
        if wtok.get_current() == "*":
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == "/":
            wtok.next()
            divisor = factor(wtok, variables)
            if divisor == 0: 
                raise EvaluationError("Division by zero") 
            else: 
                result = result / divisor
        else: 
            if wtok.get_current() not in ("*", "/"):
                raise Error("Unexpected token")
    return result

def fib(n):
    memory = {0: 0, 1: 1}

    def fib_mem2(n):
        if n < 0: 
            raise EvaluationError(f"Argument to fib is {n}. Must be integer >= 0")
        elif n not in memory: 
            memory[n] = fib_mem2(n-1) + fib_mem2(n-2)
        return memory[n]
    
    return fib_mem2(n)
    
def fac(n): 
    mem = {}

    def fac_mem(n):
        if n == 1: 
            return 1 
        elif n in mem: 
            return mem[n]
        mem[n] = n*fac_mem(n-1)
        return mem[n]
    
    return fac_mem(n)
    

def factor(wtok, variables):
    """ See syntax chart for factor"""
    function_1 = {"log": math.log, "fib": fib, "fac": math.factorial, "sin": np.sin, "cos": np.cos, "exp": np.exp}
    function_n = {"sum": sum, "max": max, "min": min, "mean": np.mean, "std": statistics.stdev}
    
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        wtok.next()
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    elif wtok.is_name():
        name = wtok.get_current()
        if name in function_1: 
            wtok.next()
            if wtok.get_current() == "(": 
                wtok.next()
                arg = assignment(wtok, variables)
                if arg <= 0 and name == "log":
                    raise EvaluationError(f"Input to '{name}' cannot be less than 0")
                elif (arg < 0 or (type(arg) != int and not arg.is_integer())) and name == "fac": 
                    raise EvaluationError(f"Input to '{name}' cannot be less than 0 or a non-integer")
                elif (arg >= 0 or (type(arg) != int and not arg.is_integer())) and name == "fac":
                    arg = int(arg)
                elif wtok.get_current() != ")":
                    raise SyntaxError(f"Expected ')' after function '{arg}' ")
                wtok.next()
                result = function_1[name](arg)
            else: 
                raise SyntaxError(f"Expected '(' after function '{name}'")
        elif name in function_n:
            wtok.next()
            args = arglist(wtok, variables)
            result = function_n[name](args)
            wtok.next()
        elif name in variables: 
            result = float(variables[name])
            wtok.next()
        else: 
            raise EvaluationError(f"Undefined variable or function '{name}'")
    elif wtok.get_current() == "-": 
        wtok.next() 
        result = -factor(wtok, variables)
    else:
        raise SyntaxError("Expected number or '('")              
    return result


def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')

        if line == '' or line[0]=='#':
            continue

        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            for var_name, value in variables.items():
                print(f"{var_name} : {value}")
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)
            except SyntaxError as se:
                print("*** Syntax error: ", se)
                if wtok.get_current() is None or wtok.is_at_end(): 
                    print(f"Error occurred at '*EOL*' just after '{wtok.get_previous()}'")
                else:
                    print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")
            except EvaluationError as se:
                print("*** Evaluation error: ", se)
            except Error as se:
                print("*** Error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")
            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
        


if __name__ == "__main__":
    main()