class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pre_max = nums[0]
        max_diff = 0
        res = 0

        for k in range(1, len(nums)):
            res = max(res, max_diff*nums[k])
            pre_max = max(pre_max, nums[k])
            max_diff = max(max_diff, pre_max-nums[k])
        return res
        