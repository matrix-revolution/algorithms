# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        new_list = []
        output = []
        len_intervals = len(intervals)
        i = 0
        if len(intervals) <= 0 and newInterval is not None:
            output.append(newInterval)
            return output

        while i < len_intervals:
            val = intervals[i]
            if newInterval.start < val.start:
                new_list.append(newInterval)
                new_list.append(val)
                break
            else:
                new_list.append(val)
            i += 1
        if i < len_intervals:
            i += 1
            while i < len_intervals:
                new_list.append(intervals[i])
                i += 1
        else:
            new_list.append(newInterval)

        # merge
        k = 0
        prev_interval = None
        intervals = new_list
        if len(intervals) <= 1:
            return intervals
        while k < len(intervals) - 1:
            if prev_interval is None:
                first = intervals[k]
            else:
                first = output.pop()
            second = intervals[k + 1]
            new_interval = Interval(0, 0)
            if first.start <= second.start <= first.end:
                new_interval.start = first.start
                if first.end <= second.end:
                    new_interval.end = second.end
                else:
                    new_interval.end = first.end
                output.append(new_interval)
                prev_interval = new_interval
            else:
                output.append(first)
                output.append(second)
                prev_interval = second

            k += 1
        return output


def main():
    sol = Solution()
    # [1,2],[3,5],[6,7],[8,10],[12,16]
    interval_1 = Interval(1, 2)
    interval_2 = Interval(3, 5)
    interval_3 = Interval(6, 7)
    interval_4 = Interval(8, 10)
    interval_5 = Interval(12, 16)
    intervals = [interval_1, interval_2, interval_3, interval_4, interval_5]
    new_interval = Interval(4, 9)
    out = sol.insert(intervals, new_interval)
    for i in range(0, len(out)):
        val = out[i]
        print 'start : %d and end: %d' % (val.start, val.end)

if __name__ == '__main__':
    main()