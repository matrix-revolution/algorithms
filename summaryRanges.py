class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        start_range = 0
        end_range = 0
        prv_val = 0
        if len(nums) <= 0:
            return nums

        for i in range(0, len(nums)):
            if i == 0:
                start_range = nums[i]
                prv_val = nums[i]
                end_range = nums[i]
            else:
                if nums[i] == prv_val + 1:
                    prv_val = nums[i]
                    end_range = nums[i]
                else:
                    if end_range != start_range:
                        output.append(str(start_range)+'->'+str(end_range))
                    else:
                        output.append(str(start_range))
                    start_range = nums[i]
                    end_range = nums[i]
                    prv_val = nums[i]
        if end_range != start_range:
            output.append(str(start_range)+'->'+str(end_range))
        else:
            output.append(str(start_range))
        return output


def main():
    sol = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    output = sol.summaryRanges(nums)
    print(output)

if __name__ == '__main__':
    main()