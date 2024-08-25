class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        result=0
        for i,a in enumerate(heights):
                start = i
                while stack and stack[-1][1] >= a:
                    index,h = stack.pop()
                    start = index
                    result = max(result,(i-index)*h)
                stack.append((start,a))
        for i , a in stack:
            result = max(result,(len(heights)-i)*a)
        return result


        