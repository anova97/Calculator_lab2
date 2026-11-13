"""Calculator testing module"""

from calculator import Calculator

class TestCalculator():
    def testSum(self):
        """Test the sum of the operands"""
        calc = Calculator(op1=1, op2=2)
        assert calc.sum() == 3

    def testSubtract(self):
        """Test the subtract of the operands"""
        calc = Calculator(op1=3, op2=2)
        assert calc.subtract() == 1

    def testMultiply(self):
        """Test the product of the operands"""
        calc = Calculator(op1=2, op2=2)
        assert calc.multiply() == 4

    def testDivide(self):
        """Test the division of the operands"""
        calc = Calculator(op1=4, op2=2)
        assert calc.divide() == 2
