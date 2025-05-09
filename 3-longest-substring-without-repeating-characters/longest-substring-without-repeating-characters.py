class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        char_index = {}
        start = 0
        max_length = 0
        
        for end, char in enumerate(s):
            if char in char_index and start <= char_index[char]:
                start = char_index[char] + 1
            else:
                max_length = max(max_length, end - start + 1)
            
            char_index[char] = end
        
        return max_length

