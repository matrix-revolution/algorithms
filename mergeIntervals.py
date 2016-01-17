# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda interval: interval.start)
        output = []
        i = 0
        prev_interval = None

        if len(intervals) <= 1:
            return intervals

        while i < len(intervals) - 1:
            if prev_interval is None:
                first = intervals[i]
            else:
                first = output.pop()
            second = intervals[i + 1]
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

            i += 1
        return output




def main():
    sol = Solution()
    # [[2,3],[4,5],[6,7],[8,9],[1,10]]
    interval_1 = Interval(2, 3)
    interval_2 = Interval(4, 5)
    interval_3 = Interval(6, 7)
    interval_4 = Interval(8, 9)
    interval_5 = Interval(1, 10)
    intervals = [interval_1, interval_2, interval_3, interval_4, interval_5]
    out = sol.merge(intervals)
    for i in range(0, len(out)):
        val = out[i]
        print 'start : %d and end: %d' % (val.start, val.end)


if __name__ == '__main__':
    main()