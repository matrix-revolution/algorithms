class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'
                     , 'U', 'V', 'W', 'X', 'Y', 'Z']

        output = ''
        quo = 0
        rem = 0

        while n >= 0:
            if n <= 26:
                output += alphabets[n-1]
                break
            else:
                quo = n/26
                rem = n%26
                if rem == 0 and quo <= 26:
                    output += alphabets[quo - 2]
                    output += alphabets[25]
                    break
                if quo <= 26:
                    output += alphabets[quo - 1]
                    output += alphabets[rem - 1]
                    break
                else:

                    if rem == 0:
                        output += self.convertToTitle(quo-1)
                        output += alphabets[25]
                        break
                    output += self.convertToTitle(quo)
                    output += alphabets[rem - 1]
                    break
        return output


def main():
    sol = Solution()
    n = 26*26*27 + 27
    out = sol.convertToTitle(n)
    print(out)

if __name__ == '__main__':
    main()