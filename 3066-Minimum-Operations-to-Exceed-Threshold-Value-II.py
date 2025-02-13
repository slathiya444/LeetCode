class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0

        h = nums
        heapq.heapify(h)

        while len(h)>0 and h[0] < k:
            res += 1

            ele1 = heapq.heappop(h)
            ele2 = heapq.heappop(h)

            heapq.heappush(h, min(ele1, ele2)*2 + max(ele1, ele2))

        return res


        