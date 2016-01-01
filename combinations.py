import copy


class Solution(object):
    def call_recursive(self, i, inner_list, n, k, output):
        copy_list = copy.deepcopy(inner_list)
        if i > n:
            return output
        copy_list.append(i)
        if len(copy_list) == k:
            output.append(copy_list)
        elif len(copy_list) != k:
            self.call_recursive(i+1, copy_list, n, k, output)
        if i+1 <= n:
            self.call_recursive(i+1, inner_list, n, k, output)
        else:
            return output
        return output

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        inner_list = []
        if k > n or k <= 0:
            return output
        if k == n:
            for i in range(1, n+1):
                inner_list.append(i)
            output.append(inner_list)
            return output
        i = 1
        output = self.call_recursive(i, inner_list, n, k, output)
        return output


def main():
    sol = Solution()
    n = 4
    k = 3
    output = sol.combine(n, k)
    print(output)

if __name__ == '__main__':
    main()