class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        combo = {}
        s2Chars = {}

        for c in t:
            combo[c] = combo.get(c, 0) + 1

        l = 0
        matches = 0
        best_start = 0
        best_length = float("inf")

        for r in range(len(s)):
            c = s[r]
            s2Chars[c] = s2Chars.get(c, 0) + 1

            # This character has just reached its required count.
            if c in combo and s2Chars[c] == combo[c]:
                matches += 1

            # We have everything needed. Try shrinking the window.
            while matches == len(combo):
                length = r - l + 1

                if length < best_length:
                    best_start = l
                    best_length = length

                # Remove the leftmost character from the window.
                left_char = s[l]
                s2Chars[left_char] -= 1

                # Did removing it leave us short of a required character?
                if (
                    left_char in combo
                    and s2Chars[left_char] < combo[left_char]
                ):
                    matches -= 1

                l += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]