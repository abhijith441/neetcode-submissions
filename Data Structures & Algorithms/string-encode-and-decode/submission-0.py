class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + str(string)
        print("encoded string: ", encoded_string)
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_result = []
        index = 0

        while index < len(s):

            j = index
            while s[j] != '#':
                j += 1
            
            length = int(s[index: j])
            decoded_string = s[j+1: j + 1 + length]
            print("decoded string: ", decoded_string)

            decoded_result.append(decoded_string)

            index = j + 1 + length
        return decoded_result
            
            
