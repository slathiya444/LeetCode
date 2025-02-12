class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def digit_sum(x):
            r = 0
            while x > 0:
                r += x % 10
                x //= 10
            return r

        sum_to_digit_map = {}
        res = -1
        for digit in nums:
            sum_of_digits = digit_sum(digit)
            if sum_of_digits in sum_to_digit_map:
                res = max(res, sum_to_digit_map[sum_of_digits] + digit)
                sum_to_digit_map[sum_of_digits] = max(sum_to_digit_map[sum_of_digits], digit)
            else:
                sum_to_digit_map[sum_of_digits] = digit

        return res
        