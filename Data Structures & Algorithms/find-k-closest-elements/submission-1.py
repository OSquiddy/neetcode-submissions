class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distCount = 0
        l = 0
        result = []

        for r in range(k):
            distCount += abs(arr[r] - x)
            
        result = [x for x in arr[l:r+1]]
        minCount = distCount

        print(minCount)
        
        for r in range(k, len(arr)):
            distCount += abs(arr[r] - x)
            distCount -= abs(arr[l] - x)
            l += 1
            if distCount < minCount:
                print(distCount, minCount)
                result = [x for x in arr[l:r+1]]
                minCount = distCount
        
        return result
            