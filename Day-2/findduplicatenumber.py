class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] = hashmap[i] + 1
        for key,value in hashmap.items():
            if value != 1:
                return key
        