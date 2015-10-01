def remove_unreachable(gram):
    reach, new = None, set([initsym(gram)])
    while reach != new:
        reach = new.copy()
        new.update(s for p in gram for s in rhs(p)
                     if lhs(p) in reach and nonterm(s))
    return [p for p in gram if lhs(p) in reach]
