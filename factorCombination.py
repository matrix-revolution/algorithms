import copy
class Solution(object):

    def call_recur(self, n, out, sub_list):
        if n < 2:
            return
        k = 2
        while n / k >= k:
            rem = n % k
            if rem == 0:
                val = n / k
                if len(sub_list) > 0 and sub_list[len(sub_list) - 1] > k:
                    pass
                elif val >= k:
                    copy_sub = copy.deepcopy(sub_list)
                    copy_sub.append(k)
                    new_sub = copy.deepcopy(copy_sub)
                    copy_sub.append(val)
                    out.append(copy_sub)
                    del copy_sub
                    self.call_recur(val, out, new_sub)
                    del new_sub
                k += 1
            else:
                k += 1
        return

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        out = []
        sub_list = []
        self.call_recur(n, out, sub_list)
        return out


def main():
    sol = Solution()
    n = 48
    out = sol.getFactors(n)
    print(out)

if __name__ == '__main__':
    main()