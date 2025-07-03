# 3304. Find the character in String Game I
class Solution:
    def nextch(self, c: str) -> str:
        return "a" if c == "z" else chr(ord(c) + 1)

    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            next_part = "".join(self.nextch(c) for c in word)
            word += next_part
        return word[k - 1]
c =Solution()
print(c.kthCharacter(5))





