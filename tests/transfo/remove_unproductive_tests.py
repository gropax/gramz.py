from nose.tools import *
from gramz import grammar, remove_unproductive

input = [('S', ('b', 'A')),
         ('S', ('a', 'B')),
         ('A', ('a', 'A')),
         ('B', ('b', 'B')),
         ('B', ())]

expected = [('S', ('a', 'B')),
            ('B', ('b', 'B')),
            ('B', ())]

class TestRemoveUnproductive:
    def setup(self):
        self.input = grammar(input)
        self.expected = grammar(expected)

    def test_remove_unproductive(self):
        output = remove_unproductive(self.input)
        assert_equal(output, self.expected)
