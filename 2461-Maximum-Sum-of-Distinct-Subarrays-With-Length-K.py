class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        mapp = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            mapp[nums[r]] += 1

            if r-l+1 > k:
                mapp[nums[l]] -= 1
                if mapp[nums[l]] == 0:
                    mapp.pop(nums[l])
                curr_sum -= nums[l]
                l += 1

            if len(mapp) == r-l+1 == k:
                res = max(res, curr_sum)


        return res
        
        
        
        