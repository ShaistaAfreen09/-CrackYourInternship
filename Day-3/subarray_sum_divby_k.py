# question states that we need to find the subarrays which sum divisible by k where k is integer and sums is an array.
# we can solve using finding the subarrays in a given list have sums that are divisible by k, it does this is by using total prefix , which keeps track of sum of numbers as we go throughh list.(not completly explained)

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        prefix = 0
        n = len(nums)
        mod_seen = defaultdict(int)
        mod_seen[0] = 1
        for i in range(n):
            prefix = (prefix+nums[i]) % k
            mod_seen[prefix] += 1
            res += (mod_seen[prefix] - 1)
        return res
        