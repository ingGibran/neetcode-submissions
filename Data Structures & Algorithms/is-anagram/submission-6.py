class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        word_s = dict()
        word_t = dict()

        for i in range(len(s)):
            letter_s = s[i]
            if letter_s in word_s.keys():
                word_s[letter_s] += 1
            else:
                word_s[letter_s] = 1
            
            letter_t = t[i]
            if letter_t in word_t.keys():
                word_t[letter_t] += 1
            else:
                word_t[letter_t] = 1
        
        if word_s != word_t:
            return False
        
        return True