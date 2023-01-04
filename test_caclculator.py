"""
Unit test for the calculator library
"""


import calculator


class TestCalculator:
    """  test """
    def test_addition(self):
        """ Add test """
        assert 10 == calculator.add(4, 6)

    def test_subtraction(self):
        """ subtraction test """
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        """ multiply test """
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        """ division test """
        assert 10 == calculator.division(100, 10)

    def test_failed_division(self):
        """ failed division test """
        assert 10 != calculator.division(100, 20)