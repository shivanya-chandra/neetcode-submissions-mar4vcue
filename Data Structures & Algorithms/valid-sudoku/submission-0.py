class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #read 3x3 at once and make a dict, if the element
        #is already in the dict, then return false
        #reset the dict after every 3x3
        #figure out how to move along the 3x3

        #two for loops inside a function with
        #changing bounds
        
            

        def readThree(m,n):
            dic = {}
            for i in range(m, m + 3):
                for j in range(n, n +3):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in dic:
                        return False
                    dic[board[i][j]] =  1
            return True
        
        for i in range(9):
            row = {}
            col = {}
            for j in range(9):
                colVal = board[i][j]
                rowVal = board[j][i]
                if board[i][j] != ".":
                    if colVal in col:
                        return False
                col[colVal] =  1

                if board[j][i] != ".":
                    if rowVal in row:
                        return False
                row[rowVal] =  1
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not readThree(i,j):
                    return False



        return True
    

        