class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ni_0 = newInterval[0]
        ni_1 = newInterval[1]
        len_inter = len(intervals)
        ni_0_loc, ni_1_loc = len_inter, len_inter
        for idx, val in enumerate(intervals):
            if ni_0 > val[1]:
                continue
            elif val[0] <= ni_0 <= val[1]: # ni_0 == val[1] or ni_0 == val[0] or
                ni_0 = val[0]
                ni_0_loc = idx
                break
            else: #ni_0 < val[0]:
                ni_0_loc = idx
                break

        for i in range(ni_0_loc, len_inter):
            if ni_1 > intervals[i][1]:
                continue
            elif intervals[i][0] <= ni_1 <= intervals[i][1]: # ni_1 == intervals[i][1] or ni_1 == intervals[i][0] or
                ni_1 = intervals[i][1]
                ni_1_loc = i
                break
            else:  # ni_1 < val[0]:
                ni_1_loc = i - 1
                break

        return intervals[:ni_0_loc] + [[ni_0, ni_1]] + intervals[ni_1_loc+1:]
       
