class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        val_store = [0 for i in range(0, n+1)]
        for k in range(0, n+1):
            if k == 0 or k == 1:
                val_store[k] = 1
            else:
                val_store[k] = val_store[k-1] + val_store[k-2]
        return val_store[n]


def main():
    sol = Solution()
    n = 5
    out = sol.climbStairs(n)
    print out

if __name__ == '__main__':
    main()