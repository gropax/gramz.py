def initsym(gram):
    return gram[0][0]

def nonterms(gram):
    nx = []
    for p in gram:
        for s in (p[0],) + p[1]:
            if nonterm(s) and not s in nx:
                nx.append(s)
    return nx

def lhs(prod):
    return prod[0]

def rhs(prod):
    return prod[1]

def unit(prod):
    return len(prod[1]) == 1 and nonterm(prod[1][0])

def epsilon(prod):
    return prod[1] == []

def term(sym):
    return str.lower(sym[0]) == sym[0]

def nonterm(sym):
    return not term(sym)

def format_grammar(gram):
    return "\n".join(lhs(p) + " => " + (" ".join(rhs(p)) or u"\u03B5") for p in gram)
