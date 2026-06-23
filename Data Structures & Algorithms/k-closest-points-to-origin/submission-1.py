class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [0 for x in points]
        for i in range(len(points)):
            distances[i] = (math.sqrt(points[i][0]**2 + points[i][1]**2), points[i])
        
        heapq.heapify_max(distances)

        while len(distances) > k:
            heapq.heappop_max(distances)
        return [x for _, x in distances]