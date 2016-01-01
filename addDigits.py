class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum_v = 0
        sum_v += num % 10
        num /= 10
        while num > 0:
            sum_v += num % 10
            num /= 10
            if num <= 0 and sum_v > 9:
                num = sum_v
                sum_v = 0
        return sum_v


def main():
    sol = Solution()
    num = 391
    out = sol.addDigits(num)
    print out

if __name__ == '__main__':
    main()