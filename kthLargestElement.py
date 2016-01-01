class Solution(object):
    def find_min(self, nums, low, high, flag):
        min_v = min(nums[low], nums[low + 1])
        prev_min = max(nums[low], nums[low + 1])
        low += 2
        while low < high:
            if nums[low] < min_v:
                prev_min = min_v
                min_v = nums[low]
            elif nums[low] < prev_min:
                prev_min = nums[low]
            low += 1
        if flag:
            return min_v
        return prev_min

    def find_max(self, nums, low, high, flag):
        max_v = max(nums[low], nums[low + 1])
        pre_max = min(nums[low], nums[low + 1])
        low += 2
        while low < high:
            if nums[low] > max_v:
                pre_max = max_v
                max_v = nums[low]
            elif nums[low] > pre_max:
                pre_max = nums[low]
            low += 1
        if flag:
            return max_v
        return pre_max

    def call_recursion(self, low, high, nums, n):
        len_val = high - low + 1
        if len_val <= 1:
            return nums[low]
        if n == 1:
            return self.find_min(nums, low, high, 1)
        if n == 2:
            return self.find_min(nums, low, high, 0)
        if n == len(nums):
            return self.find_max(nums, low, high, 1)
        if n == len(nums) - 1:
            return self.find_max(nums, low, high, 0)

        mid = int((low + high)/2)
        val = nums[mid]
        left_pointer = low
        right_pointer = high

        while left_pointer < right_pointer:
            if nums[left_pointer] > val >= nums[right_pointer]:
                temp = nums[left_pointer]
                nums[left_pointer] = nums[right_pointer]
                nums[right_pointer] = temp
                left_pointer += 1
                right_pointer -= 1
            else:
                if val < nums[right_pointer]:
                    right_pointer -= 1
                elif nums[left_pointer] <= val:
                    left_pointer += 1

        if nums[left_pointer] == val:
            left_pointer += 1

        left_partition_len = left_pointer - low

        if left_partition_len < n:
            return self.call_recursion(left_pointer, high, nums, n-left_partition_len)
        else:
            high = left_pointer - 1
            return self.call_recursion(low, high, nums, n)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        len_nums = high - low + 1
        if k > len_nums:
            return -1
        n = len(nums) - k + 1
        output = self.call_recursion(low, high, nums, n)
        return output


def main():
    sol = Solution()
    nums = [3, 3, 3, 3, 4, 3, 3, 3, 3]
    k = 5
    out = sol.findKthLargest(nums, k)
    print out

if __name__ == '__main__':
    main()