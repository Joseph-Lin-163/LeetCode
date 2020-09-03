class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # Using a tracker
#         if k == 0:
#             return False

#         print(len(nums))
#         if t == 0:
#             if len(set(nums)) != len(nums):
#                 return True
#             else:
#                 return False

#         tracker = []
#         for i in range(1, len(nums)):
#             diff = nums[i] - nums[i-1]
#             if i < k + 1:
#                 tracker.append(0)
#                 tracker = [x+diff for x in tracker[:i]] + tracker[i:]
#                 if any([abs(x) < t + 1 for x in tracker[:i]]):
#                     return True
#             else:
#                 # tracker = tracker[1:]
#                 if any([abs(x) < t + 1 for x in tracker]):
#                     return True
#                 tracker = [x+diff for x in tracker][1:] + [diff]
#                 # if any([abs(x) < t + 1 for x in tracker]):
#                 #     return True
#             # print("i: {}, tracker: {}, diff: {}".format(i, tracker, diff))

#         if any([abs(x) < t + 1 for x in tracker]):
#             return True
#         return False


        # Using Bucket Algorithm, more efficient
        if t < 0:
            return False
        d = {}

        for i in range(len(nums)):
            idx = nums[i] // (t+1)
            if idx in d:
                return True
            if idx-1 in d and abs(nums[i]-d[idx-1]) < (t+1):
                return True
            if idx+1 in d and abs(nums[i]-d[idx+1]) < (t+1):
                return True
            d[idx] = nums[i]

            if(i >= k):
                del d[nums[i-k]//(t+1)]

            # print(d)
        return False
