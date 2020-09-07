class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pat = [x for x in pattern]
        word_list = str.split()
        # print(pat, word_list)
        if len(pat) != len(word_list):
            return False

        d = {}
        for c, word in zip(pat, word_list):
            if c not in d:
                d[c] = word
                continue

            if d[c] != word:
                return False

        if len(set(d.values())) != len(d.values()):
            return False

        return True
        
