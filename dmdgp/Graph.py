from . import symmetry
import numpy as np

VERBOSE = False
# VERBOSE = True


class Graph:

    def __init__(self,
                 n: int,
                 edges: list[tuple[int, int, float]] = None,
                 adj: list[list] = None,
                 matrix: list[list[float]] = None) -> None:

        if isinstance(n, int) and n >= 4:
            self.n = n
        else:
            raise ValueError("n must be an integer greater than 4")

        if edges is None and adj is None and matrix is None:
            raise ValueError(
                "edges, adj and matrix can not be None at the same time.")

        if not edges is None:
            self.edges = edges.copy()
            self.adj = [[] for _ in range(n + 1)]
            self.matrix = np.zeros((n + 1, n + 1))

            for u, v, duv in self.edges:
                self.adj[u].append((v, duv))
                self.adj[v].append((u, duv))
                self.matrix[u, v] = duv
                self.matrix[v, u] = duv

            if VERBOSE:
                print(self.edges)
                print(self.adj)
                with np.printoptions(linewidth=np.inf):
                    print(self.matrix)

        # TODO adj is not None
        # TODO matrix is not None

        self.prune = [(u, v) for u, v, _ in edges if abs(u - v) > 3]
        if VERBOSE: print(self.prune)

    def __len__(self) -> int:
        return len(self.edges)

    def __str__(self) -> str:
        return f'Graph with {self.n} nodes and {len(self)} edges'

    def __int__(self) -> int:
        return self.n

    def __iter__(self):
        return iter(self.edges)

    def __list__(self) -> list:
        return self.edges

    def prune_edges(self) -> list:
        return self.prune

    def symetries(self):
        symmetry.sym(self)
