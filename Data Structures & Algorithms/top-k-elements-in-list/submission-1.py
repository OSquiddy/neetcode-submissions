class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if freqMap.get(num) != None:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        result = []
        for key, value in sorted(freqMap.items(), reverse=True, key=lambda x: x[1])[:k]:
            result.append(key)

        return result