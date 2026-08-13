class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += word + "`" # add word with space in front
        #print(encoded_string)
        return encoded_string

    def decode(self, s: strs) -> List[str]:
        decoded_strs = []
        word = ""
        for char in s:
            if char == "`":
                decoded_strs.append(word)
                word = ""
            else:
                word += char
                #print(word)
        return decoded_strs
