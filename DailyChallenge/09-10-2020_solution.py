class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        b_helper = {}
        rest = []
        for x, y in zip(secret, guess):
            if x == y:
                a += 1
            else:
                rest.append(x)
                b_helper[y] = b_helper.get(y, 0) + 1

        for i in rest:
            if i in b_helper and b_helper[i] != 0:
                b += 1
                b_helper[i] -= 1

        return "{}A{}B".format(a, b)
                
