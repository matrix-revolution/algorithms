class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = 1
        while num <= n:
            if n/num == 1 and n % num == 0:
                return True
            elif n/(num*2) == 1 and n % (num*2) == 0:
                return True
            num *= 2
        return False


def main():
    sol = Solution()
    n = 16
    out = sol.isPowerOfTwo(n)
    print out

if __name__ == '__main__':
    main()