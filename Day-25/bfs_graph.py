#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visit=set()
        queue = [0]
        path = []
        while queue:
            s = queue.pop(0)
            if s not in visit:
                visit.add(s)
                path.append(s)
            neigh = adj[s]
            for n in neigh:
                if n not in visit:
                    queue.append(n)
        return path

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
print()
        

# } Driver Code Ends