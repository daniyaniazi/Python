import array
"""Array   data structure, ordered series means at particular address ,have indexing starting from 0  ."""
"""python list and array array can store only single data type values but list can store int float str etc """
"""operation are different"""

#use alias name import array as arr :a=arr.array('i',[1,2,3,4,5])
#or using star from array import * : a=array(i',[1,2,3,4,5])
# * means all that is presdnt in module
a=array.array('i',[1,2,3,4,5])
print(a)
"""access index value"""
print(a[2])
"""basic array operation"""
#array are mutalbe changable
"""finding lenght"""
print(len(a))
"""adding elemets"""
#append : add a single element at the end
#extrnd: more than one element at the end
#insert : add elemnt at a specific position
a.append(8)
print(a)
a.extend([9,10])
print(a)
a.insert(4,56)
print(a)
""" rmoving elements"""
#pop :remove and return may take index or remove last
#remove : only reyurn  take element as parameter
print("pop at last",a.pop(), "removed")
print("pop at index 3 i,e:",a.pop(3), "removed")
print(a)
a.remove(56)
print("56 removed ",a)

"""array concatrnation + """
#array have same type
a1=array.array("d",[1,2,3,4,5])
a2=array.array("d",[6,7,8,9,10])
a3=array.array("d") #empty array
a3=a1+a2
print (" concatenation of a1 and a2 :",a3)
""" SLICING : fetching a part of an array"""
print(a3[0:3]) #3 excluded

print(a3[0:-2])
# reverse copy of array
print(a3[::-1])
print(a3  ," original array")
"""looping through array"""
#for #while
for i in a3:
    print(i)
for i in a3[0:6]:
        print(i)
#while
print("WHILE LOOP")
temp=0
while temp<a3[4]:
    print(a3[temp])
    temp+=1
print("while using lenght")
temp1=0
while temp1<len(a3):
    print(a3[temp1])
    temp1+=1