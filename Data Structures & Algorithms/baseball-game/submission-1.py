class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nList=[]
        

        for i in range(len(operations)):
            if operations[i] == "C" and nList != []:
                nList.pop()

            elif operations[i] == "D" and nList != []:
                x = nList[-1]
                nList.append(x*2)
            elif operations[i] == "+" and nList != []:
                x = nList[-1]
                y = nList[-2]
                nList.append(x+y)
            
            else:
                nList.append(int(operations[i]))

        return sum(nList)