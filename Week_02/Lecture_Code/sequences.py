# Data Structures in python
"""
List: Sequence of multiple values
Tuple: Sequence of immutable values
Set: Collection of unique values
Dict: Collection of Key-Value pairs
"""

# List
names = ["Harry" ,"Ron", "Hermoine", "Ginny"];

names.append("Draco")
names.sort()

print(names)

# Set
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(3)

s.remove(3)

print(s)

# Dictionary
houses = {
    "Harry": "Gryffindor",
    "Draco": "Slytherin"
}

houses["Hermoine"] = "Gryffindor"

print(houses["Harry"])
print(houses["Hermoine"])

# Tuple
coordinate = (10.0, 20.0)
print(coordinate[0])
print(coordinate[1])

# Using the length function 'len()'
print(f"The list has {len(names)} number of elements. ");
print(f"The set has {len(s)} number of elements. ");
print(f"The dictionary has {len(houses)} number of elements. ");
print(f"The tuple has {len(coordinate)} number of elements. ");