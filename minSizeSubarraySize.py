import Queue
import sys


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        value_store = []
        len_nums = len(nums)
        min_sum = sys.maxint
        sum_v = 0
        if len_nums <= 0:
            return 0

        for i in range(0, len_nums):
            value_store.append(nums[i])
            sum_v += nums[i]
            if sum_v >= s:
                #min_sum = len(value_store)
                diff = sum_v - s
                while diff >= value_store[0]:
                    val = value_store.pop(0)
                    diff -= val
                    sum_v -= val
                if min_sum > len(value_store):
                    min_sum = len(value_store)
        if sum_v < s:
            return 0
        return min_sum


def main():
    sol = Solution()
    s = 7
    nums = [2, 3, 1, 2, 3, 3]
    out = sol.minSubArrayLen(s, nums)
    print out

if __name__ == '__main__':
    main()