class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        perms_sorted = sorted([(x[0]*10 + x[1], x[2]*10+x[3]) for x in itertools.permutations(A,4) if x[0]*10 + x[1] < 24 and x[2]*10+x[3] < 60], key=itemgetter(0))
        if not perms_sorted:
            return ""
        max_hour = perms_sorted[-1][0]
        max_minutes = max([x[1] for x in perms_sorted if x[0] == max_hour])
        if max_minutes < 9:
            max_minutes = "0{}".format(max_minutes)
        max_hour = perms_sorted[-1][0] if perms_sorted[-1][0] > 9 else "0{}".format(perms_sorted[-1][0])

        return "{}:{}".format(max_hour, max_minutes)


        
