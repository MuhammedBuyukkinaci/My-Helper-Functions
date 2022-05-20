import numbers
import sys

class CalculatorError(Exception):
    """An exception class for Calculator"""

class Calculator:
    """A terrible calculator"""

    # def add(self,a,b):
    #     try:
    #         return a + b
    #     except TypeError:
    #         raise CalculatorError('')
    
    def add(self,a,b):
        self._check_operand(a)
        self._check_operand(b)
        return a+b


    def subtract(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def divide(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            raise CalculatorError("Can't divide by zero")

    def _check_operand(self,operand):
        if not isinstance(operand,numbers.Number):
            raise CalculatorError(f"'{operand}' wasn't a number" )


if __name__ == '__main__':
    print("Let's calculate")
    calculator = Calculator()
    operations = [
    calculator.add,
    calculator.subtract,
    calculator.multiply,
    calculator.divide
    ]
    while True:
        print("Pick an operation")
        for i, operation in enumerate(operations,start=1):
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        operation = input("Pick an operation:")

        if operation == 'q':
            sys.exit()
        
        op = int(operation)

        a = float(input("what is a?"))
        b = float(input("what is b?"))

        try:
            print(operations[op-1](a,b))
        except CalculatorError as ex:
            print(ex)