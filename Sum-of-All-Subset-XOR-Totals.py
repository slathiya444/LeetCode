class Solution:
    def subsetXORSum(self, nums):

        def dp(idx, total):
            ## base case
            if idx == len(nums):
                return total

            return dp(idx+1, total ^ nums[idx]) + dp(idx+1, total)
            
        return dp(0, 0)