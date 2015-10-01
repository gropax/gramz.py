from gramz import *

def remove_unreachable(gram):
    reach, new = None, set([gram.init])
    while reach != new:
        reach = new.copy()
        new.update(s for p in gram for s in p.rhs
                     if p.lhs in reach and nonterm(s))
    newp = [p for p in gram if p.lhs in reach]
    return Grammar(gram.init, newp)
