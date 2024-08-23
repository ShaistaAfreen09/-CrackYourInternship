class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        land_count = 0
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    land_count += 1
                    queue.append((i, j, 0))
        if land_count == n * n or not queue:
            return -1
        for i, j, dist in queue:
            for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append((x, y, dist + 1))
        return queue[-1][2]
