class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        kmod = 10**9+7
        dp={-1:0}
        stack = [-1]
        for i in range(n):
            while stack != [-1] and arr[i] <= arr[stack[-1]]:
                stack.pop()
            last = stack[-1]
            dp[i] = dp[last] + (i - last) * arr[i]
            stack += [i]
        return sum(dp.values()) % kmod
