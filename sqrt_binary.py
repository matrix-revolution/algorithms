
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        if x == 0:
            return 0
        if x == 1:
            return 1
        while low < high:
            mid = int((low+high)/2)
            val = mid * mid
            lower_bound = val
            upper_bound = (mid+1) * (mid+1)
            if lower_bound <= x < upper_bound:
                return mid
            if val > x:
                high = mid
            elif val < x:
                low = mid


def main():
    sol = Solution()
    x = 99
    out = sol.mySqrt(x)
    print out


if __name__ == '__main__':
    main()