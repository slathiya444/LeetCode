class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        if len(list(filter(lambda k: k%2!=0, count.values()))):
            return False
        return True