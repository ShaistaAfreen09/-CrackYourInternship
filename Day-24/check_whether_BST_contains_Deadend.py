# Your task is to complete this function
# function should return true/false or 1/0
from collections import deque
class Solution:
    def isDeadEnd(self, root):
        # Code here
        queue = deque()
        queue.append(root)
        
        visited_nodes,leaf_nodes = set(),set()
        while queue:
            current_node = queue.popleft()
            visited_nodes.add(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            if not current_node.left and not current_node.right:
                leaf_nodes.add(current_node.data)
        for leaf in leaf_nodes:
            if (leaf == 1 and 2 in visited_nodes) or (leaf - 1 in visited_nodes and leaf + 1 in visited_nodes):
                return 1
        return 0
            


#{ 
 # Driver Code Starts

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
                
        ob = Solution()
        if ob.isDeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends