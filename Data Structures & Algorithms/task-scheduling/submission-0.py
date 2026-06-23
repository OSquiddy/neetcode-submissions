class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0

        task_freq_map = {}
        q = []
        for task in tasks:
            task_freq_map[task] = task_freq_map.get(task, 0) + 1
            q.append([task_freq_map[task] * n - n, task])


        ans = 0

        while q:
            heapq.heapify(q)
            print(q)
            if q[0][0] == 0:
                elem = heapq.heappop(q)
                for item in q:
                    if item[1] != elem[1]:
                        item[0] = max(0, item[0] - 1)
            else:
                for item in q:
                    item[0] = max(0, item[0] - 1)
            ans += 1

        return ans