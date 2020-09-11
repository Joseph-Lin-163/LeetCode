class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # No zeros were found
        # Can have odd negatives (return max(nums[:last_neg], nums[first_neg+1:]))
        # Can have no negatives (return product all)
        # Can have even negatives (return product all)

        if len(nums) == 1:
            return nums[0]

        def get_prod(num_list):
            if len(num_list) == 1:
                return num_list[0]

            if len([x for x in num_list if x < 0]) % 2 == 1:
                neg_idxs = [idx for idx, val in enumerate(num_list) if val < 0]
                return max(math.prod(num_list[:neg_idxs[-1]]), math.prod(num_list[neg_idxs[0] + 1:]))
            else:
                return math.prod(num_list)

        zero_idxs = [idx for idx, val in enumerate(nums) if val == 0]
        #print(zero_idxs)
        sub_arrays_div_zero = None
        if zero_idxs:
            if zero_idxs[0] != 0:
                zero_idxs.insert(0, -1)
            zero_tmp = zero_idxs[1:] + [len(nums)]
            zero_idxs = [x+1 for x in zero_idxs]
            sub_arrays_div_zero = [x for x in zip(zero_idxs, zero_tmp)]
        #print(sub_arrays_div_zero)

        if sub_arrays_div_zero:
            print(sub_arrays_div_zero)
            return max([get_prod(nums[x:y]) for x,y in sub_arrays_div_zero if x != y] + [0])
        else:
            return get_prod(nums)
            
