class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def find_atleast_k(k):
            res = 0
            vovel = defaultdict(int)
            non_vovel = 0
            left = 0

            for right in range(len(word)):
                if word[right] in "aeiou":
                    vovel[word[right]] += 1
                else:
                    non_vovel += 1

                while len(vovel) == 5 and non_vovel >= k:
                    res += (len(word) - right)

                    # move the left pointer to next of left
                    if word[left] in "aeiou":
                        vovel[word[left]] -= 1

                    else:
                        non_vovel -= 1

                    if vovel[word[left]] == 0:
                        vovel.pop(word[left])

                    left += 1
            
            return res

        return find_atleast_k(k) - find_atleast_k(k+1)
        