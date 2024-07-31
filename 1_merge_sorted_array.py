
class Solution_one:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        the logic of the solution is to compare the last element of the two arrays and put the larger one
        at the end of the first array. Then we move the pointer of the array with the larger element to the
        left and repeat the process until we reach the end of the second array. 
        Finally, if there are still elements in the second array, we copy them to the first array.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1
    
# Path: 2_merge_sorted_array.py
class Solution2:
    def marge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        The logic of the solution is to copy the elements of the second array to the end of the first array
        and then sort the first array.
        The .sort() method is a built-in method in Python that sorts the elements of a LISTS in ascending order.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1
    
nums1 = [1, 2, 3, 0, 0, 0]
print(len(nums1))