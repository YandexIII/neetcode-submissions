class Solution:
    def isPalindrome(self, s: str) -> bool:
        if ''.join(c for c in reversed(s.lower()) if c.isalnum()) == ''.join(c for c in s.lower() if c.isalnum()):
            return True
        return False