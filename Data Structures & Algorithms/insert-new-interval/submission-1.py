class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        intervals.sort()
        firstEnd = intervals[0]
        for [start, end] in intervals[1:]:
            last = firstEnd[1]
            if last >= start:
                if last < end:
                    firstEnd[1] = end
            else:
                res.append(firstEnd[:])
                firstEnd=[start,end]
        res.append(firstEnd[:])
        print(res)
             


        return res
        