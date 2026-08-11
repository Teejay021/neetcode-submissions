class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = 0

        word = ""
        for c in s:
            if c.isalnum():
                word += c.lower()

        backward = len(word) - 1

        while forward < backward:
            if word[forward] != word[backward]:
                return False

            forward += 1
            backward -= 1

        return True