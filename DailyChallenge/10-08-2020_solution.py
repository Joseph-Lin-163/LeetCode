class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     return -1
        if not nums:
            return -1

        if target < nums[0] or target > nums[-1]:
            return -1

        ret = 0
        while True:
            half_length = int(len(nums)/2)

            if len(nums) == 1 and nums[0] == target:
                return 0

            if half_length < 1:
                return -1

            if nums[half_length] > target:
                nums = nums[:half_length]
            elif nums[half_length] < target:
                ret += half_length
                nums = nums[half_length:]
            else:
                return ret + half_length
