class Solution(object):
    def one_diff(self, val, goal):
        diff = 0
        for i in range(0, len(goal)):
            if val[i] != goal[i]:
                diff += 1
        if diff <= 1:
            return True
        else:
            return False

    def wordLadder(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        store = []
        store.append(word1)
        store.append(None)

        my_dict = {}
        my_dict[word1] = 0

        len_word = len(word1)
        k =0
        start_idx = ord('a')
        count = 0
        output = 1
        while count < len(store):
            k = 0
            while k < len_word:
                val = store[count]
                if val is not None:
                    for i in range(0, 26):
                        if k > 0:
                            val = val[:k] + chr(start_idx+i) + val[k+1:]
                        else:
                            val = chr(start_idx+i) + val[k+1:]
                        if val not in my_dict and val in words:
                            if self.one_diff(val, word2):
                                return output+2
                            my_dict[val] = 0
                            store.append(val)
                k += 1
            if val is not None:
                store.append(None)
                output += 1
            if len(my_dict) == len(words):
                return 0
            count += 1
        return 0


def main():
    sol = Solution()
    # words = ["dose","ends","dine","jars","prow","soap","guns","hops","cray","hove","ella","hour","lens","jive","wiry","earl","mara","part","flue","putt","rory","bull","york","ruts","lily","vamp","bask","peer","boat","dens","lyre","jets","wide","rile","boos","down","path","onyx","mows","toke","soto","dork","nape","mans","loin","jots","male","sits","minn","sale","pets","hugo","woke","suds","rugs","vole","warp","mite","pews","lips","pals","nigh","sulk","vice","clod","iowa","gibe","shad","carl","huns","coot","sera","mils","rose","orly","ford","void","time","eloy","risk","veep","reps","dolt","hens","tray","melt","rung","rich","saga","lust","yews","rode","many","cods","rape","last","tile","nosy","take","nope","toni","bank","jock","jody","diss","nips","bake","lima","wore","kins","cult","hart","wuss","tale","sing","lake","bogy","wigs","kari","magi","bass","pent","tost","fops","bags","duns","will","tart","drug","gale","mold","disk","spay","hows","naps","puss","gina","kara","zorn","boll","cams","boas","rave","sets","lego","hays","judy","chap","live","bahs","ohio","nibs","cuts","pups","data","kate","rump","hews","mary","stow","fang","bolt","rues","mesh","mice","rise","rant","dune","jell","laws","jove","bode","sung","nils","vila","mode","hued","cell","fies","swat","wags","nate","wist","honk","goth","told","oise","wail","tels","sore","hunk","mate","luke","tore","bond","bast","vows","ripe","fond","benz","firs","zeds","wary","baas","wins","pair","tags","cost","woes","buns","lend","bops","code","eddy","siva","oops","toed","bale","hutu","jolt","rife","darn","tape","bold","cope","cake","wisp","vats","wave","hems","bill","cord","pert","type","kroc","ucla","albs","yoko","silt","pock","drub","puny","fads","mull","pray","mole","talc","east","slay","jamb","mill","dung","jack","lynx","nome","leos","lade","sana","tike","cali","toge","pled","mile","mass","leon","sloe","lube","kans","cory","burs","race","toss","mild","tops","maze","city","sadr","bays","poet","volt","laze","gold","zuni","shea","gags","fist","ping","pope","cora","yaks","cosy","foci","plan","colo","hume","yowl","craw","pied","toga","lobs","love","lode","duds","bled","juts","gabs","fink","rock","pant","wipe","pele","suez","nina","ring","okra","warm","lyle","gape","bead","lead","jane","oink","ware","zibo","inns","mope","hang","made","fobs","gamy","fort","peak","gill","dino","dina","tier"]
    # word1 = 'nape'
    # word2 = 'mild'
    words = ['hot', 'dog']
    word1 = 'hot'
    word2 = 'dog'
    out = sol.wordLadder(words, word1, word2)
    print(out)

if __name__ == '__main__':
    main()