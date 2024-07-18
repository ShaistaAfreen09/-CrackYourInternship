# the question states that i need to find unique permutations existing in the array and donot include the repeated one's.
# we ca use python module called itertools from which we can import permutations followed by sorting the set on which we might have applied to permutation function to find the arrangement so that it gives us uique values in sorted order and converts the created set back to list and then the driver code runs.

#User function Template for python3
from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        uniq = list(sorted(set(permutations(arr))))
        return uniq


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends