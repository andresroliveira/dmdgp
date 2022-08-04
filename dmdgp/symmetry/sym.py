import numpy as np
from ..Graph import Graph


def sym(g: Graph) -> list:
    n = int(g)
    prune = g.prune_edges()

    m = [0 for _ in range(n + 1)]

    for u, v in prune:
        m[u] = max(m[u], v)

    eps = [(i, m[i]) for i in range(n + 1) if m[i] != 0]

    print(eps)

    return []
