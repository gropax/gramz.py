def nonterms(gram):
    nx = []
    for p in gram:
        for s in (p[0],) + p[1]:
            if nonterm(s) and not s in nx:
                nx.append(s)
    return nx

def term(sym):
    return str.lower(sym[0]) == sym[0]

def nonterm(sym):
    return not term(sym)


class Grammar:
    def __init__(self, prods):
        self.productions = prods
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

    def __hash__(self):
        return hash((self.lhs, self.rhs))

    def __str__(self):
        return lhs(p) + " => " + (" ".join(rhs(p)) or u"\u03B5")
