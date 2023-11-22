from ast import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        store = {}
        answer=[]
        arr1 = sorted(list(set(arr)))
        print(arr1)
        for i in range(len(arr1)):
            store[arr1[i]] = i+1
        for i in arr:
            answer.append(store[i])
        return answer
