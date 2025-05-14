class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i == len(s):
            return 0
        
        sign = 1
        if s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result