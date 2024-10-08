#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        q=[]
        visited=[-1]*V
        distance=0
        heapq.heappush(q,(0,0)) #distance,node
        
        while q:
            dist,node=heapq.heappop(q)
            if visited[node]!=-1:
                continue
            visited[node]=1
            distance+=dist
            for neighbor,wt in adj[node]:
                if visited[neighbor]==-1:
                    heapq.heappush(q,(wt,neighbor))
                else:
                    continue
        return distance


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends
