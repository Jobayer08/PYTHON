collection={1,3,4,4,5,'hello'}
print(len(collection))
set1={}#dict
print(type(set1))
set1=set()
print(type(set1))

#methods
set1.add(1)
set1.add(4)
print(set1)
set1.remove(1)
print(set1)
set1.clear()
print(set1)
set1.add('a')
set1.add('b')
set1.add('c')
set1.add('d')
print(set1.pop())

set2={1,4,5}
set3={5,6,7}
print(set3.union(set2))
print(set3.intersection(set2))

