class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        value_store = {}
        size_nums = len(nums)

        for i in range(0, size_nums):
            num = nums[i]
            if num not in value_store:
                value_store[num] = i
            else:
                prev_idx = value_store[num]
                curr_idx = i
                diff = curr_idx - prev_idx
                if diff <= k:
                    return True
                else:
                    value_store[num] = curr_idx
        return False


def main():
    nums = [1, 5, 2, 7, 2, 8]
    new_obj = Solution()
    k = 3
    out = new_obj.containsNearbyDuplicate(nums, k)
    print out

if __name__ == '__main__':
    main()
