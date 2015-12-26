class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        low = 0
        high = len_nums - 1
        star_point = -1
        end_point = -1

        if low == high and nums[low] == target:
            return [low, low]

        while low < high:
            mid = int((low + high)/2)
            if nums[mid] == target:
                if star_point == -1:
                    star_point = mid
                    end_point = mid

                if nums[mid+1] > target:
                    high = mid
                elif nums[mid+1] == target:
                    low = mid
                     #nums[mid+1] != target:
                    end_point = mid
                    return [star_point, end_point]
                low = mid

            if low == mid:
                if nums[high] == target:
                    if star_point != -1:
                        end_point = high
                    else:
                        star_point = high
                        end_point = high
                    return [star_point, end_point]
                else:
                    return [star_point, end_point]

            if nums[mid] < target:
                low = mid
            elif nums[mid] > target:
                high = mid
            else:
                return [star_point, end_point]
        return [star_point, end_point]


def main():
    sol = Solution()
    # nums = [5, 7, 7, 8, 8, 10]
    nums = [1, 1, 2]
    target = 1
    output = sol.searchRange(nums, target)
    print output

if __name__ == '__main__':
    main()