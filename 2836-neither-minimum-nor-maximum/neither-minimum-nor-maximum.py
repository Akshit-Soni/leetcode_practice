class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        '''
        minNum = 101
        maxNum = 0
        for num in nums:
            if num > maxNum:
                maxNum = num
            if num < minNum:
                minNum = num
            else:
                continue
        print(minNum, maxNum)
        for num in nums:
            if num > minNum and num < maxNum:
                return num
        '''
        nums.sort()
        return nums[1]