class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1FreqMap = {}
        s2FreqMap = {}
        for char in s1:
            s1FreqMap[char] = s1FreqMap.get(char, 0) + 1
        
        print(s1FreqMap)

        for i in range(len(s2) - len(s1) + 1):
            window = s2[i: i + len(s1)]
            print(window)
            for c in window:
                s2FreqMap[c] = s2FreqMap.get(c, 0) + 1

            flag = 1
            for k, v in s1FreqMap.items():
                if k not in s2FreqMap or s2FreqMap[k] != v:
                    flag = 0
            
            if flag == 1:
                return True

            s2FreqMap = {}
            
        return False