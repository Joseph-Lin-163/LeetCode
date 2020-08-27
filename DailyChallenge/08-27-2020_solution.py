import bisect

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # dict where k is the start point and v is the index
        start_point_idxs = {start[0]: idx for idx, start in enumerate(intervals)}
        max_start = max(start_point_idxs)
        sorted_keys = sorted(start_point_idxs)
        return [-1 if x[1] > max_start else start_point_idxs[x[1]] if x[1] in start_point_idxs else start_point_idxs[sorted_keys[bisect.bisect(sorted_keys, x[1])]] for x in intervals]
            
