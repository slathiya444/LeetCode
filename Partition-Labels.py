class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {} #char : last_idx
        for idx, char in enumerate(s):
            if char not in last_pos:
                last_pos[char] = -1
            last_pos[char] = idx

        size, end = 0, 0
        res = []
        for i in range(len(s)):
            end = max(end, last_pos[s[i]])
            if i != end:
                size += 1
            else:
                res.append(size+1)
                size = 0

        return res

