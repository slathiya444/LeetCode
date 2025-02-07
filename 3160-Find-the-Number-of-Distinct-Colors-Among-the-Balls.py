class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color_map = {}
        color_map = {}
        res = []
        for ball, color in queries:
            if ball in ball_color_map:
                color_map[ball_color_map[ball]] -= 1

                if color_map[ball_color_map[ball]] == 0:
                    del color_map[ball_color_map[ball]]

            ball_color_map[ball] = color
            color_map[color] = color_map.get(color, 0) + 1
            res.append(len(color_map))

        return res
        


        