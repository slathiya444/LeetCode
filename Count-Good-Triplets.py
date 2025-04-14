class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        res = 0
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    if(
                        abs(arr[i] - arr[j]) <= a and
                        abs(arr[k] - arr[j]) <= b and
                        abs(arr[i] - arr[k]) <= c
                    ):
                        res += 1
        
        return res
        