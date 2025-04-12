class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out_list = []
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    out_list.append(i)
                    out_list.append(j)
                    return out_list