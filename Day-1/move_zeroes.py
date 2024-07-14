# The question states that a list iss given and we nee to move all the zeroes to end in the list and return it
#Appproach : firstly we will define a variable with value zero which would mainly be used to track the value of non zero elements and then iterate to each index of nums followed by a condition check that if the value in num while iteration is not equal to zero the swap the values of non zero indexs values then the non zero elements moves to k place and is incremented to next non zero elements .

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[k] = nums[k],nums[i]
                k += 1