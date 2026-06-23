class MedianFinder:

    def __init__(self):
        self.q = []

    def addNum(self, num: int) -> None:
        if self.q:
            heapq.heappush(self.q, num)
        else:
            self.q.append(num)
        

    def findMedian(self) -> float:
        res = []
        copyOfQ = [x for x in self.q]
        while copyOfQ:
            heapq.heapify(copyOfQ)
            res.append(heapq.heappop(copyOfQ))

        if len(res) % 2 == 0:
            idx = len(res) // 2
            print(idx)
            return (res[idx] + res[idx - 1]) / 2
        else:
            return res[len(res) // 2]
        