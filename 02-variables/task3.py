def is_valid_UCN(ucn, should_bypass_checksum=False):
    weight = [2,4,8,5,10,9,7,3,6]
    month= ord(ucn[2])* 10 + ord(ucn[3])
    if (month >=1 and month <=12) or (month >= 41 and month <= 52): 
        print("broke month")
        return False
    if should_bypass_checksum:
        return True
    count =0
    sum = 0
    for char in ucn:
        sum =sum + weight[count] * (ord(char) - 48)
        print(sum, ord(char) - 48, count)
        count= count + 1
    sum =sum - (sum//11) * 11
    if sum == ucn[9]: return True
    return False
print(is_valid_UCN("6101057509") == True)
# print(is_valid_UCN("6101057500", shoul_bypass_checksum=True) == True)
# print(is_valid_UCN("6101057500") == False)
# print(is_valid_UCN("6913136669") == False)