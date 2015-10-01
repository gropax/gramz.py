import helpers
import unreachable
import unproductive
from unit import *
import epsilon
import chomsky

gram = [('S', ('A', 'B')),
        ('S', ('A')),
        ('A', ('a', 'B')),
        ('A', ('b', 'A')),
        ('A', ('a', 'S', 'b')),
        ('B', ('S')),
        ('B', ('b'))]

g2 = remove_unit(gram)

print(format_grammar(g2))
