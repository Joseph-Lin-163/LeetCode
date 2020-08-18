class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        loops = int(candies / ((num_people*(num_people+1)) / 2))
        # if loops > 0:   
        num_p = num_people
        while loops > 0:
            num_p += num_people
            loops = int(candies / ((num_p*(num_p+1)) / 2))

        num_p = num_p - num_people
        loops = (num_p) / num_people
        candies = candies - ((num_p*(num_p+1)) / 2)
        distr = [num_people * (((loops - 1) * (loops))/2)] * num_people
        distr = [x + (loops * (idx+1)) for idx, x in enumerate(distr)]
        count = 0
        while candies > 0:
            to_add = (loops * num_people) + (count + 1)
            distr[count] += to_add if candies > to_add else candies
            candies = candies - to_add
            count = count + 1        
            
        return distr
