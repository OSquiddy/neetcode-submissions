class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i: [] for i in range(numCourses)}
        res = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            print(crs)
            # Cycle detected
            if crs in visiting:
                print("Crs visited already")
                return False

            # No prereq
            if crs == []:
                return True

            visiting.add(crs)
            for preq in preMap[crs]:
                if not dfs(preq):
                    return False
                else:
                    if preq not in res:
                        res.append(preq)
            visiting.remove(crs)

            return True

        for c in range(numCourses):
            if dfs(c) and c not in res:
                res.append(c)

        return res if len(res) == numCourses else []