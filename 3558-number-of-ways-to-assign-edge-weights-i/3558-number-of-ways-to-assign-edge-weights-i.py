class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        from collections import deque

        q = deque([(1, 0)])  # (node, depth)
        visited = [False] * (n + 1)
        visited[1] = True

        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append((nei, depth + 1))

        return pow(2, max_depth - 1, self.MOD)