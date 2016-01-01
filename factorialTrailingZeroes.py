class Solution(object):
    def factorial(self, n, val_store):
        if len(val_store) <= 0:
            val_store.append(0)
        if n == 0:
            return val_store[n]
        if n == 1:
            val_store.append(1)
            return val_store[n]
        return n * self.factorial(n-1, val_store)

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        val_store = []
        fact = self.factorial(n, val_store)
        return fact
        """
        count = 0
        while n/5 >= 1:
            count += n/5
            n /= 5
        return count


def main():
    sol = Solution()
    n = 125
    out = sol.trailingZeroes(n)
    print(out)

if __name__ == '__main__':
    main()