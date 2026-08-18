class NumMatrix:
    #start at the first index
    #end at the second lst
    #start range and end range
    #but that would be brute force
    #what would be the optimizatiom?

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                s += self.matrix[i][j]
        return s
                
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)