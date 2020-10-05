class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # Can beat 98%
        new_num = '0b'
        for i in "{0:b}".format(N):
            if i == '0':
                new_num += '1'
            else:
                new_num += '0'
        return int(new_num, 2)


# bit operator solution below
#         if N == 0:
#             return 1

#         if N == 1:
#             return 0

#         up = 2
#         while up <= N:
#             up = up << 1

#         return up-1-N
