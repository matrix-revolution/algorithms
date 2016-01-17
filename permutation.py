import copy


class Solution(object):
    def call_recursion(self, nums, sub_list, store, output, count):
        if len(sub_list) == len(nums):
            output.append(sub_list)
            return
        sub_list = copy.deepcopy(sub_list)
        for i in range(count, len(nums)):
            copy_list = copy.deepcopy(sub_list)
            copy_list.append(store[0])
            if len(store) <= 0:
                return
            val = store.pop(0)
            self.call_recursion(nums, copy_list, store, output, count+1)
            store.append(val)
        return

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sub_list = []
        output = []
        count = 0
        store = copy.deepcopy(nums)
        self.call_recursion(nums, sub_list, store, output, count)
        return output


def main():
    sol = Solution()
    nums = [1, 2, 3]
    out = sol.permute(nums)
    print 'len of out: %d' % len(out)

if __name__ == '__main__':
    main()