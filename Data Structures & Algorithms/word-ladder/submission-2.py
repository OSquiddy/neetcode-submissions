class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        totalWords = [beginWord] + wordList + [endWord]
        adj = {i: [] for i in totalWords}

        for i in range(len(totalWords)):
            for j in range(i + 1, len(totalWords)):
                count = 0
                for k in range(len(beginWord)):
                    if totalWords[i][k] != totalWords[j][k]:
                        count += 1
                if count == 1:
                    if totalWords[j] not in adj[totalWords[i]]:
                        adj[totalWords[i]].append(totalWords[j])
                    if totalWords[i] not in adj[totalWords[j]]:
                        adj[totalWords[j]].append(totalWords[i])
        
        visit = set([beginWord])
        q = deque([beginWord])
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord and endWord in wordList:
                    return count
        
                for w in adj[word]:
                    if w != word and w not in visit:
                        q.append(w)
            count += 1

        return 0