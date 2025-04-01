class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = [0] * len(questions)
        def dp(idx):

            # base case
            if idx >= len(questions):
                return 0

            if cache[idx]:
                return cache[idx]

            cache[idx] = max(
                dp(idx+1), # skip the current problem
                questions[idx][0] + dp(idx+1+questions[idx][1])
            )
            
            return cache[idx]


        return dp(0)
        