class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        len_store = []
        for i in range(0, len(nums)):
            if i == 0:
                len_store.append(1)
                output = 1
            else:
                k = i-1
                max_len = 1
                while k >= 0:
                    if nums[k] < nums[i]:
                        size = len_store[k] + 1
                        if size > max_len:
                            max_len = size
                    k -= 1
                len_store.append(max_len)
            if len_store[i] > output:
                output = len_store[i]
        return output





def main():
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 9, 3, 101, 18]
    out = sol.lengthOfLIS(nums)
    print out

if __name__ == '__main__':
    main()