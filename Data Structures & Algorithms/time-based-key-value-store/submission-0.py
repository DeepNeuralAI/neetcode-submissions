class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.data[key]
        l = 0
        r = len(self.data[key]) - 1

        while l <= r:
            m = (l + r) // 2

            candidate = values[m]

            if candidate[0] > timestamp:
                r = m - 1
            else:
                res = candidate[1]
                l = m + 1
        
        return res
        
