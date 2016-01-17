class Solution(object):
    def sort_string(self, nums):
        nums_str = []
        for i in range(0, len(nums)):
            nums_str.append(str(nums[i]))
        out = self.merge_sort(0, len(nums_str)-1, nums_str)
        return out

    def compare(self, first, second):
        len_first = len(first)
        len_second = len(second)
        m = 0
        n = 0
        while m < len_first and n < len_second:
            if int(first[m]) < int(second[n]):
                return -1
            elif int(first[m]) > int(second[n]):
                return 1
            else:
                m += 1
                n += 1
        if m == len_first and n < len_second:
            while n < len_second:
                if int(second[n]) < int(first[0]):
                    return 1
                elif int(second[n]) > int(first[0]):
                    return -1
                else:
                    n += 1
            if int(second[n-1]) < int(first[m-1]):
                return 1
            else:
                return -1
        elif n == len_second and m < len_first:
            while m < len_first:
                if int(first[m]) < int(second[0]):
                    return -1
                elif int(first[m]) > int(second[0]):
                    return 1
                else:
                    m += 1
            if int(first[m-1]) > int(second[n-1]):
                return 1
            else:
                return -1


    def merge(self, low, high, mid, nums):
        first = low
        second = mid+1
        while first < second <= high:
            if self.compare(nums[first], nums[second]) == 1:
                temp = nums[second]
                k = second
                while k != first:
                    nums[k] = nums[k-1]
                    k -= 1
                nums[first] = temp
                second += 1
            else:
                first += 1
        return nums

    def merge_sort(self, low, high, nums):

        mid = (low + high)/2
        if high == low:
            return
        self.merge_sort(low, mid, nums)
        self.merge_sort(mid+1, high, nums)

        nums = self.merge(low, high, mid, nums)
        return nums

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return str(nums[0])
        out = self.sort_string(nums)
        largest_num = ''
        for i in range(len(out)-1, -1, -1):
            largest_num += out[i]
        if int(largest_num[0]) == 0:
            return '0'
        return largest_num


def main():
    sol = Solution()
    #nums = [1]
    #nums = [99, 8, 84, 5, 91]
    #nums = [128, 12, 320, 32]
    nums = [121, 12]
    #nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    #nums = [824,938,1399,5607,6973,5703,9609,4398,8247]
    """nums = [4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,
            3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,
            1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,
            1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,
            5460,3399,9533,914,3932,192,
            3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398]
    """
    out = sol.largestNumber(nums)
    print(out)

if __name__ == '__main__':
    main()