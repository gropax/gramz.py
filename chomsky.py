def replace_terms(p, px):
    if len(rhs(p)) == 1:
        return p
    else:
        sx = []
        for s in rhs(p):
            if term(s):
                n = "_" + str.upper(s)
                px.add((n, (s)))
                sx.append(n)
            else:
                sx.append(s)
        return (lhs(p), tuple(sx))

def break_up(p):
    if len(rhs(p)) <= 2:
        return [p]
    else:
        s0, *sx = rhs(p)
        s = "_" + "".join(sx)
        newp = (lhs(p), (s0, s))
        return [newp] + break_up((s, tuple(sx)))

def chomsky_normal_form(gram):
    # Remove terms from complex productions
    termp = set()
    step1 = [replace_terms(p, termp) for p in gram] + list(termp)
    # Break long productions into binary ones
    return sum([break_up(p) for p in step1], [])
