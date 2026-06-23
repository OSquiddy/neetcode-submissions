class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n):
            digits[n - 1 - i] = digits[n - 1 - i] if carry == 0 else digits[n - 1 - i] + 1
            if digits[n - 1 - i] == 10:
                digits[n - 1 - i] = 0
                carry = 1
            else:
                carry = 0
        
        
        return [1] + digits if digits[0] == 0 else digits