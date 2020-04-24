p=10
#print(p)
print(p)
print(p)
print(p)
"""this is a docstring"""
#variables
x=4
y=5
print(x+y)
#upper case and lower case are different
"""data type"""
#numbers
i=4 #int
f= 0.4 #float
c=5j #complex
print(type(i))
print(type(f))
print(type(c))
boolean= 10>0
print(type(boolean))
#strings
name="daniya"
print(len(name))
print(name[4])
#name[4]=g this gives an error strings are imutble
#indexing and slicing
print(name[2:5])
print(name.upper())
print(name.lower())
print(name[-2])
"""list : collection of array that can be change have multi data types and can have multiple entries """
list1=["daniya","course",10 ,20 ,20,30]
print(list1)
#indexing
print(list1[2:5])
#update
list1[4]=25
print(list1)
#insert a value at a sprcifoed index no
list1.insert(6,35)
print(list1)
#append a value at the end of a list
list1.append(10)
print(list1)
list1.reverse()
print(list1)
""" DICTIONARY : unorderd , changeable and no dublicate entries are present"""
""" Key used as indexes beacause they are unique but VALUES  in the keys can be duplicated"""
#have key value pair
animalsdic={"reptiles":"sankes","mamals":"whale","amphibians":"frogs"}
print(animalsdic)
#acces values using keys as index
print(animalsdic["reptiles"])
#0r
print(animalsdic.get("mamals"))
#update a value in dictionary
animalsdic["reptiles"]="animal"
print(animalsdic)
#added new key value pair
animalsdic["new key"]="new value"
print(animalsdic)
""" TUPLE : orderd and unchangeable imutable just like string but we can have duplicate values ,when you dont want tlo change value in future"""
course=("python","django","tensor","flask",10,10,30)
print(course)
#indexing
print(course[3])
#since imutable so the are less operation
print(course.count(10))
""" SET : collection just like dic or tuple , unordered , No duplicates are present"""
learn={10,30,30,"html","css"}
print(learn)
print(learn)
#indexing
#print(learn[2]) "no indexing cux unorderd everytime it may chosse a random value"
"""range : iterating through value"""
print(list(range(0,11)))
#make list woth other data type
a={1,2,3}
b={4,5,6}
c=[a,b]
print(c)
"""type conversion"""
name="daniya"
#print(name+2) error
print(name+str(2))
