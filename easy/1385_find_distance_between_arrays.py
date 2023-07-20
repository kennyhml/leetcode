"""
Given two integer arrays arr1 and arr2, and the integer d, return the 
distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that 
there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
"""


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        return sum(abs(num - self.closest(arr2, num)) > d for num in arr1)

    def closest(self, arr, target) -> int:
        left, right = 0, len(arr) - 1
        closest_diff = closest_value = None
        
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return target

            diff = abs(arr[mid] - target)
            if closest_value is None or diff < closest_diff:
                closest_value = arr[mid]
                closest_diff = diff
                
            if target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return closest_value