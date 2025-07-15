#131. Valid Word
import re
class Solution:
    def isValid(self,word):
        has_vowel = re.search(r"[aeiouAEIOU]", word)
        has_consonant = re.search(r"[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]", word)
        if len(word)>2 and re.match("^[A-Za-z0-9]+$", word) and (has_vowel) and(has_consonant):
            return True
        return False