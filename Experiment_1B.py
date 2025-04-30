# initialize empty dictionary
d = {}
d = {1: 'Poornima', 2: 'College', 3: 'Engineering'}
print(d)
# creating dictionary using dict() constructor
d1 = dict({1: 'Poornima', 2: 'College', 3: 'Enfineering'})
print(d1)
d2 = {1: 'Poornima', 'name': 'College', 3: 'Engineering'}
# Accessing an element using key
print(d2['name'])
# Accessing a element using get
print(d2.get(3))
