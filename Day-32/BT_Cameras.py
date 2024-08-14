# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.minCameras = 0
        
    def cameras(self,root, minCameras):
        if root == None:
            return "ok"
        
        left = self.cameras(root.left, minCameras)
        right = self.cameras(root.right, minCameras)
        
        if left == "want" or right == "want":
            self.minCameras += 1
            return "provide"
        
        elif left == "provide" or right == "provide":
            return "ok"
        
        else:
            return "want"
        
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if self.cameras(root, self.minCameras) == "want":
            self.minCameras += 1
        return self.minCameras