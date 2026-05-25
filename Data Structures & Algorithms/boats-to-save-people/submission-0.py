class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
            people.sort()
            c = 0
            m = 0

            i = 0
            j = len(people)-1
            while i< j:
                
                if(people[i] + people[j] <= limit):
                    i+=1
                    j-=1
                    m+=1
                else:
                    j-=1
                    m+=1
            
            if i== j:
                m+=1
            return m
        