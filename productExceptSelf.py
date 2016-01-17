class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        out = []
        n = len(nums)
        left = [1 for i in range(0, n)]
        right = [1 for i in range(0, n)]

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            right[n-i-1] = right[n-i] * nums[n-i]

        for i in range(0, n):
            val = left[i] * right[i]
            out.append(val)
        return out


def main():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    out = sol.productExceptSelf(nums)
    print(out)

if __name__ == '__main__':
    main()