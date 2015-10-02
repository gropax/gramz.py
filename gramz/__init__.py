from gramz.helpers import *
from gramz.production import Production
from gramz.grammar import Grammar
from gramz.transfo import *

def grammar(lst):
    init = lst[0][0]
    prods = [Production(*p) for p in lst]
    return Grammar(init, prods)
