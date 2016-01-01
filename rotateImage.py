class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = rows
        itr = int(rows/2)
        k = 0
        s_row = 0
        s_col = 0
        e_row = rows - 1
        e_col = cols - 1
        c = 0
        c_e = e_col
        r_e = e_row
        r = 0
        while k < itr:
            m = 0
            while m < cols-1:
                temp = matrix[r][e_col]
                while temp is not None:
                    matrix[r][e_col] = matrix[s_row][c]
                    new_temp = matrix[e_row][c_e]
                    matrix[e_row][c_e] = temp
                    temp = new_temp
                    new_temp = matrix[r_e][s_col]
                    matrix[r_e][s_col] = temp
                    temp = new_temp
                    matrix[s_row][c] = temp
                    temp = None
                m += 1
                c += 1
                r += 1
                c_e = e_col - c
                r_e = e_row - r
            k += 1
            s_row = s_row + k
            s_col = s_col + k
            e_row = e_row - k
            e_col = e_col - k
            cols = e_col - s_col + 1
            c = s_col
            r = s_row
            c_e = e_col
            r_e = e_row


def main():
    sol = Solution()
    #matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    #matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    sol.rotate(matrix)
    print(matrix)

if __name__ == '__main__':
    main()