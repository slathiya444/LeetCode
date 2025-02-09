class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        total_pairs = 0
        good_pairs = 0
        count = collections.defaultdict(int)
        for i in range(N):
            total_pairs += i
            good_pairs += count[nums[i] - i]
            count[nums[i] - i] += 1

        return total_pairs - good_pairs



        