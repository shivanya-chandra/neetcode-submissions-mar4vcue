class FreqStack:

    def __init__(self):
        self.freq = {}      # val -> frequency
        self.group = {}     # frequency -> list of values with that frequency
        self.maxFreq = 0    # current highest frequency
        

    def push(self, val: int) -> None:
        # update frequency of val
        self.freq[val] = self.freq.get(val, 0) + 1
        currFreq = self.freq[val]

        # create list for this frequency if it does not exist
        if currFreq not in self.group:
            self.group[currFreq] = []

        # add val to the stack for its current frequency
        self.group[currFreq].append(val)

        # update max frequency
        self.maxFreq = max(self.maxFreq, currFreq)
        

    def pop(self) -> int:
        # pop the most recent value from the highest frequency group
        val = self.group[self.maxFreq].pop()

        # reduce its frequency
        self.freq[val] -= 1

        # if no values are left at this max frequency, reduce maxFreq
        if len(self.group[self.maxFreq]) == 0:
            self.maxFreq -= 1

        return val