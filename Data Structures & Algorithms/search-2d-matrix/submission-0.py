class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            left1 = 0
            right1 = len(matrix) - 1
            

            while left1 <= right1:
                mid1 = (left1 + right1) // 2
                if matrix[mid1][len(matrix[mid1]) -1] > target:
                    right = len(matrix[mid1]) -1
                    left = 0
                    
                    
                    while left <= right:
                        mid = (left + right)//2
                        # print(left, right, mid)
                        if matrix[mid1][mid] > target:
                            right = mid -1
                        elif matrix[mid1][mid] < target:
                            left = mid + 1
                        elif matrix[mid1][mid] == target:
                            return True
                    right1 = mid1 - 1
                elif matrix[mid1][len(matrix[mid1]) -1] < target:
                    left1 = mid1 +1
                elif matrix[mid1][len(matrix[mid1]) -1] == target:
                    return True
            return False