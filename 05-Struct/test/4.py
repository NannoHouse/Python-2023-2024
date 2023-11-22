from ast import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr="qwertyuiop"
        sr="asdfghjkl"
        tr="zxcvbnm"
        fn = []
        for word in words:
            p=word.lower()
            if len(set(fr+p))==len(fr) or len(set(sr+p))==len(sr) or len(set(tr+p))==len(tr) :
                fn.append(word)
        return fn
