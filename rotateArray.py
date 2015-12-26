class Solution(object):

    def move_rest(self, nums):
        end = len(nums) - 2
        while end >= 0:
            nums[end + 1] = nums[end]
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k %= n
        elif k == n or k == 0:
            k = 0

        move_last = len(nums) - 1

        while k > 0:
            temp = nums[move_last]
            self.move_rest(nums)
            nums[0] = temp
            k -= 1


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 18
    new_obj = Solution()
    new_obj.rotate(nums, k)
    print nums

if __name__ == '__main__':
    main()