class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        sum_update = 0
        max_val = 0
        for i in range(0, len_nums):
            if i == 0:
                sum_update = nums[i]
                max_val = nums[i]
            else:
                sum_update = max(sum_update+nums[i], nums[i])
                if sum_update > max_val:
                    max_val = sum_update
        return max_val


def main():
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sum = sol.maxSubArray(nums)
    print sum

if __name__ == '__main__':
    main()