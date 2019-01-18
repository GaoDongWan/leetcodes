'''
nums1:n nums2:m
题目意思见标题，要求O(log(n+m))
'''
//一 符合要求的
// https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = int(half_len - i)
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

//二 运行最快的 O(n~nlogn)?
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        mid = (len(nums) - 1) / 2.0
        if mid == int(mid):
            return nums[int(mid)]
        else:
            return (nums[int(mid)] + nums[int(mid) + 1]) / 2.0
            
//三 自己写的，类似归并过程，只循环到中间次数  O((n+m)/2)
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        i = 0
        j = 0
        k = 0
        temp = 0
        result = 0.0
        length = nums1.__len__() + nums2.__len__()
        while k < float(length / 2):
            if i == nums1.__len__():
                temp = nums2[j]
                j += 1
                k += 1
                continue
            if j == nums2.__len__():
                temp = nums1[i]
                i += 1
                k += 1
                continue
            if nums1[i] < nums2[j]:
                temp = nums1[i]
                i += 1
            else:
                temp = nums2[j]
                j += 1
            k += 1

        if length % 2 == 0 and i < nums1.__len__() and j < nums2.__len__():
            result = (temp + min(nums1[i], nums2[j])) / 2
        elif length % 2 == 0 and i == nums1.__len__():
            result = (temp + nums2[j]) / 2
        elif length % 2 == 0 and j == nums2.__len__():
            result = (temp + nums1[i]) / 2
        else:
            result = temp
        return result
   
