class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        result = 0
        is_negative = x < 0
        x = abs(x)
        
        while x:
            digit = x % 10
            
            # Check for potential overflow
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > 7):
                return 0
                
            result = result * 10 + digit
            x //= 10
        
        return -result if is_negative else result