class Solution:
    def convertToTitle(self,x):
        result = []
        while x > 0:
            result.append(string.ascii_uppercase[(x - 1) % 26])
            x = (x - 1) // 26
        return "".join(reversed(result))