class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftCol = 0
        rightCol = len(matrix) - 1

        while leftCol <= rightCol:
            midCol = (leftCol + rightCol) // 2

            if target == matrix[midCol][0]:
                return True
            elif target > matrix[midCol][-1]:
                leftCol = midCol + 1
            elif target < matrix[midCol][0]:
                rightCol = midCol - 1
            elif target >= matrix[midCol][0] and target <= matrix[midCol][-1]:
                leftRow = 0
                rightRow = len(matrix[midCol]) - 1

                while leftRow <= rightRow:
                    midRow = (leftRow + rightRow) // 2

                    if target == matrix[midCol][midRow]:
                        return True
                    elif target < matrix[midCol][midRow]:
                        rightRow = midRow - 1
                    else:
                        leftRow = midRow + 1
                
                return False           
        return False