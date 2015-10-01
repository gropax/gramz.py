from gramz.helpers import *
from gramz.production import Production
from gramz.grammar import Grammar
from gramz.remove_unreachable import *
from gramz.remove_unproductive import *
from gramz.remove_epsilon import *
from gramz.remove_unit import *

def grammar(lst):
    init = lst[0][0]
    prods = [Production(*p) for p in lst]
    return Grammar(init, prods)
