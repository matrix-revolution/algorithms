class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(0, len(matrix)):
            inner_matrix = matrix[i]
            len_inner = len(inner_matrix)
            low = 0
            high = len_inner-1

            if target == inner_matrix[low] or target == inner_matrix[high]:
                return True
            while low < high:
                mid = int((low+high)/2)
                if inner_matrix[mid] == target:
                    return True
                if low == mid:
                    if inner_matrix[low] == target or inner_matrix[high] == target:
                        return True
                    else:
                        break
                elif inner_matrix[mid] > target:
                    high = mid
                elif inner_matrix[mid] < target:
                    low = mid
                else:
                    break
        return False


def main():
    sol = Solution()
    matrix = [[1,   4,  7, 11, 15], [2, 5,  8, 12, 19], [3, 6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 29
    out = sol.searchMatrix(matrix, target)
    print out

if __name__ == '__main__':
    main()
