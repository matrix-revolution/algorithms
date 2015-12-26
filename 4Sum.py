__author__ = 'rajeevkumar'
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
'''

class Solution:
    def TwoSum(self, nums, leftStartIndex, rightEndIndex, target):
        output = []
        if leftStartIndex > rightEndIndex:
            return output
        while leftStartIndex <= rightEndIndex:
            if nums[leftStartIndex] + nums[rightEndIndex] == target:
                output.append((nums[leftStartIndex], nums[rightEndIndex]))
                leftStartIndex += 1
                rightEndIndex -= 1
            elif nums[leftStartIndex] + nums[rightEndIndex] > target:
                rightEndIndex -= 1
            else:
                leftStartIndex += 1
        return output

    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        output = []
        for i in range(len(nums) - 3):
            for j in range(i+1, range(len(nums) - 2)):
                twoSumTuple = TwoSum(self, nums, j+1, len(nums)-1)
                if len(twoSumTuple) != 0:
                    for it in twoSumTuple:
                        output.insert((nums[i], nums[j] + it))

        return output
