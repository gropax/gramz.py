from nose.tools import *
from gramz import grammar, newsym

data = [('S', ('B', 'B0', 'C4', 'B1'))]

class TestHelpers:
    def setup(self):
        self.gram = grammar(data)

    def test_newsym(self):
        syms = self.gram.symbols()
        assert_equal(newsym(syms, 'C'), 'C')
        assert_equal(newsym(syms, 'S'), 'S0')
        assert_equal(newsym(syms, 'B'), 'B2')
