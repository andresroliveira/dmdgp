from dmdgp.branch_prune import bp
from dmdgp.symmetry import sym
from dmdgp import Graph


def main():
    n, m = 0, 0
    edges = []

    with open('andres_7_18.in', 'r') as f:
        n, m = map(int, f.readline().split())

        for _ in range(m):
            l = f.readline().split()
            u, v = map(int, l[:2])
            duv = float(l[2])
            edges.append((u, v, duv))

    g = Graph(n, edges=edges)
    # g.symetries()
    sym(g)


if __name__ == '__main__':
    main()