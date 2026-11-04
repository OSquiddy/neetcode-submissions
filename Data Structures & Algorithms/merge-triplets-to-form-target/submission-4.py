class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        if len(triplets) == 1 and triplets[0] == target:
            return True

        curr = [0, 0, 0]
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            curr = [max(curr[0], triplets[i][0]), max(curr[1], triplets[i][1]), max(curr[2], triplets[i][2])]

            # print(curr)
            if curr == target:
                return True

        return False