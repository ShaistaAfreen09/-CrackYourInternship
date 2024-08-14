# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width=0
        a=deque([(root,0)])
        while a:
            res=[]
            for i in range(len(a)):
                node,num = a.popleft()
                res.append(num)
                if node.left:
                    a.append((node.left,num*2+1))
                if node.right:
                    a.append((node.right,num*2+2))
            max_width = max(max_width,res[-1] - res[0] + 1)
        return max_width
        