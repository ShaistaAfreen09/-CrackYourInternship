class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0

        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += ' '

                result.append(''.join(line))
                line = []
                line_length = 0 

            line.append(word)
            line_length += len(word)

        result.append(' '.join(line).ljust(maxWidth)) #ljust is a method in python - , it pads the string on the right with spaces
        return result