# Question : we have two arrays, nums1 and nums2, where nums1 is a subset of nums2. For each element in nums1, we need to find the first greater element that appears to the right of it in nums2. If no such element exists, the result for that element should be -1.
#Appraoch : we will use hashmap concept as it will be easy to define the index places of each value and then we can create a empty stack and suppose our first list as -1(no element is greater here) followed by iterating in nums2 and then if update the values to stack if we get less value in nums2 then we will append it with the value or else pop the given value if the next value is greater and in end return the res var with the list of updated greter elements.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Hashmap = {n: i for i,n in enumerate(nums1)}
        res= [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and stack[-1] <num:
                smaller_num = stack.pop()
                if smaller_num in Hashmap:
                    res[Hashmap[smaller_num]] = num
            stack.append(num)
        return res
        