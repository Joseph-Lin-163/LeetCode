class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele = {}
        maj_ele = [] # len(2) is max
        maj_num = len(nums)/3
        for i in nums:
            if i in maj_ele:
                continue

            ele[i] = ele.get(i, 0) + 1
            if ele[i] > maj_num:
                maj_ele.append(i)
                if len(maj_ele) == 2:
                    return maj_ele

        return maj_ele
        
