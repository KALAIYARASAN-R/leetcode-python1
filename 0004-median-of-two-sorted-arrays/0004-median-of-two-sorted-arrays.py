class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = [0] * (len(nums1) + len(nums2))
        j = 0

        for i in nums1:
            arr[j] = i
            j += 1

        for i in nums2:
            arr[j] = i
            j += 1

        arr.sort()

        if len(arr) % 2 == 0:
            return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        else:
            return arr[len(arr) // 2]
        