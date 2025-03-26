class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total = 0
        for r in grid:
            for c in r:
                total += c
                if c % x != grid[0][0] % x:
                    return -1
        
        nums = sorted([col for row in grid for col in row])

        prefix = 0
        res = float("inf")
        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix
            cost_right = total - prefix - (nums[i] * (len(nums) - i))
            operations = (cost_left + cost_right) // x
            res = min(res, operations)
            prefix += nums[i]

        return res

        