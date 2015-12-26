import copy
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value_store = {}
        max_v = 0
        for i in range(0, len(nums)):
            temp_list = []
            if i == 0:
                temp_list.append(nums[0])
                value_store[0] = temp_list
                max_v = 1
            else:
                len_store = len(value_store)
                k = len_store - 1
                temp_max = 0
                while k >= 0 and temp_max < max_v:
                    inner_list = value_store[k]
                    if nums[i] > inner_list[len(inner_list)-1]:
                        temp_list = copy.deepcopy(inner_list)
                        temp_list.append(nums[i])
                        value_store[len_store] = temp_list
                        temp_max = len(temp_list)
                        if max_v < len(temp_list):
                            max_v = len(temp_list)
                    k -= 1
                if k < 0:
                    new_list = []
                    new_list.append(nums[i])
                    value_store[len_store] = new_list
        return max_v




def main():
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 9, 3, 101, 18]
    out = sol.lengthOfLIS(nums)
    print out

if __name__ == '__main__':
    main()