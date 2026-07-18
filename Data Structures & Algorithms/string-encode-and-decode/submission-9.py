class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for s in strs:
            word_length = len(s)
            colon = ":"
            word_length = f"{word_length}{colon}"
            res_word = f"{word_length}{s}"
            encode_string += res_word   
        return encode_string     
    def decode(self, s: str) -> List[str]:
        decode_string = []
        word_len , i = 0 , 0
        while i < len(s):
            if s[i].isdigit():
                word_len = word_len * 10 + int(s[i])
                i += 1
            else:
                broken_word = s[i+1:i+1+word_len]
                decode_string.append(broken_word)
                i = i+1 + word_len
                word_len = 0
        return decode_string
