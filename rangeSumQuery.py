class NumArray(object):
    nums = []
    """
    Idea is to store all the calculations once and then just refer the stored values to calculate further
    """
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        start_idx = 0
        end_idx = len(nums)
        val_store = {}
        for k in range(start_idx, end_idx):
            if k == start_idx:
                val_store[k] = nums[k]
            else:
                val_store[k] = val_store[k-1] + nums[k]
        self.nums = val_store

    """
    def sum_range(self, i, j):
        sum_of_array = 0
        k = i
        count = 0
        total = (j-i)/2
        while k <= i+total:
            sum_of_array = sum_of_array + self.nums[k]
            if j-count != k:
                sum_of_array += self.nums[j-count]
            count += 1
            k += 1
        return sum_of_array
    """

    def sum_range(self, i, j):

        if i == 0:
            sum_of_array = self.nums[j]
        else:
            sum_of_array = self.nums[j] - self.nums[i-1]

        return sum_of_array


def main():
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    print(num_array.sum_range(0, 2))

if __name__ == '__main__':
    main()

