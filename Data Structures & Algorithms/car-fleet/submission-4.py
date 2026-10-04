class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        val = reversed(sorted(zip(position, speed)))
        stack = []
        # position, speed = zip(*sorted(zip(position, speed)))
        for pos, spd in val:
            stack.append((target - pos)/spd)
            
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                # stack.append((target - pos)/spd)
                stack.pop()

        return len(stack)