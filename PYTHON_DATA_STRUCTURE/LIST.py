#LIST DS
list=[1,2,3,"edureka"]
print(list)
list[1]=5 #list can be changed
#add data elements
#append ,extend and insert
list.append(2)
print(list)
list.append((2,0))
print(list)
#list.extend(2)
list.extend((2,0))
print(list)
list.insert(3,"example")
print(list)
#DELETE data elements
#DEL,POP,REMOVE
del list[3]
print(list)

p_element=list.pop(4)
print(p_element)
print("after pop")

print(list)
print("after remove")
list.remove(2)
print(list)
#slicing
print(list[:])
print(list[:2])
print(list[:4:2])
print(list[::-1])
#LISR FUMCTIONS
list1=[1,3,6,8,2,4,0]
print(sorted(list1))
print(list1)
#change oeiginal data
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
print(list1.index(8))
print(list1.count(8))
