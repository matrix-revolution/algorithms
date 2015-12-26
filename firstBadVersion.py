# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
version_list = []


def isBadVersion(version):
    global version_list
    if not version_list[version-1]:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low < high:
            mid = int((low+high)/2)
            is_bad = isBadVersion(mid)
            next_is_bad = isBadVersion(mid+1)
            if is_bad is False and next_is_bad is True:
                return mid
            if not is_bad:
                low = mid
            else:
                high = mid
            return mid


def main():
    sol = Solution()
    global version_list
    version_list = [0, 0]
    n = 2
    out = sol.firstBadVersion(n)
    print out

if __name__ == '__main__':
    main()