class Solution:
    def smallestNumber(self, pattern: str) -> str:

        res, stack = [], []

        for i in range(len(pattern) + 1): # 0-indexed

            stack.append(i+1) # need results starting from 1

            # now if 'I' comes, pop from stack, untill it is empty
            while stack and (i == len(pattern) or pattern[i] == 'I'):
                res.append(str(stack.pop()))

        return "".join(res)
        