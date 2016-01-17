class Solution(object):

    def call_search(self, nums, target, low, high):

        if target == nums[low]:
            return low
        if target == nums[high]:
            return high

        while low < high:
            mid = (low + high) / 2

            if target == nums[mid]:
                return mid
            if low == mid:
                if target == nums[high]:
                    return high
                else:
                    return -1

            if nums[low] <= nums[high]:
                if target < nums[mid]:
                    high = mid - 1
                elif target > nums[mid]:
                    low = mid
                else:
                    return -1

            elif nums[low] > nums[high]:
                if target < nums[mid]:
                    if nums[mid] > nums[low]:
                        if target < nums[high]:
                            low = mid
                        elif target > nums[high]:
                            high = mid - 1
                    elif nums[mid] < nums[low]:
                        high = mid - 1

                elif target > nums[mid]:
                    if nums[mid] > nums[low]:
                        low = mid
                    elif nums[mid] < nums[low]:
                        if target < nums[high]:
                            low = mid
                        elif target > nums[high]:
                            high = mid - 1
                else:
                    return -1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)

        low = 0
        high = len_nums - 1

        out = self.call_search(nums, target, low, high)
        return out

def main():
    sol = Solution()
    # nums = [0, 1, 2, 4, 5, 6, 7]
    # nums = [4, 5, 6, 7, 0, 1, 2]
    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 4
    idx = sol.search(nums, target)
    print 'index is: %d' % idx

if __name__ == '__main__':
    main()