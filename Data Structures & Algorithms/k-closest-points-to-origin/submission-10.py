import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a=[]
        for x in points:
            b = math.sqrt(x[0]*x[0] + x[1] * x[1])
            a.append([x[0],x[1],b])
        self.maxHeap = [[-x[2], x[1], x[0]] for x in a]
        heapq.heapify(self.maxHeap)
        print(self.maxHeap)
        while len(self.maxHeap) > k:
            heapq.heappop(self.maxHeap)
        
        return [[x[2], x[1]] for x in self.maxHeap]
        