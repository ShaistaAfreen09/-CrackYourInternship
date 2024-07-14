# The question states that we need to find the nums contains values in which on adding two values we should get the target value .
# approach : so we can solve in a way that firslty we initailize an empty dictionary which would store key and indices of the values followed by iteration of list nums from iand n as i represents the index of current element and n is the value of current element then we we store value of target that is present in list in the diff  variable which we need to meet and check if the value already exist in prev dict if so then return the index of the two numbers or else add the index of current number to the prev. 
class Solution:
    def twoSum(sel, nums: List[int] , target:int) -> List[int]:
        prev= {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff] , i]
            prev[n] = i