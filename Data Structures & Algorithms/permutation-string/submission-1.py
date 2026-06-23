class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map = {}
        for char in s1:
            if map.get(char):
                map[char] += 1
            else:
                map[char] = 1

        for idx in range(0, len(s2)):
            substring = s2[idx:idx+len(s1)]
            subMap = {}
            for char in substring:
                if subMap.get(char):
                    subMap[char] += 1
                else:
                    subMap[char] = 1
            print(subMap, map)
            if len(map) != len(subMap):
                continue
            flag = True
            for char in substring:
                if subMap.get(char) != map.get(char):
                    flag = False
            if flag:
                return flag

                    
        return False