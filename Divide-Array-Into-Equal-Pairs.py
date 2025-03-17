class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums:
            if count[num]:
                count[num] += 1
                if count[num] % 2 == 0:
                    del(count[num])
            else:
                count[num] = 1

        if count:
            return False
        else:
            return True

        