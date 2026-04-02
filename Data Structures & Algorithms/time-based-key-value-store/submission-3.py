class TimeMap:

    def __init__(self):
        self.cmap = {}
        self.bvalues = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.cmap:
            self.cmap[key][timestamp] = value
            self.bvalues[key].append(timestamp)
        else:
            self.cmap[key] = {}
            self.cmap[key][timestamp] = value
            self.bvalues[key] = []
            self.bvalues[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.cmap:
            if timestamp in self.cmap[key]:
                return self.cmap[key][timestamp]
            else:
                target = timestamp
                arr = self.bvalues[key]
                l = 0
                r = len(arr) - 1
                ret = arr[l]
                while l <= r:
                    m = (l + r) // 2
                    if arr[m] < timestamp:
                        ret = arr[m]
                    if target > arr[m]:
                        l = m + 1
                    else:
                        r = m - 1
                if ret > timestamp:
                    return ""
                return self.cmap[key][ret]
        else:
            return ""
