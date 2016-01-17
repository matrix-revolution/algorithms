class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.input_dic = {}
        self.output_dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        len_input_dic = len(self.input_dic)

        if len_input_dic >= 1:
            for key in self.input_dic:
                sum_v = number + key
                self.output_dic[sum_v] = 0

        self.input_dic[number] = 0

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value in self.output_dic:
            return True
        else:
            return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)

def main():
    two_sum = TwoSum()
    two_sum.add(2)
    two_sum.add(2)
    two_sum.add(3)
    two_sum.add(5)
    out = two_sum.find(4)
    print(out)
    out1 = two_sum.find(17)
    print(out1)

if __name__ == '__main__':
    main()