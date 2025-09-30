from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
p = Person("Sushil", 19)
print(p.name)  # Output: Sushil
print(p.age)   # Output: 19