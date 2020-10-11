class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Original solution can hit 99% at 24ms
#         d = []
#         for char in s:
#             if char not in d:
#                 d.append(char)
#                 if len(d) == 26:
#                     break

#         d.sort()
#         ret = ""
#         while d:
#             len_ret = len(ret)
#             d_idx = 0
#             # print("ret: {}".format(ret))
#             while len_ret == len(ret):
#                 if d_idx >= len(d):
#                     print("Error, d_idx >= len(d)")
#                     return
#                 char = d[d_idx]
#                 idx = s.find(char)
#                 # print(char, idx, s)
#                 for ch in d[d_idx+1:]:
#                     if s[idx:].find(ch) > 0:
#                         continue
#                     else:
#                         d_idx += 1
#                         break
#                 if d_idx >= len(d) or d[d_idx] != char:
#                     continue
#                 else:
#                     ret += char
#                     s = s[idx:]
#                     d.pop(d_idx)

#         return ret

        # Below is a more beautiful and simple solution, although it's debatable which one does more work
        d={c:i for i,c in enumerate(s)}
        res=""
        for i,x in enumerate(s):
            if x not in res:
                while res and x < res[-1] and i < d[res[-1]]:
                    res=res[:-1]
                res+=x
        return res
