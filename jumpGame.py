class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_nums = len(nums)
        valid_steps_idx = 0
        final_dest = len_nums-1
        start_point = 0
        for i in range(len_nums-1, -1, -1):
            steps_required = final_dest - i
            if nums[i] >= steps_required:
                valid_steps_idx = i
            else:
                if nums[i] >= valid_steps_idx -i:
                    valid_steps_idx = i
        if valid_steps_idx == start_point:
            return True
        return False


def main():
    sol = Solution()
    # nums = [3, 2, 1, 0, 4]
    nums = [2, 3, 1, 1, 4]
    out = sol.canJump(nums)
    print(out)

if __name__ == '__main__':
    main()