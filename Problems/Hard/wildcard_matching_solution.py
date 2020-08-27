class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        regex_table = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        regex_table[0][0] = True # empty string case, also rt[0][X] or rt[X][0] where X > 0 is meaningless

        # Handle the case where s = "" and p is not
        for i in range(2, len(p) + 1):
            regex_table[i][0] = p[i-1] == "*" and regex_table[i-2][0]

        # Typical case
        for i in range(1,len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i-1] != "*":
                    # True only if last match was true and current match is also true
                    regex_table[i][j] = regex_table[i-1][j-1] and (s[j-1] == p[i-1] or p[i-1] == ".")
                else:
                    # Could just have the previous regex match to be true and call it a day since x* could match nothing
                    # Or current char in s to match/regex match is '.' as well as the previous char in s matching
                    regex_table[i][j] = regex_table[i-2][j] or ((p[i-2] == s[j-1] or p[i-2] == ".") and regex_table[i][j-1])

        return regex_table[-1][-1]
    
