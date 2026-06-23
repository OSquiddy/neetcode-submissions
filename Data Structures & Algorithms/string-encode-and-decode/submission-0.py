class Solution:

    def encode(self, strs: List[str]) -> str:
        key = 2
        alpha = "abcdefghijklmnopqrstuvwxyz"
        encodedString = ""
        for word in strs:
            for char in word:
                char = ord(char) + key
                char = chr(char)
                encodedString += char
            encodedString += "$*/$"
        return encodedString

    def decode(self, s: str) -> List[str]:
        key = 2
        words = s.split("$*/$")
        result = []
        for word in words:
            decodedString = ""
            for char in word:
                char = ord(char) - key
                char = chr(char)
                decodedString += char
            result.append(decodedString)
        return result[:len(result) - 1]

