class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        lastFound = intervals[0]
        for [start, end] in intervals[1:]:
            last = lastFound[1]
            if start <= last:
                lastFound[1] = max(lastFound[1], end)
            else:
                res.append(lastFound[:])
                lastFound=[start,end]
        res.append(lastFound)
        return res
