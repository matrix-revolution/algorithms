class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = - pow(2, 31)
        prev_max = 0
        prev_min = 0

        for i in range(0, len(nums)):
            if i == 0:
                max_val = nums[i]
                prev_max = max_val
                prev_min = max_val
            else:
                curr_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
                curr_min = min(prev_max * nums[i], prev_min * nums[i], nums[i])
                if curr_max > max_val:
                    max_val = curr_max
                prev_max = curr_max
                prev_min = curr_min
        return max_val


def main():
    sol = Solution()
    nums = [2, 3, -2, -4]
    out = sol.maxProduct(nums)
    print(out)

if __name__ == '__main__':
    main()