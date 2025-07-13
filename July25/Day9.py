class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        reverse = reversed(str(x))
        if reverse ==str(x):
            return True