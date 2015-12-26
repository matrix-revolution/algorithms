class Solution(object):

    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value_store = {}
        flag = False
        for i in nums:
            if i not in value_store:
                value_store[i] = 1
            else:
                value_store[i] += 1
                flag = True
                break
        return flag


def main():
    new_obj = Solution()
    nums = [1, 2, 1, 3, 5, 2, 4, 5, 3, 5, 16]
    out = new_obj.contains_duplicate(nums)
    print out

if __name__ == '__main__':
    main()