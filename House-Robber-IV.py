class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_valid(cap):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= cap:
                    i += 2
                    count += 1
                else:
                    i+=1

                if count == k:
                    break
            
            return count == k

        l, r = min(nums), max(nums)
        res = 0
        while l<=r:
            mid = (l+r)//2
            if is_valid(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1

        return res
        