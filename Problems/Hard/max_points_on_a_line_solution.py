class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        slopes = {}
        max_points = 0
        for i in range(len(points)):
            slopes[i] = {}
            slopes[i]['self'] = 0
            num_self = 1
            if max_points > len(points) - i:
                break
            for j in range(i+1, len(points)):
                if (points[i][0] - points[j][0]) == 0 and (points[i][1] - points[j][1]) == 0:
                    num_self += 1
                    continue
                elif (points[i][0] - points[j][0]) == 0:
                    slope = "inf"
                else:
                    dy, dx = (points[i][1] - points[j][1]), (points[i][0] - points[j][0])
                    if dx < 0:
                        dy, dx = -dy, -dx
                    gcd = math.gcd(dy, dx)
                    slope = (dy/gcd, dx/gcd)

                slopes[i][slope] = slopes[i].get(slope, 0) + 1

            for slope in slopes[i]:
                max_points = max(max_points, slopes[i][slope] + num_self)

        # for slope in slopes:
        #     print("{}: {}".format(slope, slopes[slope]))

        return max_points
