# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 0:
            return 0

        if len(points) == 1:
            return 1

        len_points = len(points)
        store = {}
        max_slope = 0
        max_no = 0
        for i in range(0, len_points):
            temp = {}
            point1 = points[i]
            max_slope = 0
            max_no = 0
            for j in range(i+1, len_points):
                point2 = points[j]
                if point2.x - point1.x == 0:
                    slope = 0
                else:
                    slope = (point2.y - point1.y) / (point2.x - point1.x)
                if slope not in temp:
                    temp[slope] = 1
                    if temp[slope] > max_no:
                        max_no = temp[slope]
                        max_slope = slope
                else:
                    temp[slope] += 1
                    if temp[slope] > max_no:
                        max_no = temp[slope]
                        max_slope = slope
            if max_slope not in store:
                store[max_slope] = max_no
            else:
                store[max_slope] += max_no

        max_val = 0
        for k in store:
            if store[k] > max_val:
                max_val = store[k]
        return max_val+1


def main():
    sol = Solution()
    point1 = Point(0, 0)
    #point2 = Point(0, 0)
    point3 = Point(-1, -1)
    point4 = Point(2, 2)
    #points = [point1, point2]
    points = [point1, point3, point4]
    out = sol.maxPoints(points)
    print(out)

if __name__ == '__main__':
    main()