

class Solution(object):

    def get_hint(self, secret, guess):

        len_str = len(secret)
        a = [0 for i in range(0, 10)]
        b = [0 for j in range(0, 10)]
        count_cows = 0
        count_bull = 0
        for i in range(0, len_str):

            a_val = int(secret[i])
            b_val = int(guess[i])

            if a_val == b_val:
                count_bull += 1

            else:
                a[int(secret[i])] += 1
                b[int(guess[i])] += 1

        for j in range(0, 10):
            count_cows += min(a[j], b[j])

        output = str(count_bull)+'A'+str(count_cows)+'B'
        return output


def main():

    """ test case 1

    secret = '1807'
    guess = '7810'"""

    #test case 2
    secret = '1123'
    guess = '0111'
    newObj = Solution()
    out = newObj.get_hint(secret, guess)
    print out

if __name__ == '__main__':
    main()
