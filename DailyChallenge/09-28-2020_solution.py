class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         a = 1
#         len_nums = len(nums)
#         answers = []

#         def return_subarrays(L, answers):
#             # if answers == []:
#             #     return []
#             return [L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1) if L[i:i+j] not in answers]

#         for i in range(len_nums):
#             if nums[i] >= k:
#                 continue
#             while a < len_nums and math.prod(nums[i:a]) < k:
#                 a += 1
#             if math.prod(nums[i:a]) >= k:
#                 a -= 1

#             to_extend = return_subarrays(list(range(i,a)), answers)
#             answers.extend(to_extend)

        r, l, answer, prod, len_nums = 0, 0, 0, 1, len(nums)
        for r in range(len_nums):
            if nums[r] >= k:
                prod = 1
                l = r + 1
                continue

            prod *= nums[r]
            while prod >= k and l <= r:
                prod /= nums[l]
                l += 1

            if prod < k:
                answer += r - l + 1

        return answer
