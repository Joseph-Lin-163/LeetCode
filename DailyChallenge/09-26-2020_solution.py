class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time_poisoned = 0
        len_series = len(timeSeries)
        idx = 0
        while idx < len_series:
            start, end = timeSeries[idx], timeSeries[idx] + duration
            while idx + 1 < len_series and timeSeries[idx+1] <= end:
                idx += 1
                end = timeSeries[idx] + duration
            time_poisoned += (end - start)
            idx += 1


        return time_poisoned
