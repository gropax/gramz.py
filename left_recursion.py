from helpers import *
from itertools import groupby

def remove_direct_left_recursion(gram):
    prods = {s: list(px) for s, px in groupby(gram, lhs)}

    newg = []
    for s in nonterms(gram):
        # Collect left-recursive productions
        lrec, others = [], []
        for p in prods[s]:
            if rhs(p) and rhs(p)[0] == s:
                lrec.append(p)
            else:
                others.append(p)

        if lrec:
            ss = s + "'"
            for p in others:
                newg.append((lhs(p), rhs(p) + (ss,)))
            for p in lrec:
                newg.append((ss, rhs(p)[1:] + (ss,)))
            newg.append((ss, ()))
        else:
            newg += prods[s]

    return newg

def remove_left_recursion(gram):
    nterms = nonterms(gram)

    g2 = gram.copy()
    for s in nterms:
        g1 = None
        while g1 != g2:
            g1 = g2.copy()
            prods = {s: list(px) for s, px in groupby(g2, lhs)}

            for p in prods[s]:
                fst = rhs(p)[0]
                if nonterm(fst) and nterms.index(fst) < nterms.index(s):
                    g2.remove((s, rhs(p)))
                    for pp in prods[fst]:
                        g2.append((s, rhs(pp) + rhs(p)[1:]))

        g2 = remove_direct_left_recursion(g2)

    return g2


if __name__ == '__main__':
    gram = [('S', ('S', 'a')),
            ('S', ('b',))]

    print(format_grammar(remove_direct_left_recursion(gram)))

    gram2 = [('S', ('A', 'a')),
             ('A', ('S', 'b')),
             ('A', ('a',))]

    gram3 = [('A', ('B', 'x', 'y')),
             ('A', ('x',)),
             ('B', ('C', 'D')),
             ('C', ('A',)),
             ('C', ('c',)),
             ('D', ('d',))]

    print("\nbefore:\n")
    print(format_grammar(gram3))
    print("\nafter:\n")
    print(format_grammar(remove_left_recursion(gram3)))
