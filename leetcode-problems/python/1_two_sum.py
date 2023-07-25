class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        array_length = len(nums)
        for i in range(array_length):
            for j in range(i + 1, array_length):
                if nums[i] + nums[j] == target:
                    return [i, j]
