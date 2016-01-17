class Solution(object):
    def call_power(self, x, n):

        if n == 0:
            return 1
        store = self.call_power(x, n/2)
        val = store * store
        if n % 2 != 0:
            val *= x
        return val

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            out = self.call_power(x, -n)
            return 1/out
        else:
            return self.call_power(x, n)


def main():
    sol = Solution()
    x = 2
    n = 12
    out = sol.myPow(x, n)
    print(out)

if __name__ == '__main__':
    main()