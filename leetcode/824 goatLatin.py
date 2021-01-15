# Source: https://leetcode.com/problems/goat-latin/
# Topic: String Manipulation
# Time Complexity: O(n)

class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        for i in range(len(words)):
            if words[i][0] not in "aeiouAEIOU":
                words[i] = words[i][1:] + words[i][0]
            words[i] = words[i] + "ma" + "a" * (i+1)
        return  " ".join(words)
