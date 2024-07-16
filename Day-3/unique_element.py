# question states that we need to find the most unique value from the given error firslty remove the repeating one's then make he another array iwthout spaces and then return the length of array. (lenght of new error needs to be returned is main part of question)
# Approach : we can solve it in this way convert he array into set so that it doesn't contain repeating values then apply sort folloowed by slicing of values and then return the length of nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
