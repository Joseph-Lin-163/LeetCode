class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        local_min = prices[0]
        max_return = 0

        for i in prices:
            if local_min >= i:
                local_min = i
            else:
                max_return = max(i - local_min, max_return)

        return max_return
