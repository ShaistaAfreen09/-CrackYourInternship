#binary search
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)     
        while low < high:
            mid = (low + high) // 2
            current_sum = 0
            count = 1          
            for num in nums:
                if current_sum + num > mid:
                    current_sum = num
                    count += 1
                else:
                    current_sum += num    
            if count > k:
                low = mid + 1
            else:
                high = mid 
        return low
