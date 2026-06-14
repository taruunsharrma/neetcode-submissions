class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs == []:
            return ''

        sizes = [len(size) for size in strs]
        encode_string = ','.join(str(size) for size in sizes)
        final_string = encode_string + '#'
        grouped_string = ''.join(word for word in strs)
    
        return final_string + grouped_string
        

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []

        hash_index = s.index('#')

        sizes_part = s[:hash_index]
        words_part = s[hash_index + 1:]

        sizes = [int(x) for x in sizes_part.split(',')]

        result = []
        i = 0

        for size in sizes:
            result.append(words_part[i:i+size])
            i += size

        return result