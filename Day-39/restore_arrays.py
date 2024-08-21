class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in adjacentPairs:
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)
        result = []
        visited = set()
        start = next(node for node in graph if len(graph[node]) == 1)
        stack = [start]
        while stack:
            current = stack.pop()
            result.append(current)
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return result
