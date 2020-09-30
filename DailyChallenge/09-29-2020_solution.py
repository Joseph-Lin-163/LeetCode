class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic={}
        for w in wordDict:
            if len(w) in dic:
                dic[len(w)].append(w)
            else:
                dic[len(w)]=[w]
        dp=[1]+[0]*len(s)
        for i in range(len(s)):
            for k in dic:
                if i-k+1>=0 and dp[i-k+1] and s[i-k+1:i+1] in dic[k]:
                    dp[i+1]=1
        return dp[-1]
