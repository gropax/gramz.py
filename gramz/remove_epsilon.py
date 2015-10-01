from gramz import *

def remove_epsilon(gram):
    # Compute nullable symbols
    null, new = None, set()
    while null != new:
        null = new.copy()
        new.update(p.lhs for p in gram
                          if p.epsilon or all(s in null for s in p.rhs))

    newi, newp = gram.init, []

    # If initial symbol is nullable, add a new one on top
    if gram.init in null:
        newi = gram.init + "'"
        newp = [Production(newi, (gram.init)),
                Production(newi, ())]

    # Build rules
    for p in gram:
        if not p.epsilon():
            combs = [[]]
            for s in p.rhs:
                new = [c + [s] for c in combs]
                combs = combs + new if s in null else new
            newp += [Production(p.lhs, c) for c in combs if c]

    return Grammar(newi, newp)
