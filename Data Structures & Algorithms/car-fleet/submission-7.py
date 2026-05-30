class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fArr = []
        fleet = []
        c = 0
        a = []
        k = 0
        p = []
        for i in range(len(position)):
            

            fArr.append([position[i], speed[i]])



        fArr.sort()
    


        curFleet = 0
        prevFleet = 0
        for i in range(len(fArr) - 1, -1, -1):
            
            x = (target-fArr[i][0])/fArr[i][1]
            curFleet = x
        
            if(curFleet > prevFleet):
            
                c += 1
                prevFleet = curFleet
        
            fleet.append(x)
        




        return c
