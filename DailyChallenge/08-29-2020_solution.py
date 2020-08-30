class Solution:
    def flip(self, A, ind, ind2):
        A = A[ind::-1] + A[ind+1:]
        return A[ind2::-1] + A[ind2+1:]

    def pancakeSort(self, A):
            sorted_A = sorted(A)
            pancake_order = []
            for i in range(len(sorted_A)-1, -1, -1):
                to_app = A.index(sorted_A[i])
                pancake_order.extend([to_app+1, i+1])
                A = self.flip(A, to_app, i)

            return pancake_order
