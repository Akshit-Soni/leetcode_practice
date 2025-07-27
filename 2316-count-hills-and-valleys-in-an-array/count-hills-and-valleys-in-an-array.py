class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        num = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                num.append(nums[i])
        
        print(num)
        count = 0
        for i in range(len(num)-2):
            if num[i] < num[i+1] and num[i+1] > num[i+2]:
                count += 1
            elif num[i] > num[i+1] and num[i+1] < num[i+2]:
                count += 1
    
        return count