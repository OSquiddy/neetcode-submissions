class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt((x1)**2 + (y1)**2), (x1, y1)) for x1, y1 in points]
        heapq.heapify(distances)

        res = []
        for i in range(k):
            dist, points = heapq.heappop(distances)
            res.append(points)
        
        return res