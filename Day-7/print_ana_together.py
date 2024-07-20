#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        lst1 = []
        dict = {}
        lst_2d = []
        for word in words:
            word = list(word)
            word.sort()
            word = ''.join(word)
            if word not in lst1:
                lst1.append(word)
                
                
        for word in words:
            temp = word
            word = list(word)
            word.sort()
            word = ''.join(word)
            if word not in dict:
                dict[word] = (temp,)
                
            else:
                dict[word] += (temp,)
                
        for key, values in dict.items():
            lst_2d.append(list(values))
            
        return lst_2d    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends