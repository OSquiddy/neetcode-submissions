from copy import deepcopy
class MedianFinder:

    def __init__(self):
        self.q = deque()
        self.q = []

    def addNum(self, num: int) -> None:
        if self.q:
            # if num >= self.q[-1]:
            #     self.q.append(num)
            # elif num <= self.q[0]:
            #     self.q.appendleft(num)
            heapq.heappush(self.q, num)
        else:
            self.q.append(num)
        

    def findMedian(self) -> float:
        res = []
        copyOfQ = deepcopy(self.q)
        while copyOfQ:
            heapq.heapify(copyOfQ)
            res.append(heapq.heappop(copyOfQ))

        if len(res) % 2 == 0:
            idx = len(res) // 2
            print(idx)
            return (res[idx] + res[idx - 1]) / 2
        else:
            return res[len(res) // 2]
        