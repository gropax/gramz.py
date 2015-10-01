from nose.tools import *
from gramz import grammar, Production

data = [('S', ('c', 'B', 'C')),
        ('B', ('C', 'A')),
        ('B', ('b')),
        ('A', ('a', 'A')),
        ('A', ()),
        ('C', ())]

class TestGrammar:
    def setup(self):
        self.gram = grammar(data)

    def test_init(self):
        assert_equal(self.gram.init, 'S')

    def test_productions_is_a_set(self):
        assert_is_instance(self.gram.productions, set)

    def test_iterable(self):
        prods = set(p for p in self.gram)
        assert_set_equal(self.gram.productions, prods)

    def test_symbols(self):
        assert_set_equal(self.gram.symbols(),
                         set(['S', 'A', 'B', 'C', 'a', 'b', 'c']))

    def test_equal_if_same_init_and_prods(self):
        other = grammar(data)
        assert_equal(self.gram, other)

    def test_not_equal_if_different_init(self):
        other = grammar(data)
        other.init = 'A'
        assert_not_equal(self.gram, other)

    def test_not_equal_if_different_prods(self):
        other = grammar(data + [('A', ('b'))])
        assert_not_equal(self.gram, other)
