from nose.tools import *
from gramz import grammar, remove_unreachable

input = [('S', ('c', 'A')),
         ('A', ('a', 'C')),
         ('B', ('C', 'A')),
         ('C', ('c')),
         ('D', ('a', 'A'))]

expected = [('S', ('c', 'A')),
            ('A', ('a', 'C')),
            ('C', ('c'))]

class TestRemoveUnreachable:
    def setup(self):
        self.input = grammar(input)
        self.expected = grammar(expected)

    def test_remove_unreachable(self):
        output = remove_unreachable(self.input)
        assert_equal(output, self.expected)
