from mycalc2.models import add, subtract


class TestCalculator:
    def test_addition(self):
        assert 4 == add(2, 2)

    def test_subtraction(self):
        assert 2 == subtract(4, 2)
