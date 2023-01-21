'''
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
-> nums1.length == m
-> nums2.length == n
-> 0 <= m <= 1000
-> 0 <= n <= 1000
-> 1 <= m + n <= 2000
-> -106 <= nums1[i], nums2[i] <= 106

'''

import time

start = time.perf_counter()

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        array_concatened = nums1 + nums2
        array_concatened.sort()
        
        size_of_array = len(array_concatened)

        f_value_pre_medium = int((size_of_array/2) -1)
        s_value_pre_medium = int((size_of_array/2))
        print(f"f_value_pre_medium:  {f_value_pre_medium}")
        print(f"s_value_pre_medium:  {s_value_pre_medium}")


        position_f_value = array_concatened[f_value_pre_medium]
        position_s_value = array_concatened[s_value_pre_medium]
        print(f"position_f_value:  {position_f_value}")
        print(f"position_s_value:  {position_s_value}")

        medium_array = (position_f_value + position_s_value) /2
        
        return medium_array

nums1 = [1,3]
nums2 = [2]
solutionObject = Solution()
result = solutionObject.findMedianSortedArrays(nums1, nums2)

print(result)

end = time.perf_counter()
runtime = end-start
print(f"Runtime {runtime}")


