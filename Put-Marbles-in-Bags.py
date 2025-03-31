class Solution:
    def applyOperations(self, nums):
        n = len(nums)

        # Step 1: Apply operations on the array
        for index in range(n - 1):
            if nums[index] == nums[index + 1] and nums[index] != 0:
                nums[index] *= 2
                nums[index + 1] = 0

        # Step 2: Shift non-zero element in place
        non_zero_index = 0
        for index in range(n):
            if nums[index]:
                nums[index], nums[non_zero_index] = nums[non_zero_index], nums[index]
                non_zero_index += 1

        return nums