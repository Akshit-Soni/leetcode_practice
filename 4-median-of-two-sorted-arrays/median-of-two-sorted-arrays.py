class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # Find partition points in both arrays
            partition_x = (low + high) // 2
            partition_y = (x + y + 1) // 2 - partition_x
            
            # Get values at partition boundaries
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == x else nums1[partition_x]
            
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == y else nums2[partition_y]
            
            # Found the right partition
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # For odd total length
                if (x + y) % 2 != 0:
                    return max(max_left_x, max_left_y)
                # For even total length
                else:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            
            # Adjust search range
            elif max_left_x > min_right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1
        
        raise ValueError("Input arrays are not properly sorted")