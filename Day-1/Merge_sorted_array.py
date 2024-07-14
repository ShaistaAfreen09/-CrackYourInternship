# The question mainly asks about to two lists nums1 and nums2 are given and we need to sum them in such a way that both together form a single list with nums1 only , here nums1 has length of m+n where m is valid values and n is 0's and length of nums2 is n .

#approach :  we will firstly iterate from the m to nums1 whole and then pop the n values from it as we are iterating from m it won't take n (0's) followed by adding the first and the second list nums2 and then sort them .
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.nums1=a nums2=b maxpoi=m,min=n
        """
        for element in range(m,len(nums1)):
            nums1.pop()
        nums1 += nums2
        nums1.sort()


