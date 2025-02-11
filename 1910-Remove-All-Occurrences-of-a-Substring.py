class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            part_start_at = s.index(part)

            ## update the string by removing indexes of part
            s = s[:part_start_at] + s[part_start_at + len(part) :]

        return s



# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
        # stack = []
        # part_length = len(part)

        # for char in s:
        #     stack.append(char)

        #     if len(stack) >= part_length and self._check_match(
        #         stack, part, part_length
        #     ):
        #         for _ in range(part_length):
        #             stack.pop()

        # return "".join(stack)

    def _check_match(self, stack: list, part: str, part_length: int) -> bool:
        return "".join(stack[-part_length:]) == part