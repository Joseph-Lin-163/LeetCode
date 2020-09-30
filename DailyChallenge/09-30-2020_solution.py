class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        len_n = len(nums)
        while i < len_n:
            if nums[i] == i+1:
                i += 1
                continue

            if nums[i] <= 0 or nums[i] > len_n:
                nums[i] = 0
                i += 1
                continue

            if nums[i] > i+1:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                if tmp <= 0 or tmp > len_n or tmp == nums[i]:
                    nums[i] = 0
                    i += 1
                else:
                    nums[i] = tmp
                continue

            if nums[i] < i+1:
                nums[nums[i]-1] = nums[i]
                nums[i] = 0
                i += 1
                continue

        i = 0
        while i < len_n:
            if nums[i] == 0:
                return i + 1
            i+=1

        return len_n + 1
