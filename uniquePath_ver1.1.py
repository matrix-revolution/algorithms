
class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # move right
        # move down

        start_point = 0
        end_point = m * n - 1
        grid = []
        for i in range(0, m):
            for j in range(0, n):
                grid.append(i)

        store = [0 for k in range(0, m*n)]

        for i in range(start_point, end_point+1):
            if i == start_point:
                store[i] = 1
            else:
                # move right
                if grid[i] == grid[i - 1]:
                    store[i] += store[i - 1]

                # move down
                if 0 <= i - n <= end_point:
                    store[i] += store[i - n]

        return store[end_point]


def main():
    sol = Solution()
    m = 8
    n = 8
    out = sol.uniquePaths(m, n)
    print(out)

if __name__ == '__main__':
    main()