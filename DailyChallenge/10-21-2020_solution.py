class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Original solution was faster
        ret = deque([asteroids[0]])
        for i in range(1, len(asteroids)):
            if not ret:
                ret.append(asteroids[i])
                continue

            if asteroids[i] < 0:
                if ret[-1] < 0:
                    ret.append(asteroids[i])
                    continue
                else:
                    aster = asteroids[i] * -1
                    for j in range(len(ret) - 1, -2, -1):
                        if j == -1:
                            ret = [aster*-1]
                            break
                        if ret[j] > 0:
                            if ret[j] > aster:
                                # ret = ret[:j+1]
                                break
                            elif ret[j] == aster:
                                # ret = ret[:j]
                                ret.pop()
                                break
                            else:
                                ret.pop()
                                continue
                        else:
                            # ret = ret[:j+1] + [aster*-1]
                            ret.append(aster*-1)
                            break
            else:
                ret.append(asteroids[i])

        return ret

#         Other solution
#         stack = deque([])

#         for asteroid in asteroids:
#             appendAsteroid = True
#             while stack and asteroid < 0 < stack[-1]:
#                 # If incoming asteroid weighs more
#                 if abs(asteroid) > stack[-1]:
#                     stack.pop()
#                     continue
#                 elif abs(asteroid) == stack[-1]:
#                     stack.pop()
#                 appendAsteroid = False
#                 break
#             if appendAsteroid:
#                 stack.append(asteroid)

#         return stack
