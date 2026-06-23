class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}
        anagramMap = {}
        
        for word in strs:
            for char in word:
                if freqMap.get(char) != None:
                    freqMap[char] += 1
                else:
                    freqMap[char] = 1

            key = ""
            sortedList = sorted(list(freqMap.items()), key = lambda x: x[0]) 
            for item in sortedList:
                key += f"{item[0]}{item[1]}"
            
            if anagramMap.get(key) != None:
                subList = anagramMap.get(key)
                subList.append(word)
            else:
                anagramMap[key] = [word]
            
            freqMap = {}

        return list(anagramMap.values())
        

