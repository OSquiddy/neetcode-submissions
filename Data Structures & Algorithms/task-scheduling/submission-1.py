class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Iterate through the tasks
        # When you come across a new one, execute it - Track in dict or set?
        # If it already exists, check the time remaining?
            # If it's greater than in the tracker, continue
            # If it's less, add to list, update the minCycles count
        count = Counter(tasks)
        print(count)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        
