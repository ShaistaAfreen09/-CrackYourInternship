class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if nums[ abs(num) - 1 ] < 0:
                # Already Marked --> Repeated Guy
                ans.append(abs(num))

            else: # Not Marked
                nums[ abs(num) - 1 ] = - (nums[ abs(num) - 1 ])

        return ans