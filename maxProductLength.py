

# function returns bool whether any character is common to both the words or not

def has_common_character(word_1, word_2):
    flag = False
    for letter_1 in word_1:
        for letter_2 in word_2:
            if letter_1 == letter_2:
                flag = True
            if flag:
                break
        if flag:
            break
    return flag


def max_product_length(words):
    flag = False
    max_val = 0
    for word_1 in words:
        for word_2 in words:
            if not has_common_character(word_1, word_2):
                flag = True
                len_val = len(word_1) * len(word_2)
                if len_val > max_val:
                    max_val = len_val
    if flag:
        return max_val
    else:
        return 0


def main():
    # words = ['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef']
    # words = ['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd']
    words = ['a', 'aa', 'aaa', 'aaaa']
    max_val = max_product_length(words)
    print 'max product length'
    print max_val

if __name__ == '__main__':
    main()