class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        # print(nums1)
        nums1.sort()

        if len(nums1)%2 == 0:
            mid_index = len(nums1)//2
            # print(mid_index)
            return (nums1[mid_index] + nums1[mid_index-1])/2
        else:
            mid_index = len(nums1)//2
            return nums1[mid_index]