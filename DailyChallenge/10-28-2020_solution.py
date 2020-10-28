class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        len_n = len(nums)
        if len_n == 1:
            return [str(nums[0])]

        ranges = []
        last = 0

        for i in range(0,len_n-1):
            if i != len_n - 2 and nums[i] + 1  == nums[i+1]:
                continue
            elif i == len_n - 2 and nums[i] + 1 == nums[i+1]:
                ranges.append("{}->{}".format(nums[last], nums[i+1]))
            elif i == len_n - 2 and nums[i] + 1 != nums[i+1]:
                if i == last:
                    ranges.append(str(nums[i]))
                else:
                    ranges.append("{}->{}".format(nums[last], nums[i]))
                ranges.append(str(nums[i+1]))
            else:
                if i == last:
                    ranges.append(str(nums[i]))
                else:
                    ranges.append("{}->{}".format(nums[last], nums[i]))
                last = i+1

        return ranges
