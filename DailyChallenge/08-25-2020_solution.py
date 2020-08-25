class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        final_cost = [0 for i in range(days[-1] + 1)]
        set_days = set(days)
        for i in range(days[-1] + 1):
            if i not in set_days:
                final_cost[i] = final_cost[max(0, i-1)]
            else:
                final_cost[i] = min(final_cost[max(0,i-1)] + costs[0], final_cost[max(0,i-7)] + costs[1], final_cost[max(0,i-30)] + costs[2])

        return final_cost[-1]
