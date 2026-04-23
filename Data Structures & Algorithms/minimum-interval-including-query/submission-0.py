class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = [-1] * len(queries)
        for x, q in enumerate(queries):
            for i in intervals:
                length = 0
                if i[0] <= q <= i[1]:
                    length = i[1] - i[0] + 1
                    res[x] = min(length,res[x] if res[x] != -1 else float("inf"))
        return res