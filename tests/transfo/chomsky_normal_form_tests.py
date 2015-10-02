from nose.tools import *
from gramz import grammar, chomsky_normal_form

input = [('S', ('a', 'S', 'b', 'S')),
         ('S', ())]

expected = [("S'", ('S')),
            ("S'", ()),
            ('S', ('a', 'S', 'b', 'S')),
            ('S', ('a', 'b', 'S')),
            ('S', ('a', 'S', 'b')),
            ('S', ('a', 'b'))]

class TestChomskyNormalForm:
    def setup(self):
        self.input = grammar(input)
        self.expected = grammar(expected)

    def test_chomsky_normal_form(self):
        output = chomsky_normal_form(self.input)
        print(str(output) + "\n\n" + str(self.expected))
        assert_equal(output, self.expected)
