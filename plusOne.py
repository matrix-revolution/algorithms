class Solution(object):

    def reverse_digits(self, digits):
        size_digits = len(digits)
        start_pointer = 0
        end_pointer = size_digits - 1

        i = 0
        while i < end_pointer-i:
            temp = digits[i]
            digits[i] = digits[end_pointer-i]
            digits[end_pointer-i] = temp
            i += 1

        print digits

    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        additive = 1
        self.reverse_digits(digits)
        i = 0
        while i < len(digits):
            val = digits[i] + additive
            remainder = val % 10
            quotient = val / 10
            additive = quotient
            digits[i] = remainder
            i += 1

        if additive > 0:
            digits.append(additive)
        self.reverse_digits(digits)
        return digits


def main():
    digits = [1, 2, 3]
    # digits = [9, 9, 9]
    new_obj = Solution()
    output = new_obj.plus_one(digits)
    print(output)


if __name__ == '__main__':
    main()