"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) <= 1:
            return len(intervals)
        
        intervals.sort(key = lambda i:i.start)

        visited = set()
        ret = 0

        for i in range(len(intervals)):
            if i in visited:
                continue
            else:
                visited.add(i)
                ret += 1
                r = intervals[i].end
            for j in range(i + 1, len(intervals)):
                if j in visited:
                    continue
                if intervals[j].start >= r:
                    visited.add(j)
                    r = intervals[j].end

        return ret