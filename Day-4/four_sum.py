# question states that we need find the array which meets the target and return the array.
#Approach : in this mainly firslty we will store length of nums in a variable named n and further sort the array and then staore an empty array which mainly represents our target in temp variable . then we will iterate over n and 
# and check if our current value meets the i and continue further same goes with j but j will be the second most value from i and the length of l 
# now we will continue k will be next value of j and l will be total length of n which is the last value mainly then followed by values of i,j,k and l summation would be done and store in a variable named current,
#now check the condition that current_sum meets target and then store it in a value and append to temp and store the array meeting.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        temp = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
               
                k, l = j + 1, n - 1
                while k < l:
                    current_sum = nums[i] + nums[j] + nums[k] + nums[l]
                   
                    if current_sum == target:
                        ans = [nums[i], nums[j], nums[k], nums[l]]
                        temp.append(ans)
                       
                        k += 1
                        l -= 1
                        
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    
                    elif current_sum < target:
                        k += 1
                    
                    else:
                        l -= 1
        
        
        return temp
