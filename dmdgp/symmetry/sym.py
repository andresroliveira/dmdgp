import numpy as np
from ..Graph import Graph


def sym(g: Graph) -> list:
    n = int(g)
    prune = g.prune_edges()

    m = [0 for _ in range(n + 1)]

    for u, v in prune:
        m[u] = max(m[u], v)

    eps = [(i, m[i]) for i in range(n + 1) if m[i] != 0]

    s_bar = []

    if eps:
        l, r = eps[0]

        for vi, vmi in eps:
            if r >= vi + 3:
                r = max(vmi, r)
            else:
                s_bar.append((l + 4, r))
                l = vi
                r = vmi
        s_bar.append((l + 4, r))

    s = [4]
    i = 0

    for v in range(5, n + 1):
        u_bar, v_bar = s_bar[i]

        if u_bar > v or v > v_bar:  # if v \not \in [u_bar, v_bar]
            s.append(v)

        if v == v_bar and i + 1 < len(s_bar): i += 1

    return s
