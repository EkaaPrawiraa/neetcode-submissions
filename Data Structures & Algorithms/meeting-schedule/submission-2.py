"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        current = intervals[0]
        for inter in intervals[1:]:
            if inter.start < current.end:
                return False
            else:
                current = inter

        return True
