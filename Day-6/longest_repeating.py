class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minindex = min(strs)
        maxindex=max(strs)
        k=""
        for i in range(len(minindex)):
            if (minindex[i] == maxindex[i]):
                k+=minindex[i]
            else:
                break
        return k
        