class Solution(object):
    def partition(self, ar):
        val = ar[0]
        left_pointer = 0
        right_pointer = len(ar) - 1

        while left_pointer < right_pointer:
            if ar[left_pointer] > val >= ar[right_pointer]:
                temp = ar[left_pointer]
                ar[left_pointer] = ar[right_pointer]
                ar[right_pointer] = temp
                left_pointer += 1
                right_pointer -= 1
            else:
                if val < ar[right_pointer]:
                    right_pointer -= 1
                elif ar[left_pointer] <= ar:
                    left_pointer += 1

        temp = ar[left_pointer]
        ar[left_pointer] = ar[0]
        ar[0] = temp

        return ar


def main():
    sol = Solution()
    ar = [4, 5, 3, 7, 2]
    out = sol.partition(ar)
    print(out)

if __name__ == '__main__':
    main()
