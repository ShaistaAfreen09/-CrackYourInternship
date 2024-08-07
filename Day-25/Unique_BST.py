# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
         return self.rec(list(range(1, n+1)))
    
    def rec(self, nums): #rec is used as helper function here
        return [TreeNode(val=nums[i], left=left, right=right)
                for i in range(len(nums))
                for left in self.rec(nums[:i])
                for right in self.rec(nums[i+1:])] or [None]
        