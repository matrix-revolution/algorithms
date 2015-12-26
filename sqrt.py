import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = math.log(x, 2)
        y = a/2
        while y < a:
            val = pow(2, y)
            out = int(val)*int(val)
            if out <= x:
                return int(val)
            y += 1


def main():
    sol = Solution()
    x = 16
    out = sol.mySqrt(x)
    print out

if __name__ == '__main__':
    main()