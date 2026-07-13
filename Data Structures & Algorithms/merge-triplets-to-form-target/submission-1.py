class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = [False, False,False]
        #collecting the indices which contain the valid combinations
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            if triplets[i][0] == target[0]:
                valid[0] = True
            if triplets[i][1] == target[1]:
                valid[1] = True
            if triplets[i][2] == target[2]:
                valid[2] = True

        return all(valid)
            
            
       
        
        

        