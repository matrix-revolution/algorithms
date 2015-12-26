class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        len_matrix = len(matrix)
        chosen_matrix = -1
        flag = False

        for i in range(0, len_matrix):
            len_inner = len(matrix[i])
            if matrix[i][len_inner-1] > target:
                chosen_matrix = i
                break
            elif matrix[i][len_inner-1] == target:
                return True
        if chosen_matrix == -1:
            return False
        search_list = matrix[chosen_matrix]
        low = 0
        high = len(search_list)-1
        while low < high:
            mid = int((low+high)/2)
            if mid == low:
                if target == search_list[low] or target == search_list[high]:
                    return True
                else:
                    return False
            if target < search_list[mid]:
                high = mid
            elif target > search_list[mid]:
                low = mid
            elif target == search_list[mid]:
                return True
        return False


def main():
    sol = Solution()
    # matrix = [[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
    matrix = [[1]]
    target = 1
    out = sol.searchMatrix(matrix, target)
    print out

if __name__ == '__main__':
    main()