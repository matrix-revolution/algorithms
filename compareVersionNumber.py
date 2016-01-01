class Solution(object):
    def no_zeros(self, list_ver, idx):
        len_list = len(list_ver)
        while idx < len_list:
            if int(list_ver[idx]) != 0:
                return True
            else:
                idx += 1
        return False

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if len(version1) > 1 and version1[1] != '.':
            version1 = version1.lstrip('0')
        if len(version2) > 1 and version2[1] != '.':
            version2 = version2.lstrip('0')
        if version1 == '':
            version1 = '0'
        if version2 == '':
            version2 = '0'

        list_ver1 = version1.split('.')
        list_ver2 = version2.split('.')

        i = 0
        j = 0
        while i < len(list_ver1) and j < len(list_ver2):
            if int(list_ver1[i]) < int(list_ver2[j]):
                return -1
            elif int(list_ver1[i]) > int(list_ver2[j]):
                return 1
            else:
                i += 1
                j += 1
        if len(list_ver1) == len(list_ver2):
            return 0
        elif len(list_ver1) < len(list_ver2) and self.no_zeros(list_ver2, j):
            return -1
        elif len(list_ver1) > len(list_ver2) and self.no_zeros(list_ver1, i) != 0:
            return 1
        else:
            return 0


def main():
    sol = Solution()
    ver1 = '1.0'
    ver2 = '1'
    out = sol.compareVersion(ver1, ver2)
    print(out)

if __name__ == '__main__':
    main()