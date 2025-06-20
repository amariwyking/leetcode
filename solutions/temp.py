from typing import List


# class Solution:
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    ret = []

    def matrixIsEmpty():
        for row in matrix:
            if row:
                return False
                print(f"Matrix isn't empty: {row}")
        return True

    def traverseRight():
        for i in range(len(matrix)):
            if matrix[i]:
                while matrix[i]:
                    buffer = matrix[i]

            matrix[i] = []

            return matrix[i]

    while not matrixIsEmpty():
        ret += traverseRight()
        break

    return ret


# spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print([2, 3, 4, 5, 6][::-1])