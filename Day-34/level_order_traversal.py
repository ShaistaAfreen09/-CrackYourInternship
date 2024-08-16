# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([(root, 0)])  

        while queue:
            node, level = queue.popleft()

            if node is None:  
                continue

            if len(res) == level:
                res.append([])

            res[level].append(node.val) 
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return res
