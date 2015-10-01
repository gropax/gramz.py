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
        eps_free = [(new_init, (initsym(gram))),
                    (new_init, ())]
    # Build rules
    for p in gram:
        if not epsilon(p):
            combs = [[]]
            for s in rhs(p):
                new = [c + [s] for c in combs]
                combs = combs + new if s in null else new
            eps_free += [(lhs(p), tuple(c)) for c in combs if c]

    return eps_free
