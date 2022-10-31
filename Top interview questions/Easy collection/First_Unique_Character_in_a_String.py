class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 1
            else:
                seen[s[i]] += 1
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] == 1:
                return i
                break
        return -1
