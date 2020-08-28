# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        r1 = rand7()
        r2 = rand7()
        while r1 == 7:
            r1 = rand7()
        while r2 > 5:
            r2 = rand7()

        return r2 + ((r1 % 2) * 5)
