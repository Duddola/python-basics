
a_list = ["2", 3, 7.5, None]
tup= ('A', 'B', 'C', 4)
b_list= list(tup)
type(a_list)

Tup1 = 4,5
Tup2 = (23,'abc',4.56,(2,3))
Tup3 = (1,)
Tup4 = (1)
Tup5 = 1,
Tup6 = tuple('string')
type(Tup1)
type(Tup2)
type(Tup3)
type(Tup4)
type(Tup5)
type(Tup6)

my_friends={}
my_friends['Bill']=1
my_friends['Smith']=2
print(my_friends)

dict2=dict(One = "1", Two = "2", Three="3")
print(dict2)

set1 = {'a', 0, 3.14, (2,3), True, 0, 'a', 'b','c'}
set2= set() # null set
set2.add(10) # any item
set2.update('a') # any iterable
set3 = set("aabbccdd")
print(set1)
print(set2)
print(set3)

mylist=[i for i in range(2,102,2)]
print(mylist, end=' ')

mystrg= [str(i) for i in range(2,101,2)]
print(mystrg, end=' ')
type(mystrg)

tu= (23, 'abc', 4.56, (2,3), 'def')
tu[3]

