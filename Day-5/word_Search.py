# we have been given a board of characters and a word, we need to check whether the word exist init or not , same letter cell may nti be used more than once
# Approach : firslty determine size of board foloowed by creating a set which contains visited cells then we can define our function and start the search from starting to thei th charcater and if our i matches length of words i.e we found the word then return true and if so doesn't happen and we come acroos the situation where our cells are outside board or it's already visited then return false and ass to visited now we need to see our other possible directions where the word can exist be it top , bottom , left and right and if we found the same word again store in ans and then after exploring all we remove current from visited and set it to be used by other paths and return the function which was created using our result



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        visited = set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            
            if r<0 or r==m or c<0 or c==n or (r,c) in visited or board[r][c]!=word[i]:
                return False

            visited.add((r,c))
            ans = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            visited.remove((r,c))
            return ans

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True

        return False