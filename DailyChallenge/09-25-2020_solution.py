class Solution:
    def largestNumber(self, nums: List[int]) -> str:
#         nums_str = {str(x):[] for x in range(0,10)}
#         for n in nums:
#             s = str(n)
#             nums_str[s[0]].append(s)

#         def comp_st(s1, s2):
#             if len(s1) == len(s2):
#                 if s1 < s2:
#                     return s2
#                 else:
#                     return s1
#             elif len(s1) < len(s2):
#                 if s1 < s2[:len(s1)]:
#                     return s2
#                 elif s1 > s2[:len(s1)]:
#                     return s1
#                 else:
#                     if s2[len(s1)] > s1[0]:
#                         return s2
#                     elif s2[len(s1)] < s1[0]:
#                         return s1
#                     else:
#                         greater = comp_st(s2[len(s1):],s1)
#                         if greater == s2[len(s1):]:
#                             return s2
#                         else:
#                             return s1
#             else:
#                 if s1[:len(s2)] < s2:
#                     return s2
#                 elif s1[:len(s2)] > s2:
#                     return s1
#                 else:
#                     greater = comp_st(s1[len(s2):],s2)
#                     if greater == s1[len(s2):]:
#                         return s1
#                     else:
#                         return s2


#         def sort_list(num_st):
#             if len(num_st) <= 1:
#                 return num_st
#             max_len = max([len(x) for x in num_st])

#             sorted_numst = []
#             while num_st:
#                 if len(num_st) == 1:
#                     sorted_numst.append(num_st[0])
#                     return sorted_numst
#                 t_max = num_st[0]
#                 for i in range(1,len(num_st)):
#                     t_max = comp_st(t_max, num_st[i])
#                 sorted_numst.append(t_max)
#                 num_st.remove(t_max)

#         result = ''
#         for i in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']:
#             # nums_str[i] = sort_list(nums_str[i])
#             result = result + ''.join(sort_list(nums_str[i]))

#         if result[0] == '0':
#             result = '0'

#         return result

        # The way this cmp works is just by concatenating the two numbers and seeing which is bigger
        # This works to properly sort the list using cmp_to_key
        def cmp(x, y):
            u = x + y
            v = y + x
            if u == v:
                return 0
            elif u < v:
                return -1
            else:
                return 1

        v = map(str, nums)
        result = ''.join(reversed(sorted(v, key=cmp_to_key(cmp))))
        if result and result[0] == '0':
            return '0'
        else:
            return result
    
