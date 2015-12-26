class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        val_store = [0 for i in range(0, len_nums+3)]
        for i in range(len_nums-1, -1, -1):
            val = nums[i] + max(val_store[i+2], val_store[i+3])
            val_store[i] = val

        return max(val_store[0], val_store[1])


def main():
    sol = Solution()
    nums = [5, 10, 2, 7, 4, 15, 12, 3]
    max = sol.rob(nums)
    print max

if __name__ == '__main__':
    main()