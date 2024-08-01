'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        count = 0
        res=0
        i=-1
        pet = 0
        dis = 0
        for i in range(len(lis)):
            pet +=lis[i][0]
            dis +=lis[i][1]
        if dis>pet:
            return -1
        while count<n:
            i = i+1
            i = i%n
            res =res+lis[i][0]-lis[i][1]
            count+=1
            if res<0:
                count=0
                res=0
        return (i+1)%n


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends