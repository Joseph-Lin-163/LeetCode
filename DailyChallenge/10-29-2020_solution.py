class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_zeros = 0
        count = 0

        if seats[0] == 0:
            for n in seats:
                if n == 0:
                    count += 1
                else:
                    break
            max_zeros = count * 2
            count = 0

        for n in seats:
            if n == 0:
                count += 1
            else:
                if count > max_zeros:
                    max_zeros = count
                count = 0

        if count*2 > max_zeros:
            return count

        return (max_zeros+1) // 2
        
