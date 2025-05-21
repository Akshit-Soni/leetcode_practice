class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = ""
        count = 0
        for i in nums:
            a += str(i)
            if a.count(str(i)) > len(nums)/2:
                return i