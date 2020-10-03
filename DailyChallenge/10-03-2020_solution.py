class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            d = {}
            for n in nums:
                d[n] = d.get(n, 0) + 1
            return len([x for x in d.values() if x > 1])

        nums = sorted(set(nums))
        i, j, s = 0, 0, 0
        length = len(nums)
        while j < length:
            if nums[j] - nums[i] > k:
                i += 1
                continue
            elif nums[j] - nums[i] < k:
                j += 1
                continue
            elif nums[j] - nums[i] == k:
                s += 1
                j += 1
                continue
        return s
