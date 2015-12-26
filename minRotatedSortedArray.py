class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) -1

        if nums[low] > nums[high]:
            while low < high:
                mid = int((low+high)/2)
                if low == mid:
                    val = min(nums[low], nums[high])
                    return val
                elif nums[mid] > nums[low]:
                    low = mid
                elif nums[mid] < nums[low]:
                    high = mid

        elif nums[low] > nums[high]:
            return nums[low]
        else:
            return nums[low]
def main():
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    out = sol.findMin(nums)
    print out

if __name__ == '__main__':
    main()