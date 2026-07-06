class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = []
        windowSum = 0

        l = 0
        for i in range(k):
            windowSum += arr[i]
            avg = windowSum / k
        
        if avg >= threshold:
            res.append(arr[l:k])
        
        for r in range(k, len(arr)):
            windowSum += arr[r]
            windowSum -= arr[l]
            l += 1
            avg = windowSum / k
            if avg >= threshold:
                res.append(arr[l:r+1])
        
        return len(res)