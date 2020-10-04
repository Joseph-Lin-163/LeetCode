class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if length == 1:
            return 1
        # intervals = sorted(sorted(intervals,key=lambda x: (x[0], x[1]), reverse=True), key=lambda x: x[0])
        intervals.sort(key=lambda x: (x[0], x[1]), reverse=True)
        intervals.sort(key=lambda x: x[0])
        count, i, j = 0, 0, 1
        # print(intervals)
        # return 0
        while i+j < length:
            while i+j < length:
                if intervals[i+j][1] <= intervals[i][1]:
                    count += 1
                    j += 1
                else:
                    break
            if j == 1:
                i += 1
            else:
                i += j
                j = 1

        return length - count
