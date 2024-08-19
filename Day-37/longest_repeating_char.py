class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        max_length = 0
        char_count = {}
        while end < len(s):
            char_end = s[end]
            char_count[char_end] = char_count.get(char_end, 0) + 1
            max_freq = max(char_count.values())
            if end - start + 1 - max_freq > k:
                char_start = s[start]
                char_count[char_start] -= 1
                start += 1     
            max_length = max(max_length, end - start + 1)
            end += 1
        return max_length
