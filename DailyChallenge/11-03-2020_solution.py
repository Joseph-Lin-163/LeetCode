class Solution:
    def maxPower(self, s: str) -> int:
        max_len = -inf
        c = s[0]
        tmp = 0
        for i in range(len(s)):
            if s[i] == c:
                tmp += 1
            else:
                if tmp > max_len:
                    max_len = tmp
                tmp = 1
                c = s[i]


        if tmp > max_len:
            return tmp
        else:
            return max_len

        
