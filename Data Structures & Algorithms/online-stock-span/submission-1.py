class StockSpanner:

    def __init__(self):
        self.stack = []
        self.res = []
        

    def next(self, price: int) -> int:
        neg_count = -1
        count = 0

        if len(self.stack) == 0:
            self.stack.append(price)
            self.res.append(1)
            return 1

        while -neg_count <= len(self.stack) and self.stack[neg_count] <= price:
            count += 1
            neg_count -= 1

        self.res.append(count + 1)
        ans = count + 1

        if -neg_count <= len(self.stack) and self.stack[neg_count] > price:
            scount = 0

        self.stack.append(price)
        return ans