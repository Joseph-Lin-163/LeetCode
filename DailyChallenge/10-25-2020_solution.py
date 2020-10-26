class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # The idea is to fill up dp with the possibilities that can be played
        # If we find such an event where i + candidate == remaining rocks, Alice wins, otherwise loses
        dp = [0] * (n+1)
        candidates = []
        for j in range(1, int(math.sqrt(n))+1):
            candidates.append(j*j)
        for i in range(n):
            if not dp[i]:
                for can in candidates:
                    # print('i+can: {} + {} = {}'.format(i,can,i+can))
                    if i + can < n:
                        dp[i+can] = 1
                    elif i + can == n:
                        return True

            # print(i)
            # print(dp)
            # print(candidates)
        return False
