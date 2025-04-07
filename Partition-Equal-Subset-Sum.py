class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(nos, remaining_sum):
            if remaining_sum == 0:
                return True

            if nos == 0 or remaining_sum < 0:
                return False

            result = (dp(nos-1, remaining_sum - nums[nos-1])) or (dp(nos - 1, remaining_sum))

            return result

        total = sum(nums)
        n=len(nums)

        target = total // 2 
        if total % 2 != 0:
            return False

        return dp(n-1, target)

        


        