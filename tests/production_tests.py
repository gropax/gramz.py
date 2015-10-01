from nose.tools import *
from gramz import *

prod = ('S', ('c', 'B', 'C'))
unit = ('S', ('B',))
epsilon = ('S', ())

class TestProduction:
    def setup(self):
        self.prod = Production(*prod)
        self.unit = Production(*unit)
        self.epsilon = Production(*epsilon)

    def test_lhs(self):
        assert_equal(self.prod.lhs, 'S')

    def test_rhs(self):
        assert_equal(self.prod.rhs, ('c', 'B', 'C'))

    def test_symbols(self):
        assert_set_equal(self.prod.symbols(),
                         set(['S', 'B', 'C', 'c']))

    def test_unit(self):
        assert_true(self.unit.unit())
        assert_false(self.prod.unit())
        assert_false(self.epsilon.unit())

    def test_epsilon(self):
        assert_true(self.epsilon.epsilon())
        assert_false(self.prod.epsilon())
        assert_false(self.unit.epsilon())

    def test_hash_key(self):
        assert_equal(hash(self.prod), hash(('S', ('c', 'B', 'C'))))

    def test_equality(self):
        copy = Production(*prod)
        assert_equal(self.prod, copy)

    def test_equality_in_set(self):
        copy = Production(*prod)
        s = set([self.prod, copy])
        assert_equal(len(s), 1)
