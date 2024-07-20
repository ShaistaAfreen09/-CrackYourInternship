class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()[::-1]
        res=''
        for word in words:
            res += word+' '
        return res[:-1]