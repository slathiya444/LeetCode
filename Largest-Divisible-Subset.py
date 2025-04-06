class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()

        @lru_cache(None)
        def dp(curr_idx, prev):
            ## base cases
            if curr_idx == N:
                return []

            ## recurance relation
            # do not include current number and move to next
            skip_res = dp(curr_idx+1, prev)
            # include current number
            if nums[curr_idx]%prev == 0:
                include_res = [nums[curr_idx]] + dp(curr_idx+1, nums[curr_idx])
                # skip_res = skip_res if len(skip_res) > len(include_res) else include_res
                skip_res = include_res if len(include_res) > len(skip_res) else skip_res
            
            return skip_res

        return dp(0, 1)