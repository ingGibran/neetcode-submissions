class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s = s.strip().lower().replace(' ', '')

        clean_s = ""

        for char in s:
            if char.isalnum():
                clean_s = clean_s + "" + char
        
        if clean_s[::-1] == clean_s:
            return True
        
        return False