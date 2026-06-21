class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-s for s in stones]
        heapq.heapify(self.maxHeap)
        print(self.maxHeap, "hello")
        print(len(self.maxHeap))
        while len(self.maxHeap) >= 2:
            x = heapq.heappop(self.maxHeap)
            y = heapq.heappop(self.maxHeap)
            print(self.maxHeap)
            if((x-y) != 0):
                print("hi")
                heapq.heappush(self.maxHeap, (x-y)) 
            print(self.maxHeap)
            if(self.maxHeap == []):
                return 0
        return -(self.maxHeap[-1])
        