import Queue


class Solution(object):

    def call_bfs(self, m, n, grid, store):
        paths = 0
        len_grid = len(grid)
        while not store.empty():
            curr_ele = store.get()

            # move right
            if curr_ele + 1 < len_grid and grid[curr_ele + 1] == grid[curr_ele]:
                right_val = curr_ele + 1
                if right_val == len_grid - 1:
                    paths += 1
                else:
                    store.put(right_val)

            # move down
            if (curr_ele + n) < len_grid:
                down_val = curr_ele + n
                if down_val == len_grid - 1:
                    paths += 1
                else:
                    store.put(down_val)
        return paths

    def construct_grid(self, m, n):
        grid = []
        for i in range(0, m):
            for j in range(0, n):
                curr_pos = n * i + j
                grid.append(i)

        return grid

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # move right
        # move down

        len_path = m * n
        marked_path = [0 for i in range(0, len_path)]

        store = Queue.Queue()
        rows = m
        cols = n
        row_idx = 0
        col_idx = 0

        grid = self.construct_grid(rows, cols)
        store.put(grid[0])
        paths = self.call_bfs(m, n, grid, store)

        return paths

def main():
    sol = Solution()
    m = 8
    n = 8
    out = sol.uniquePaths(m, n)
    print(out)

if __name__ == '__main__':
    main()