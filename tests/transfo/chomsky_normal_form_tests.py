from nose.tools import *
from gramz import grammar, chomsky_normal_form

input = [('S', ('c', 'A', 'c', 'B')),
         ('A', ('a',)),
         ('B', ('b', 'A'))]

expected = [('S', ('C', 'X')),
            ('X', ('A', 'X0')),
            ('X0', ('C0', 'B')),
            ('A', ('a',)),
            ('B', ('B0', 'A')),
            ('B0', ('b',)),
            ('C', ('c',)),
            ('C0', ('c',))]

class TestChomskyNormalForm:
    def setup(self):
        self.input = grammar(input)
        self.expected = grammar(expected)

    def test_chomsky_normal_form(self):
        output = chomsky_normal_form(self.input)
        print(str(output) + "\n\n" + str(self.expected))
        assert_equal(output, self.expected)
