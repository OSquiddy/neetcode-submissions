class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timeMap.get(key):
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = []
            self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
            # Find the first timestamp that is less than the given timestamp
            result = ""
            array = self.timeMap.get(key, [])

            lower = 0
            upper = len(array) - 1

            while lower <= upper:
                mid = (upper + lower) // 2

                if array[mid][0] <= timestamp:
                    result = array[mid][1]
                    lower = mid + 1
                else:
                    upper = mid - 1

            return result
