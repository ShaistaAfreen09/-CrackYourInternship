class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj=[[] for i in range(n)]
        for i in range(n):
            if manager[i]!=-1:
                adj[manager[i]].append(i)
        counts = []
        stack = [[headID,0]]
        maxcount = 0
        while stack:
            node = stack.pop()
            manager = node[0]
            count = node[1]   
            for employee in adj[manager]:
                stack.append([employee, count + informTime[node[0]]])
                maxcount = max(maxcount, count + informTime[node[0]])    
        return maxcount
        