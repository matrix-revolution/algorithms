class Solution(object):

    def move_right(self, row_idx, start_col, end_col, matrix):
        a = [0 for i in range(start_col, end_col)]
        j = 0
        for i in range(start_col, end_col):
            a[j] = matrix[row_idx][i]
            j += 1
        return a

    def move_left(self, row_idx, start_col, end_col, matrix):
        a = [0 for i in range(start_col-1, end_col, -1)]
        j = 0
        for i in range(start_col-1, end_col, -1):
            a[j] = matrix[row_idx][i]
            j += 1
        return a

    def move_down(self, col_idx, start_row, end_row, matrix):
        a = [0 for i in range(start_row, end_row+1)]
        j = 0
        for i in range(start_row, end_row+1):
            a[j] = matrix[i][col_idx]
            j += 1
        return a

    def move_up(self, col_idx, start_row, end_row, matrix):
        a = [0 for i in range(start_row, end_row, -1)]
        j = 0
        for i in range(start_row, end_row, -1):
            a[j] = matrix[i][col_idx]
            j += 1
        return a

    def construct_result(self, output, steps_right, steps_down, steps_left, steps_up):

        for num in steps_right:
            output.append(num)

        for num in steps_down:
            output.append(num)

        for num in steps_left:
            output.append(num)

        for num in steps_up:
            output.append(num)

        print output

        return output

    def spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        print rows
        print cols

        start_row = 0
        start_col = 0
        end_row = rows - 1
        end_col = cols - 1

        steps_right = []
        steps_left = []
        steps_up = []
        steps_down = []

        output = list[int]
        len_out = len(output)
        len_matrix = rows*cols

        while len_out < len_matrix:
            for row_idx in range(start_row, rows):
                if row_idx == start_row:
                    steps_right = self.move_right(row_idx, start_col, end_col,  matrix)
                if row_idx == end_row:
                    steps_left = self.move_left(row_idx, end_col, start_col, matrix)
            for col_idx in range(start_col, cols):
                if col_idx == start_col:
                    steps_up = self.move_up(col_idx, end_row, start_row, matrix)
                if col_idx == end_col:
                    steps_down = self.move_down(col_idx, start_row, end_row, matrix)
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1

            output = self.construct_result(output, steps_right, steps_down, steps_left, steps_up)
            len_out = len(output)

        return output


def main():

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    new_obj = Solution()
    output = new_obj.spiral_order(matrix)
    print output

if __name__ == '__main__':
    main()