def remove_unproductive(gram):
    prod, new = None, set()
    while prod != new:
        prod = new.copy()
        new.update(lhs(p) for p in gram
                          if all(term(s) or s in prod
                                     for s in rhs(p)))
    return [p for p in gram
              if all(term(s) or s in prod for s in rhs(p))]
