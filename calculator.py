"""Calculator module"""

class Calculator:
    """Calculator that performs basic arithmetic operations"""
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        """Return the sum of the operands"""
        return self.op1 + self.op2

    def subtract(self):
        """Subtract the second operand from the first."""
        return self.op1 - self.op2

    def multiply(self):
        """Return the product of the operands."""
        return self.op1 * self.op2

    def divide(self):
        """Divide the operands or return a message for division by zero."""
        if self.op2 == 0:
            return "Cannot divide by zero."
        return self.op1 / self.op2

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator(10, 2)

    print("Sum:", calc.sum())
    print("Subtraction:", calc.subtract())
    print("Multiplication:", calc.multiply())
    print("Division:", calc.divide())

    calc_zero = Calculator(10, 0)
    print("Division by zero:", calc_zero.divide())
