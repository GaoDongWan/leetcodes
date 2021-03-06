'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

//一.利用一次hashmap，查找复杂度在1~n之间，算法总体时空均为O(n)
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, x in enumerate(nums):
            a = target - x
            if a not in dict:
                dict[x] = i
            else:
                return [dict[a], i]


//二.自己写的，先排序，首位靠近，寻找结果，时间O(n)~O(nlogn)，空间O(n)
//python.sort() 是timsort的实现，在n~nlogn之间，取决于序列有序程度(小数折半插入，大数归并)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result: list[int] = []
        tnums = nums.copy()
        tnums.sort()
        i = 0
        j = len(tnums) - 1
        while (i < j):
            tsum = tnums[i] + tnums[j]
            if tsum == target:
                result.append(nums.index(tnums[i]))
                nums[nums.index(tnums[i])] = -1
                result.append(nums.index(tnums[j]))
                break;
            elif tsum > target:
                j -= 1
            else:
                i += 1
        return result
