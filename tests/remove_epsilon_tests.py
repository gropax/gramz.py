from nose.tools import *
from gramz import grammar, remove_epsilon

input = [('S', ('a', 'S', 'b', 'S')),
         ('S', ())]

expected = [("S'", ('S')),
            ("S'", ()),
            ('S', ('a', 'S', 'b', 'S')),
            ('S', ('a', 'b', 'S')),
            ('S', ('a', 'S', 'b')),
            ('S', ('a', 'b'))]

class TestRemoveEpsilon:
    def setup(self):
        self.input = grammar(input)
        self.expected = grammar(expected)

    def test_remove_epsilon(self):
        output = remove_epsilon(self.input)
        print(str(output) + "\n\n" + str(self.expected))
        assert_equal(output, self.expected)
