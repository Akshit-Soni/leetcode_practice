class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_length = 1
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            # Check odd length palindromes
            left1, right1 = expand_around_center(i, i)
            length1 = right1 - left1 + 1
            
            # Check even length palindromes
            left2, right2 = expand_around_center(i, i + 1)
            length2 = right2 - left2 + 1
            
            # Update if we found a longer palindrome
            current_max_length = max(length1, length2)
            if current_max_length > max_length:
                max_length = current_max_length
                start = left1 if length1 > length2 else left2
        
        return s[start:start + max_length]
