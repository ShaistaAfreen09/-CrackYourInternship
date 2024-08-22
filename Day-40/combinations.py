class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def findCombination(n, k, start, subset):
            if len(subset) == k:
                result.append(subset)
                return
            for i in range(start, n+1):
                findCombination(n, k, i+1, subset+[i])
        result = []
        findCombination(n, k, 1, [])
        return result