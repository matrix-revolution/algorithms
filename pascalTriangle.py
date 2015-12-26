class Solution(object):

    def initialize_or_terminate_list(self, inner_list):
        inner_list.append(1)

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        if numRows <= 0:
            return []
        if numRows == 1:
            output.append([1])
        count = 0
        while count < numRows:
            inner_list = []
            self.initialize_or_terminate_list(inner_list)
            k = 1
            while k < count:
                prev_inner_list = output[count-1]
                val = prev_inner_list[k] + prev_inner_list[k-1]
                inner_list.append(val)
                k += 1
            if count > 0:
                self.initialize_or_terminate_list(inner_list)
            output.append(inner_list)
            count += 1

        return output


def main():
    new_obj = Solution()
    num_rows = 7
    output = new_obj.generate(num_rows)
    print output

if __name__ == '__main__':
    main()