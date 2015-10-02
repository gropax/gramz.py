def nonterms(gram):
    nx = []
    for p in gram:
        for s in (p[0],) + p[1]:
            if nonterm(s) and not s in nx:
                nx.append(s)
    return nx

def term(sym):
    return str.lower(sym[0]) == sym[0]

def nonterm(sym):
    return not term(sym)

def newsym(syms, sym):
    if sym in syms:
        i, s = 0, sym + "0"
        while s in syms:
            i += 1
            s = sym + str(i)
        return s
    else:
        return sym
