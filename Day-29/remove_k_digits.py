class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        
        stack = deque() 
        for digit_char in num:
            while k > 0 and stack and stack[-1] > digit_char:
                stack.pop()
                k -= 1
            stack.append(digit_char)

        while k > 0:
            stack.pop()
            k -= 1

        return "".join(stack).lstrip('0') or "0"
        