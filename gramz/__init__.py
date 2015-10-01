#from gramz.grammar import Grammar, Production
#import gramz.production
#import gramz.grammar
from gramz.production import Production
from gramz.grammar import Grammar

def grammar(lst):
    prods = [Production(*p) for p in lst]
    return Grammar(prods)
