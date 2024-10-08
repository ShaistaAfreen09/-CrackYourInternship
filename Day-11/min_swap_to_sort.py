

class Solution:
     def minSwaps(self, nums):
        v=[(nums[i],i) for i in range(len(nums))]
        v.sort()
        cnt=0
        i=0
        while i<len(nums):
            num, index= v[i]
            if i!=index:
                cnt+=1
                v[i],v[index]=v[index],v[i]
                i-=1
            i+=1
        return cnt




#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends