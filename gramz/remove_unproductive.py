from gramz import *

def remove_unproductive(gram):
    prod, new = None, set()
    while prod != new:
        prod = new.copy()
        new.update(p.lhs for p in gram
                         if all(term(s) or s in prod
                                    for s in p.rhs))
    newp = [p for p in gram
              if all(term(s) or s in prod for s in p.rhs)]
    return Grammar(gram.init, newp)
