class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i <= j:

            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            # elif numbers[i] < 0:
            #     i += 1
            #     continue
            # # if numbers[i] < numbers[j]:
            # #     j -= 1
            # #     continue
            # # else:
            # #     i += 1
            # #     continue

            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j -= 1
