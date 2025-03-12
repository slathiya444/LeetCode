class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len(list(filter(lambda x: x > 0, nums))), len(list(filter(lambda x: x < 0, nums))))

        # pos, neg = 0, 0
        # for num in nums:
        #     if num > 0:
        #         pos += 1
        #     elif num < 0:
        #         neg += 1

        # return max(pos, neg)
        