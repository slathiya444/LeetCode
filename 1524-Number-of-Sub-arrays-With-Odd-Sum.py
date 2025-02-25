class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = 0
        res = 0
        odd_sum = 0
        even_sum = 0
        MOD = 10**9 + 7

        for i in arr:
            cur_sum += i

            # if the sum is odd
            if cur_sum % 2:
                res = (res + 1 + even_sum) % MOD # because odd - even  = odd
                odd_sum += 1

            else: # if sum is even
                res = (res + odd_sum) % MOD # because even - odd = odd
                even_sum += 1

        return res
        