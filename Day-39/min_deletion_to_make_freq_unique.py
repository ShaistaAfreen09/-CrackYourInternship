class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        counts = list(freq.values())
        deletions = 0
        used_freq = set()
        for count in counts:
            while count > 0 and count in used_freq:
                count -= 1
                deletions += 1
            used_freq.add(count)
        return deletions
