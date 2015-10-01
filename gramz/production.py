from gramz.helpers import *

class Production:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = tuple(rhs)

    def epsilon(self):
        return not self.rhs

    def unit(self):
        return len(self.rhs) == 1 and nonterm(self.rhs[0])

    def symbols(self):
        return set((self.lhs,) + self.rhs)

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs

    def __hash__(self):
        return hash((self.lhs, self.rhs))

    def __str__(self):
        return self.lhs + " => " + (" ".join(self.rhs) or u"\u03B5")
