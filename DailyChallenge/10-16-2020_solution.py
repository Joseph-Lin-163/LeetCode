class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n - 1
        while r-l >= 0:
            mid = (l + r) // 2
            # column = mid % n
            # row = mid//n
            # found = matrix[row][column]
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] > target:
                r = mid-1
            else:
                l = mid+1

        return False
