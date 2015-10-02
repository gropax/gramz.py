from gramz import *

def replace_terms(p, px):
    if len(p.rhs) == 1:
        return p
    else:
        sx = []
        for s in p.rhs:
            if term(s):
                n = "_" + str.upper(s)
                px.add(Production(n, (s)))
                sx.append(n)
            else:
                sx.append(s)
        return Production(p.lhs, sx)

def break_up(p):
    if len(p.rhs) <= 2:
        return [p]
    else:
        s0, *sx = p.rhs
        s = "_" + "".join(sx)
        newp = Production(p.lhs, (s0, s))
        return [newp] + break_up(Production(s, sx))

def chomsky_normal_form(gram):
    # Remove terms from complex productions
    termp = set()
    step1 = [replace_terms(p, termp) for p in gram] + list(termp)
    # Break long productions into binary ones
    newp = sum([break_up(p) for p in step1], [])
    return Grammar(gram.init, newp)
