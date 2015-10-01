from nose.tools import *
from gramz import grammar, remove_unit

input = [('S', ('a', 'B')),
         ('S', ('A')),
         ('A', ('a', 'A')),
         ('A', ('B')),
         ('B', ('b', 'A'))]

expected = [('S', ('a', 'B')),
            ('S', ('a', 'A')),
            ('S', ('b', 'A')),
            ('A', ('a', 'A')),
            ('A', ('b', 'A')),
            ('B', ('b', 'A'))]


class TestRemoveUnit:
    def setup(self):
        self.input = grammar(input)
        self.expected = grammar(expected)

    def test_remove_unit(self):
        output = remove_unit(self.input)
        print(str(output) + "\n\n" + str(self.expected))
        assert_equal(output, self.expected)
