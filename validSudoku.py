class Solution(object):
    def is_row_valid(self, n_rows, m_cols, row_idx, board):
        row_valid = True
        valid_store = [0 for i in range(0, 10)]
        for col in range(0, m_cols):
            val = board[row_idx][col]
            if val != '.':
                int_val = int(val)
                valid_store[int_val-1] += 1
                if valid_store[int_val - 1] > 1:
                    return False
        return row_valid

    def is_col_valid(self, n_rows, m_cols, col_idx, board):
        col_valid = True
        valid_store = [0 for j in range(0, 10)]
        for row in range(0, n_rows):
            val = board[row][col_idx]
            if val != '.':
                int_val = int(val)
                valid_store[int_val - 1] += 1
                if valid_store[int_val - 1] > 1:
                    return False
        return col_valid

    def is_square_valid(self, start_row, start_col, end_row, end_col, board):
        square_valid = True
        valid_store = [0 for k in range(0, 10)]
        for row in range(start_row, end_row+1):
            for col in range(start_col, end_col+1):
                val = board[row][col]
                if val != '.':
                    int_val = int(val)
                    valid_store[int_val - 1] += 1
                    if valid_store[int_val - 1] > 1:
                        return False
        return square_valid

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) <= 0:
            return True
        n_rows = len(board)
        m_cols = len(board[0])
        row_idx = 0
        col_idx = 0
        row_valid = True
        col_valid = True
        square_valid = True
        output = True

        for i in range(row_idx, n_rows):
            row_valid = row_valid and self.is_row_valid(n_rows, m_cols, i, board)
            if not row_valid:
                return False

        for j in range(col_idx, m_cols):
            col_valid = col_valid and self.is_col_valid(n_rows, m_cols, j, board)
            if not col_valid:
                return False

        start_row = 0
        end_row = 2
        start_col = 0
        end_col = 2
        while end_row < n_rows:
            start_col = 0
            end_col = 2
            while end_col < m_cols:
                square_valid = square_valid and self.is_square_valid(start_row, start_col, end_row, end_col, board)
                if not square_valid:
                    return False
                start_col += 3
                end_col += 3
            start_row += 3
            end_row += 3

        return output


def main():
    sol = Solution()
    """board = [['5', '3', '.', '.', '7', '.', '.', '.', '6'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    """
    board = [['.', '.', '.', '.', '.', '.', '5', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['9', '3', '.', '.', '2', '.', '4', '.', '.'],
             ['.', '.', '7', '.', '.', '.', '3', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '3', '4', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '3', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '5', '2', '.', '.']]
    output = sol.isValidSudoku(board)
    print(output)

if __name__ == '__main__':
    main()