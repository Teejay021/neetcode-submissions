class TimeMap:

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []

        self.keyStore[key].append([value,timestamp])        

    def get(self, key: str, timestamp: int) -> str:
        #where binary search is don perhaps but what about  finding the key
        #hashmap with array as values but th eproblem is storing the time stamps in order
        if key not in self.keyStore:
            return ""
        l = 0
        r = len(self.keyStore[key])-1
        res = ""
        while l <= r:
            mid = (l + r)//2
            if self.keyStore[key][mid][1] <= timestamp:
                res = self.keyStore[key][mid][0]
                l = mid + 1
            else:
                r = mid -1

            

        return res


