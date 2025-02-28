class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0
        left, right = 0, 0
        num_zeroes = 0

        while right < len(nums):   # While our window is in bounds
            if nums[right] == 0:    # Increase num_zeroes if the rightmost element is 0
                num_zeroes += 1

            while num_zeroes == 2:   # If our window is invalid, contract our window
                if nums[left] == 0:    
                    num_zeroes -= 1
                left += 1

            longest_sequence = max(longest_sequence, right - left + 1)   # Update our longest sequence answer
            right += 1   # Expand our window

        return longest_sequence