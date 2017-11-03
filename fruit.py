#!/usr/bin/env python
fruits = ['    BananA', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'DRAGON FRUIT', 'Green APple']

animals = ['monkey', 'cat    ', '     dog']

fruits = [ fruit.title().strip() for fruit in fruits ]
print("fruits:", " ".join(fruits))
print()

animals = [ animals.title().strip() for animals in animals ]
print("animals:", " ".join(animals))
print()

for num, fruits in enumerate(fruits, 1):
     print("{0} {1}".format(num, fruits))

for c in enumerate(animals):
    print("{0} {1}".format(*c))

