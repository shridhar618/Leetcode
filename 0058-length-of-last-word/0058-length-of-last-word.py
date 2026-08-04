class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        s = s[::-1]
        count = 0
        for ch in s:
            if ch == " ":
                break
            count += 1
        return count
        