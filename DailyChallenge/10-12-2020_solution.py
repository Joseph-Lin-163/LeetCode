class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        len_a, len_b = len(A), len(B)
        if len_a != len_b:
            return False

        matches = []
        for i in range(len_a):
            if A[i] == B[i]:
                continue
            matches.append((A[i],B[i]))

        if len(matches) == 2:
            m0, m1 = matches[0], matches[1]
            if m0[0] == m1[1] and m0[1] == m1[0]:
                return True
            else:
                return False
        elif len(matches) == 0:
            if len(set(A)) < len_a:
                return True
            else:
                return False
        else:
            return False
        
