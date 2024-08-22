class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        inn = sorted(intervals, key=lambda x: x[0], reverse=True)
        ans = [inn[0]]
        for s, e in inn[1:]:
            if ans[-1][0] >= e: 
                ans.append([s, e])
            else: 
                count += 1
        return count