#The question states that we need to find min diff between the maximum and minimum elements of subarray of size M and the given array A of size N. 
# Approach : firstly sort the array to make it easier to find diff and iititalize the minimum dfference to the possible value use the two pointer to check subarray of size M and update to min diff and return the smallest diff found 

#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        mi=max(A)
        i=0
        j=i+M-1
        while j<N:
            mi=min(mi,A[j] -A[i])
            i=i+1
            j=j+1
        return mi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends