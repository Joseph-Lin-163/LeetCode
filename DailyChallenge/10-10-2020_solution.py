class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
#         if not points:
#             return 0

#         points.sort(key=lambda x: (x[0], x[1]))
#         count = 0
#         minimum = points[0][1]
#         tmp = 0
#         for pt in points:
#             tmp += 1

#             if minimum > pt[1]:
#                 minimum = pt[1]

#             if minimum >= pt[0]:
#                 continue
#             else:
#                 count += 1
#                 minimum = points[tmp-1][1]

#         return count + 1
        end, arrow = float('-inf'), 0
        print(sorted(points, key=lambda x: x[1]))
        for start_, end_ in sorted(points, key=lambda x: x[1]):
            if start_ > end:
                end = end_
                arrow += 1
        return arrow
