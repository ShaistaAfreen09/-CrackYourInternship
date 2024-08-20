class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n
        index2 = index3 = index5 = 0
        ugly_numbers[0] = 1
        
        for i in range(1, n):
            next_ugly = min(ugly_numbers[index2] * 2, ugly_numbers[index3] * 3, ugly_numbers[index5] * 5)
            ugly_numbers[i] = next_ugly
            
            if next_ugly == ugly_numbers[index2] * 2:
                index2 += 1
            if next_ugly == ugly_numbers[index3] * 3:
                index3 += 1
            if next_ugly == ugly_numbers[index5] * 5:
                index5 += 1
                
        return ugly_numbers[n - 1]
