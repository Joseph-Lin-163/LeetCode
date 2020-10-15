class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        n = len(nums)
        k = k % n

        if k == 0:
            return

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)


    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
#         length = len(nums)
#         k = k  % length
#         if k == 0:
#             return

#         a = nums[length-k:]
#         b = nums[:length-k]
#         for i,v in enumerate(a):
#             nums[i] = v

#         for i,v in enumerate(b):
#             nums[i+k] = v


#         return
