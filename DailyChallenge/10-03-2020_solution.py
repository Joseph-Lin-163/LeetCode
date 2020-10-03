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

        # alternative implementation
        # d = collections.Counter(nums)
        # # return len([True for n in d if d[n]!=1]) if k == 0 else len([True for n in d if n-k in d])
        # count = 0
        # def inc():
        #     nonlocal count
        #     count += 1
        #
        # if k == 0:
        #     [inc() for n in d if d[n] != 1]
        # else:
        #     [inc() for n in d if n-k in d]
        #
        # return count
