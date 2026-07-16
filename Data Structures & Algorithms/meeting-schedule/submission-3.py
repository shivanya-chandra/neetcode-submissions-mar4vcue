"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        # intervals.sort(key=lambda interval: interval[0])
        if not intervals:
            return True
        l = intervals[0].end

        for i in range(1,len(intervals)):
            if l > intervals[i].start:
                return False
            l = intervals[i].end

        return True
