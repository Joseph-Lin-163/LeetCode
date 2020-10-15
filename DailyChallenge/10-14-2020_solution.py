class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now
        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))
#         if len(nums) < 4:
#             return max(nums)

#         l1=[nums[0],nums[1],nums[0]+nums[2]]
#         l2=[0,nums[1],nums[2]]

#         for i in range(3,len(nums)):
#             l1.append(max(nums[i]+l1.pop(0),nums[i]+l1[0]))
#             l2.append(max(nums[i]+l2.pop(0),nums[i]+l2[0]))

#         return max(l1[0],l1[1],l2[2])



#         if not nums:
#             return 0

#         len_nums = len(nums)
#         if len_nums == 1:
#             return nums[0]

#         # d = []
#         # for i, v in enumerate(nums):
#         #     d.append((i,v))
#         nums = [(i,nums[i]) for i in range(len_nums)]
#         nums.sort(key=lambda x: x[1], reverse=True)
#         houses = []
#         total = 0
#         for idx, num in nums:
#             if idx - 1 in houses or idx + 1 in houses:
#                 # print("skip: {} {}".format(idx, num))
#                 continue
#             else:
#                 # print(idx, num)
#                 houses.append(idx)
#                 if idx == 0:
#                     houses.append(len_nums)
#                 elif idx == len_nums - 1:
#                     houses.append(-1)
#                 total += num

        # return total
