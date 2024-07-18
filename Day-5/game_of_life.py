class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowlength= len(board[0])
        collength= len(board)

        ans = [[-1 for x in range(rowlength)] for y in range(collength)]
        def inBound(i,j):
            return (0<=i<collength) and (0<=j<rowlength)

        for i in range(collength):
            for j in range(rowlength):
                count = 0
                for ii,jj in [(i,j+1),(i,j-1),(i-1,j),(i+1,j),(i-1,j+1),(i+1,j-1),(i+1,j+1),(i-1,j-1)]:
                    if inBound(ii,jj):
                        count += board[ii][jj]
                if count < 2:
                    ans[i][j] = 0
                elif board[i][j] == 1 and (count == 2 or count==3):
                    ans[i][j] = 1
                elif board[i][j] == 1 and count > 3:
                    ans[i][j] = 0
                elif board[i][j] == 0 and count == 3:
                    ans[i][j] = 1
                else:
                    ans[i][j] = board[i][j]
        board[:] = ans
        return board