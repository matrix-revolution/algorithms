class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.stack_store = []
        self.len_store = 0
        self.words = words
        self.len_words = len(words)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        small_dic = {}
        diff_val = -1

        if self.len_store == 0:
            for i in range(0, self.len_words):
                word = self.words[i]
                self.stack_store.append(word)
                if word == word1 or word == word2:
                    if word not in small_dic:
                        small_dic[word] = i
                    if word1 in small_dic and word2 in small_dic:
                        if diff_val == -1:
                            diff_val = abs(small_dic[word1] - small_dic[word2])
                        else:
                            small_dic[word] = i
                            new_val = abs(small_dic[word1] - small_dic[word2])
                            if new_val < diff_val:
                                diff_val = new_val
            self.len_store = len(self.stack_store)

        else:
            k = self.len_store - 1
            while k >= 0:
                val = self.stack_store.pop()
                if val == word1 or val == word2:
                    if val not in small_dic:
                        small_dic[val] = k
                    if word1 in small_dic and word2 in small_dic:
                        if diff_val == -1:
                            diff_val = abs(small_dic[word1] - small_dic[word2])
                        else:
                            small_dic[val] = k
                            new_val = abs(small_dic[word1] - small_dic[word2])
                            if new_val < diff_val:
                                diff_val = new_val
                k -= 1

        return diff_val


def main():
    words = ["practice", "makes", "perfect", "coding", "makes"]
    obj = WordDistance(words)
    word1 = 'coding'
    word2 = 'makes'
    out = obj.shortest(word1, word2)
    print(out)
    out = obj.shortest('perfect', 'practice')
    print(out)

if __name__ == '__main__':
    main()



# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")