class Solution(object):

    def call_dfs(self, grid, rows, cols, row_idx, col_idx, len_grid, marked_island, count):

        curr_pos = cols * row_idx + col_idx

        if curr_pos > len_grid or row_idx < 0 or col_idx >= cols:
            return
        #print(curr_pos)
        #print 'row_idx %d and col_idx %d' % (row_idx, col_idx)

        if grid[row_idx][col_idx] == 1 and marked_island[curr_pos] == 0:
            marked_island[curr_pos] += 1
        else:
            return

        # move right
        self.call_dfs(grid, rows, cols, row_idx, col_idx + 1, len_grid, marked_island, count)

        # move left
        self.call_dfs(grid, rows, cols, row_idx, col_idx - 1, len_grid, marked_island, count)

        # move up
        self.call_dfs(grid, rows, cols, row_idx - 1, col_idx, len_grid, marked_island, count)

        # move down
        self.call_dfs(grid, rows, cols, row_idx + 1, col_idx, len_grid, marked_island, count)

        return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # move left
        # move right
        # move down
        # move up

        rows = len(grid)
        cols = len(grid[0])
        len_grid = rows * cols

        # list of marked island
        marked_island = [0 for i in range(0, len_grid)]
        count = 0
        curr_pos = 0

        for i in range(0, rows):
            for j in range(0, cols):
                curr_pos = cols * i + j
                if grid[i][j] != 0 and marked_island[curr_pos] != 1:
                    self.call_dfs(grid, rows, cols, i, j, len_grid, marked_island, count)
                    count += 1
        return count


def main():
    sol = Solution()
    """
    grid = [[1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    """
    """
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]]
    """

    out = sol.numIslands(grid)
    print(out)

if __name__ == '__main__':
    main()