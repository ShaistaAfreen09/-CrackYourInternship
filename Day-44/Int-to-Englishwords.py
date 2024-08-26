class Solution:
    def numberToWords(self, num: int) -> str:
        tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands=["","Thousand","Million","Billion","Trillion"]
        one_till_20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
        "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

        if num==0:
            return "Zero"
        def helper_fun(n):
            if n==0:
                return ""
            elif n<20:
                return one_till_20[n] + " "
            elif n < 100:
                return tens[n//10] + " " + helper_fun(n%10)
            else:
                return one_till_20[n //100] + " Hundred " + helper_fun(n%100)
        result=""
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                result = helper_fun(num % 1000) + unit + " " + result
            num //= 1000
        return result.strip()