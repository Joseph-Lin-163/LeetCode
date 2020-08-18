class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        x, y = 0, 0
        for i in range(len(s)):
            if s[i] not in s[x:y]:
                y = y + 1
            else:
                if (y - x) > max_len:
                    max_len = (y - x) 
                x = x + 1 + s[x:y].index(s[i])
                y = y + 1
                
        if max_len < y - x:
            return y - x
        
        return max_len
