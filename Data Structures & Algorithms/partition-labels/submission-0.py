class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        intervalMap = {}
        for idx, char in enumerate(s):
            if char not in intervalMap:
                intervalMap[char] = [idx, idx]
            else:
                intervalMap[char][1] = idx
            
        intervals = list(intervalMap.values())
        curr = intervals[0]
        for interval in intervals[1:]:
            if not curr:
                curr = interval
            if interval[0] > curr[1]:
                result.append(curr[1] - curr[0] + 1)
                curr = interval
            elif interval[0] < curr[1] and interval[1] > curr[1]:
                curr[1] = interval[1]
        result.append(curr[1] - curr[0] + 1)

        return result