class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        rot_aa, rot_ab, rot_ba, rot_bb = 0,0,0,0
        neg_a, neg_b = 0, 0
        a0, b0 = A[0], B[0]
        for a, b in zip(A,B):
            if neg_a == -1 and neg_b == -1:
                break

            if neg_a != -1:
                if a != a0 and b != a0:
                    neg_a = -1
                elif a != a0:
                    rot_aa += 1
                elif b != a0:
                    rot_ab += 1

            if neg_b != -1:
                if a != b0 and b != b0:
                    neg_b = -1
                elif a != b0:
                    rot_ba += 1
                elif b != b0:
                    rot_bb += 1

        if neg_a == -1 and neg_b == -1:
            return -1
        elif neg_a == 0:
            return min(rot_aa, rot_ab)
        else:
            return min(rot_ba, rot_bb)

#         def check(x):
#             """
#             Return min number of swaps
#             if one could make all elements in A or B equal to x.
#             Else return -1.
#             """
#             rot_a, rot_b = 0, 0
#             for i in range(n):
#                 if A[i] != x and B[i] != x:
#                     return -1
#                 elif A[i] != x:
#                     rot_a += 1
#                 elif B[i] != x:
#                     rot_b += 1

#             return min(rot_a, rot_b)

#         n = len(A)
#         rotations = check(A[0])

#         if rotations != -1:
#             return rotations

#         return check(B[0])



#         mn = float('inf')
#         for k in range(1,7):
#             idxs_a = [idx for idx, val in enumerate(A) if val != k]
#             idxs_b = [idx for idx, val in enumerate(B) if val != k]

#             eq_a = True
#             eq_b = True
#             for i in idxs_a:
#                 if B[i] != k:
#                     eq_a = False
#                     break

#             for i in idxs_b:
#                 if A[i] != k:
#                     eq_b = False
#                     break

#             if eq_a and len(idxs_a) < mn:
#                 mn = len(idxs_a)

#             if eq_b and len(idxs_b) < mn:
#                 mn = len(idxs_b)

#         if mn == float('inf'):
#             return -1

#         return mn
