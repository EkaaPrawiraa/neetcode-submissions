class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        current = intervals[0][1]

        for [start, end] in intervals[1:]:
            if current <= start:
                current = end
            else:
                res+=1
                current = min(end,current)
        return res