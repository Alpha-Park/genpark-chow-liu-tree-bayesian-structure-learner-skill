class ChowLiuTreeLearner:
    """Optimal tree structure learning using Chow-Liu Maximum Spanning Tree."""
    def learn_tree(self, var_names: list[str], mutual_info_matrix: list[list[float]]) -> dict:
        n = len(var_names)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((mutual_info_matrix[i][j], i, j))

        edges.sort(reverse=True, key=lambda x: x[0])
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        tree_edges = []
        total_mi = 0.0

        for mi, u, v in edges:
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                tree_edges.append({
                    "u": var_names[u],
                    "v": var_names[v],
                    "mutual_information": round(mi, 4)
                })
                total_mi += mi
                if len(tree_edges) == n - 1:
                    break

        return {
            "num_variables": n,
            "tree_edges": tree_edges,
            "total_mutual_information": round(total_mi, 4)
        }
