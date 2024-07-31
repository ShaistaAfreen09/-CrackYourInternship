class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        res = 0
        
        for value in arr:
            while stack and stack[-1] <= value:
                mid = stack.pop()
                if stack:
                    res += mid * min(stack[-1], value)
                else:
                    res += mid * value
            stack.append(value)
        
        while len(stack) > 1:
            res += stack.pop() * stack[-1]
        
        return res
        