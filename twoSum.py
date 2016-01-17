class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store_input = {}
        store_output = {}
        output = []
        count = 0
        for i in range(0, len(nums)):
            if len(store_input) <= 0:
                store_input[nums[i]] = i
            else:
                val = target - nums[i]
                if val in store_input:
                    output.append(store_input[val])
                    output.append(i)
                    return output
                else:
                    store_input[nums[i]] = i
        return output



def main():
    sol = Solution()
    nums = [2, 7, 11, 2, 15]
    target = 17
    out = sol.twoSum(nums, target)
    print(out)


if __name__ == '__main__':
    main()