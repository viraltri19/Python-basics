# Sets iteams are immmutable , unordered
collection = set()
collection.add(1)
collection.add(9)
collection.add(4)

print(collection)

# Union
collection2 = {4,78,90}
print(collection.union(collection2))
# Intersection
print(collection.intersection(collection2))
