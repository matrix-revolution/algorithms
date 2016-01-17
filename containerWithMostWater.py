class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_height = len(height)
        if len_height <= 0:
            return 0
        left_pointer = 0
        right_pointer = len_height - 1
        max_area = 0
        while left_pointer < right_pointer:
            if height[left_pointer] > height[right_pointer]:
                h = height[right_pointer]
                b = right_pointer - left_pointer
                area = h*b
                right_pointer -= 1
            elif height[left_pointer] <= height[right_pointer]:
                h = height[left_pointer]
                b = right_pointer - left_pointer
                area = h*b
                left_pointer += 1
            if area > max_area:
                max_area = area

        return max_area


def main():
    sol = Solution()
    height = [2, 6, 5, 4, 4, 9, 1]
    out = sol.maxArea(height)
    print(out)

if __name__ == '__main__':
    main()