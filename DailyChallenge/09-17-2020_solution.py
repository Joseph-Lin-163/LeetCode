class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        loc = [0,0]
        l_count, r_count = 0, 0
        for i in instructions:
            if i == 'G':
                turn = (l_count % 4) - (r_count % 4)
                # if turn > 0: left
                # if turn == 0: forward
                # if turn < 0: right
                # 1 is left, 2 is down, 3 is right, -1 is right, -2 is down, -3 is left
                if turn == 0:
                    loc[1] += 1
                elif turn == 1 or turn == -3:
                    loc[0] -= 1
                elif turn == 2 or turn == -2:
                    loc[1] -= 1
                else:
                    loc[0] += 1
            elif i == 'L':
                l_count += 1
            else:
                r_count += 1

        turn = (l_count % 4) - (r_count % 4)
        return loc == [0,0] or (abs(turn) != 0)
