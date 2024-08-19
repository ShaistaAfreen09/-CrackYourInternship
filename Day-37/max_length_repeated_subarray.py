class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        A= len(nums1)
        B= len(nums2)
        dp=[[0 for x in range(B+1)] for x in range(A+1)]
        res = 0
        for i in range(1,A+1):
            for j in range(1,B+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res,dp[i][j])
        return res
        