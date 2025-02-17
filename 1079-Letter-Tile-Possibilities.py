class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count_map = Counter(tiles) # char -> available count

        def backtrack():
            res = 0

            for char in count_map:
                if count_map[char] > 0:
                    count_map[char] -= 1
                    res += 1
                    res += backtrack()

                    count_map[char] += 1
                    
            return res
        
        return backtrack()
        