from ast import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numb = ""
        for n in digits:
            numb += str(n)
        temp = str(int(numb) + 1)

        return [int(temp[i]) for i in range(len(temp))]
    
    