from gramz import *

# @note
#     Expect a proper grammar as input.
#
def chomsky_normal_form(gram):
    # Remove terms from complex productions
    step1 = set()
    syms = gram.symbols()
    for p in gram:
        if len(p.rhs) == 1:
            step1.add(p)
        else:
            sx = []
            for s in p.rhs:
                if term(s):
                    n = newsym(syms, str.upper(s[0]))
                    syms.add(n)
                    step1.add(Production(n, (s)))
                    sx.append(n)
                else:
                    sx.append(s)
            step1.add(Production(p.lhs, sx))

    def break_up(p):
        if len(p.rhs) <= 2:
            return [p]
        else:
            s0, *sx = p.rhs
            s = newsym(syms, 'X')
            syms.add(s)
            newp = Production(p.lhs, (s0, s))
            return [newp] + break_up(Production(s, sx))

    # Break long productions into binary ones
    newp = sum([break_up(p) for p in step1], [])

    return Grammar(gram.init, newp)
