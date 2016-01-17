class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_store = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(0, cols):
            for j in range(0, rows):
                if matrix[j][i] == 0:
                    row_store.append(j)
                    for k in range(0, rows):
                        if matrix[k][i] == 0 and k != j:
                            row_store.append(k)
                        matrix[k][i] = 0
                break
        for ele in row_store:
            for j in range(0, cols):
                matrix[ele][j] = 0


def main():
    sol = Solution()
    matrix = [[1], [0]]
    sol.setZeroes(matrix)
    print(matrix)

if __name__ == '__main__':
    main()