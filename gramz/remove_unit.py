from gramz import *
from itertools import groupby

def remove_unit(gram):
    gens  = [p for p in gram if not p.unit()]
    units = [p for p in gram if p.unit()]

    # Compute symbols accessible by unit productions
    access = {s: set(p.rhs[0] for p in px)
                for s, px in groupby(units, lambda p: p.lhs)}

    # Compute closure
    cloz, new = None, access.copy()
    while cloz != new:
        cloz, new = new, {}
        for s in cloz:
            for ss in cloz[s]:
                if ss in cloz:
                    new[s] = cloz[s].union(cloz[ss])
                else:
                    new[s] = cloz[s]

    # Create new productions
    newp = []
    for s in cloz:
        for ss in cloz[s]:
            for p in gens:
                if p.lhs == ss:
                    newp.append(Production(s, p.rhs))

    return Grammar(gram.init, gens + newp)
