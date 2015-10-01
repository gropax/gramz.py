from gramz.helpers import *

class Grammar:
    def __init__(self, prods):
        self.productions = set(prods)
        self.init = prods[0].lhs

    def symbols(self):
        return set(s for p in self.productions for s in p.symbols)

    def nonterms(gram):
        return set(s for s in self.symbols() if nonterm(s))

    def __iter__(self):
        return self.productions.__iter__()

    def __str__(self):
        #return "\n".join(str(p) for p in self.productions)
        return "\n".join(self.productions)
