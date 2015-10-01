from helpers import *
from itertools import groupby

def remove_unit(gram):
    gens  = [p for p in gram if not unit(p)]
    units = [p for p in gram if unit(p)]

    # Compute symbols accessible by unit productions
    dircloz = {s: set(rhs(p)[0] for p in px)
                                for s, px in groupby(units, lhs)}

    # Compute closure
    cloz, new = None, dircloz.copy()
    while cloz != new:
        cloz, new = new, {}
        for s in cloz:
            for ss in cloz[s]:
                if ss in cloz:
                    new[s] = cloz[s].union(cloz[ss])
                else:
                    new[s] = cloz[s]

    # Create new productions
    newpx = []
    for s in cloz:
        for ss in cloz[s]:
            for p in gens:
                if lhs(p) == ss:
                    newpx.append((s, tuple(rhs(p))))

    return gens + newpx


if __name__ == '__main__':
    gram = [('S', ('A', 'B')),
            ('S', ('A')),
            ('A', ('a', 'B')),
            ('A', ('b', 'A')),
            ('A', ('a', 'S', 'b')),
            ('B', ('S')),
            ('B', ('b'))]

    print(format_grammar(remove_unit(gram)))
