from itertools import *
from functools import *

def initsym(gram):
    return gram[0][0]

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
    return "\n".join(lhs(p) + " => " + " ".join(rhs(p)) for p in gram)


gram = [('S', ['b', 'A']),
        ('A', ['a', 'A']),
        ('A', [])]



def remove_unreachable(gram):
    reach, new = None, set([initsym(gram)])
    while reach != new:
        reach = new.copy()
        new.update(s for p in gram for s in rhs(p)
                     if lhs(p) in reach and nonterm(s))
    return [p for p in gram if lhs(p) in reach]

def remove_unproductive(gram):
    prod, new = None, set()
    while prod != new:
        prod = new.copy()
        new.update(lhs(p) for p in gram
                          if all(term(s) or s in prod
                                     for s in rhs(p)))
    return [p for p in gram
              if all(term(s) or s in prod for s in rhs(p))]

def remove_epsilon(gram):
    # Compute nullable symbols
    null, new = None, set()
    while null != new:
        null = new.copy()
        new.update(lhs(p) for p in gram
                          if epsilon(p) or all(s in null for s in rhs(p)))
    eps_free = []

    # If initial symbol is nullable, add a new one on top
    if initsym(gram) in null:
        new_init = initsym(gram) + "'"
        eps_free = [(new_init, [initsym(gram)]),
                    (new_init, [])]
    # Build rules
    for p in gram:
        if not epsilon(p):
            combs = [[]]
            for s in rhs(p):
                new = [c + [s] for c in combs]
                combs = combs + new if s in null else new
            eps_free += [(lhs(p), c) for c in combs if c]

    return eps_free

# Expects an epsilon-free grammar
#
def remove_unit(gram):
    gens  = [p for p in gram if not unit(p)]
    units = [p for p in gram if unit(p)]
    dircloz = {s: set(rhs(p)[0] for p in px)
                                for s, px in groupby(units, lhs)}
    cloz, new = None, dircloz.copy()
    while cloz != new:
        cloz = new.copy()
        new = {s: cloz[s].union(cloz[ss]) for s  in cloz
                                          for ss in cloz[s]}
    return [(s, rhs(p)) for s  in cloz
                        for ss in cloz[s]
                        for p  in gens if lhs(p) == ss]

# Expects a proper grammar
#
def chomsky_normal_form(gram):
    tmp, toadd = [], set()
    for p in gram:
        if len(rhs(p)) == 1:
            tmp.append(p)
        else:
            prhs = []
            for s in rhs(p):
                if term(s):
                    n = "_" + str.upper(s)
                    toadd.add((n, s))
                    prhs.append(n)
                else:
                    prhs.append(s)
            tmp.append((lhs(p), prhs))

    tmp += [(n, [t]) for n, t in toadd]

    def break_up(p):
        if len(rhs(p)) <= 2:
            return [p]
        else:
            s0, *sx = rhs(p)
            s = "_" + "".join(sx)
            newp = (lhs(p), [s0, s])
            return [newp] + break_up((s, sx))

    return sum([break_up(p) for p in tmp], [])


gram1 = [('S', ['b', 'A']),
         ('A', ['a', 'A']),
         ('A', []),
         ('B', ['b', 'A'])]

#print(remove_unreachable(gram1))


gram2 = [('S', ['c', 'B', 'A', 'A', 'B']),
         ('B', ['b', 'A']),
         ('B', ['b']),
         ('A', ['a', 'A'])]

#print(remove_unproductive(gram2))

gram3 = [('S', ['c', 'B', 'C']),
         ('B', ['C', 'A']),
         ('B', ['b']),
         ('A', ['a', 'A']),
         ('A', []),
         ('C', [])]

#print(format_grammar(remove_epsilon(gram3)))

gram4 = [('S', ['A']),
         ('S', ['B']),
         ('A', ['B']),
         ('A', ['B']),
         ('A', ['a', 'B']),
         ('B', ['C']),
         ('B', ['b', 'b']),
         ('C', ['B']),
         ('C', ['a', 'A']),
         ('C', ['a', 'A', 'a'])]

#print(format_grammar(remove_unit(gram4)))

print(format_grammar(gram2) + "\n")
print(format_grammar(chomsky_normal_form(gram2)))
