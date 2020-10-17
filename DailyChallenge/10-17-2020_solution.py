class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for i in range(len(s)):
            seq = s[i:i+10]
            if seq in seen:
                res.add(seq)
            else:
                seen.add(seq)

        return res

# Below is using a trie
#         len_s = len(s)
#         if len_s < 11:
#             return []

#         t = {}
#         r = []
#         st = s[:10]
#         for i in range(10, len_s+1):
#             seen = True
#             tm = t
#             for c in st:
#                 if c not in tm:
#                     seen = False
#                     tm[c] = {}
#                     tm = tm[c]
#                 else:
#                     tm = tm[c]

#             if seen and st not in r:
#                 r.append(st)

#             if i < len_s:
#                 st = st[1:] + s[i]

#         return r
