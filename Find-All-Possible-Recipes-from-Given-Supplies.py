class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        can_cook = {s:True for s in supplies}
        recipe_index = {r:i for i, r in enumerate(recipes)}

        def dfs(recipe):
            if recipe in can_cook:
                return can_cook[recipe]

            if recipe not in recipe_index:
                return False

            can_cook[recipe] = False
            for nei in ingredients[recipe_index[recipe]]:
                if not dfs(nei):
                    return False
                
            can_cook[recipe] = True
            return can_cook[recipe]

        return [r for r in recipes if dfs(r)]

        