class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        curr_max = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "0":
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1 + min((dp[i - 1][j]), dp[i - 1][j - 1], dp[i][j - 1])
                curr_max = max(curr_max, dp[i][j])
        return curr_max * curr_max