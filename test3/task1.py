import os
from functools import reduce
class InvalidLineError(Exception):
    def __init__(self, lineNumero: str) -> None:
        super().__init__(f"Hvurli topa na line {lineNumero}")
class InvalidItemError (Exception):
    def __init__(self, item: str) -> None:
        super().__init__(f"This item is wrong {item}")
class InvalidQuantityError (Exception):
    def __init__(self, num: str,item:str) -> None:
        super().__init__(f"idk {num}, {item}")
class InvalidPriceError (Exception):
    def __init__(self, price: str,item:str) -> None:
        super().__init__(f"price {price} and item {item}")
class ListFileError (Exception):
    def __init__(self, filepath: str) -> None:
        super().__init__(f"Hvurli topa na line {filepath}")

#da gi opraa vsichkite
def vankata(izrechenie:(int,str)) -> int:
    ls = izrechenie[1].split(':')
    if len(ls) != 3: raise InvalidLineError(izrechenie[0])
    if len(ls[0]) == 0 or ls[0][0]!= '-': raise InvalidLineError(izrechenie[0])
    if len(ls[0][1:])== 0 or ls[0][1:].isdigit(): raise InvalidItemError(ls[0][1:])
    if not ls[1].isdigit(): raise InvalidQuantityError(ls[1],ls[0][1:])
    if not ls[2].replace('.','0').replace('\n','0').isdigit(): raise InvalidPriceError(ls[2],ls[0][1:])
    return int(ls[1]) * float(ls[2])

def validate_list(path:str)-> int:
    try: 
        kms = open(path,'r')
    except FileNotFoundError as se:
        raise ListFileError
    info = kms.readlines()
    try: 
        l= [vankata((i,x)) for i,x in enumerate(info) ]
    except Exception as s:
        raise s
    else: return sum(l) 
    finally: kms.close()

assert abs(validate_list(os.path.join("lab04_files", "task_1", "list1.txt")) - 11.25) < 0.001

assert int(validate_list(os.path.join("lab04_files", "task_1", "list2.txt"))) == 0, "Empty files should return 0"

try:
    validate_list(os.path.join("lab04_files", "task_1", "list3.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list4.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list5.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidItemError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list6.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list7.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list8.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list9.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list10.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list11.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass