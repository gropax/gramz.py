from nose.tools import *
from gramz import grammar

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

    def symbols(self):
        assert_set_equal(self.gram.symbols(),
                         set(['S', 'A', 'B', 'C', 'a', 'b', 'c']))
