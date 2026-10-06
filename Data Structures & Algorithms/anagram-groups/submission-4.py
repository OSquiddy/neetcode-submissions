class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = {}

        for s in strs:
            arr = [0] * 26
            for char in s:
                idx = ord(char) - 97
                # print(idx)
                arr[idx] += 1
            
            if tuple(arr) not in charMap:
                charMap[tuple(arr)] = [s]
            else:
                charMap[tuple(arr)].append(s)
        
        return [x for x in charMap.values()]

