# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''
        Time complexity: O(log(min(m, n)))
        '''
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (x + y + 1) // 2 - partition_x
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == x else nums1[partition_x]
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == y else nums2[partition_y]
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1
        return 0.0
    
class solution2:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''
        Time complexity: O(log(min(m, n)))
        '''
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (x + y + 1) // 2 - partition_x
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == x else nums1[partition_x]
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == y else nums2[partition_y]
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1
        return 0.0
    
    # for the test case nums1 = [1,2] and nums2 = [3,4] the output should be 2.5
    
class Solution2():
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        '''
        Time complexity: O(log(min(m, n)))
        '''
        nums1[len(nums1):] = nums2[:len(nums2)]
        nums1.sort()
        
        if len(nums1) % 2 == 0:
            median_1 = (len(nums1) // 2)  
            median_2 = len(nums1) // 2 + 1
            dat1 = nums1[median_1 - 1]
            dat2 = nums1[median_2 - 1]
            return nums1
            
        else:
            median = len(nums1) // 2
            return nums1[median]
    
    # for the test case nums1 = [1,2] and nums2 = [3,4] the output should be 2.5
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))