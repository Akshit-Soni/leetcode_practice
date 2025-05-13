class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x > 0:
            digit = x % 10
            
            if reversed_num > 214748364 or (reversed_num == 214748364 and digit > 7):
                return 0
                
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return sign * reversed_num