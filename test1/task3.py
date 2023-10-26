def merge(d1, d2):
    d1.update(d2)
        # updates the distionary with new elements that are given
        # if the element doesnt exits, it will be aded
        
        # other solution - get key and value from d2 and add them to d1
        #then return d1
    return d1

# Tests:

assert merge({"name": "Pesho", "year": 1999}, {"groups": ["A", "B"]}) == {"name": "Pesho", "year": 1999, "groups": ["A", "B"]}
assert merge({}, {}) == {}