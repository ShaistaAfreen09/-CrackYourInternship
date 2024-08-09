#User function Template for python3
from typing import List

class Solution:
    
    
    def isCyclic(self, V, adj):
        # code here
        vist = [0]* V
        path = [0]* V
        
        for i in range(V):
            if not vist[i]:
                if self.dfs(i, adj, vist, path):
                    return True
        return False
            

    def dfs(self, node, adj, vist, path):
        vist[node] = 1
        path[node] = 1
        
        for i in adj[node]:
          
            if not vist[i]:
                if self.dfs(i , adj, vist, path):
                    return True
            
            elif path[i]:
                return True
        
        path[node] = 0
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends