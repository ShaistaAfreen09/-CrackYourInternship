#User function Template for python3
from collections import deque
class Solution:
    def isPossible(self,N,P,prerequisites):
        #code here
        indeg = [0]*N
        adj = [[] for i in range(N)]
        for (src, dest) in prerequisites:
            adj[src].append(dest)
            indeg[dest] += 1
        
        q = deque([]) 
        for node in range(N):
            if indeg[node]==0:
                q.append(node)
 
        while q:
            node = q.popleft()
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
       
       
        for i in range(N):
            if indeg[i] != 0:
                return False
        return True
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends