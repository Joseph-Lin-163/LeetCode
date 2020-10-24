class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, s3 = [], -float('inf')
        for num in nums[::-1]:
            if num < s3: return True
            while stack and stack[-1] < num: s3 = stack.pop()
            stack.append(num)
        return False

#         seen = set([nums[0]])
#         new_nums = [nums[0]]
#         for i in range(1,len(nums)):
#             n = nums[i]
#             if n not in seen or new_nums[-1] != n:
#                 new_nums.append(n)
#                 seen.add(n)

#         nums = new_nums
#         len_n = len(nums)
#         if len_n < 3 or len(seen) < 3:
#             return False

#         i,j,k = 0,1,2
#         while k != len_n-1 or j != len_n-2 or i != len_n-3:
#             # print(i,j,k)
#             if nums[i] < nums[k] < nums[j]:
#                 return True

#             if k != len_n-1:
#                 k+=1
#             elif k == len_n-1 and j != len_n-2:
#                 j+=1
#                 k=j+1
#             else: # k == len_n-1 and j == len_n-2:
#                 i+=1
#                 j=i+1
#                 k=j+1

#         if nums[i] < nums[k] < nums[j]:
#             return True
#         else:
#             return False
