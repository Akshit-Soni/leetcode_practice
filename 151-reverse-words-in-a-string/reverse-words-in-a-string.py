class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        a = s.split()
        a = a[::-1]
        b = ""
        for i in a:
            b += i
            b += " "
        
        return b.strip()