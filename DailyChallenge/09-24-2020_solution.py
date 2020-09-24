class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
#         sd, td = {}, {}
#         for c in s:
#             sd[c] = sd.get(c, 0) + 1
#         for c in t:
#             td[c] = td.get(c, 0) + 1

#         if len(sd) != len(td):
#             return (set(td) - set(sd)).pop()
#         else:
#             for key in sd:
#                 if sd[key] != td[key]:
#                     return key
        for c in string.ascii_lowercase:
            if c in t and t.count(c) != s.count(c):
                return c
