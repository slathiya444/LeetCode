class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        # s = set()
        # for num in nums:
        #     if num in s:
        #         return True
        #     else:
        #         s.add(num)

        # return False
        