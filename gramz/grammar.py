from gramz.helpers import *

class Grammar:
    def __init__(self, init, prods):
        self.init = init
        self.productions = set(prods)

    def symbols(self):
        return set(s for p in self.productions for s in p.symbols())

    def __iter__(self):
        return self.productions.__iter__()

    def __eq__(self, other):
        return (self.init == other.init and
                self.productions == other.productions)

    def __str__(self):
        return "\n".join(str(p) for p in self.productions)
