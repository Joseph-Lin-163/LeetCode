class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
#         for i in range(len(s)):
#             if i > len(s)/2:
#                 return False

#             if s[i+1:(2*i)+2] == s[:i+1]:
#                 s_so_far = s[:i+1]
#                 if len(s) % len(s_so_far) != 0:
#                     continue

#                 repeats = True
#                 for i in range(len(s_so_far), len(s), len(s_so_far)):
#                     if s[i:i+len(s_so_far)] != s_so_far:
#                         repeats = False

#                 if not repeats:
#                     continue

#                 return True

#         return False

        # Simple one-liner
        return s in (s + s)[1:-1]
