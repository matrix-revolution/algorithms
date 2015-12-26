class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        pointer_m = 0
        pointer_n = 0

        size_num1 = len(nums1)
        end_m = size_num1-1

        count = end_m

        if n != 0:
            for i in range(m-1, -1, -1):
                nums1[count] = nums1[i]
                nums1[i] = -1
                count -= 1

        end_m = count + 1

        while end_m < size_num1 and pointer_n < n and pointer_m < size_num1:
            if nums1[end_m] > nums2[pointer_n]:
                nums1[pointer_m] = nums2[pointer_n]
                pointer_m += 1
                pointer_n += 1

            elif nums1[end_m] < nums2[pointer_n]:
                nums1[pointer_m] = nums1[end_m]
                pointer_m += 1
                end_m += 1

        while pointer_n < n and pointer_m < size_num1:
            nums1[pointer_m] = nums2[pointer_n]
            pointer_m += 1
            pointer_n += 1

        print nums1


def main():
    nums1 = [1, 2, 7, 9, 10, 15, -1, -1, -1, -1, -1]
    nums2 = [5, 8, 12, 16, 20]
    m = 6
    n = len(nums2)
    new_obj = Solution()
    new_obj.merge(nums1, m, nums2, n)
    print nums1

if __name__ == '__main__':
    main()
