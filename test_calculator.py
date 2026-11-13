from calculator import Calculator

class TestCalculator():
    def testSum(self):
        calc = Calculator(op1=1, op2=2)
        assert calc.sum() == 3

    def testSubtract(self):
        calc = Calculator(op1=3, op2=2)
        assert calc.subtract() == 1

    def testMultiply(self):
        calc = Calculator(op1=2, op2=2)
        assert calc.multiply() == 4

    def testDivide(self):
        calc = Calculator(op1=4, op2=2)
        assert calc.divide() == 2
