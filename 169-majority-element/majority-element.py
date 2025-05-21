class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # a = ""
        # count = 0
        # for i in nums:
        #     a += str(i)
        #     if a.count(str(i)) > len(nums)/2:
        #         return i

        major = 0
        count = 0
        max_count = 0
        if len(nums) <= 2:
            return nums[0]
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
            if count > max_count:
                max_count = count
                major = nums[i]
            if nums[i] != nums[i+1]:
                count = 0
        return major