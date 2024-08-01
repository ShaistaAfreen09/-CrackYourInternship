class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['$',0]]
        for a in s:
            if stack[-1][0] == a:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([a,1])
        return ''.join(a * cnt for a,cnt in stack)
        