import copy


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        len_nums = len(nums)
        inner_list = []

        for i in range(0, len_nums):
            if i == 0:
                l_val = []
                inner_list.append([])
                l_val.append(nums[i])
                inner_list.append(l_val)
            else:
                curr_size = len(inner_list)
                for j in range(0, curr_size):
                    val = inner_list[j]
                    if len(val) <= 0:
                        l = []
                        l.append(nums[i])
                        inner_list.append(l)
                    else:
                        new_val = copy.deepcopy(val)
                        new_val.append(nums[i])
                        inner_list.append(new_val)

        return inner_list


def main():
    sol = Solution()
    nums = [1, 2, 3]
    output = sol.subsets(nums)
    print output

if __name__ == '__main__':
    main()