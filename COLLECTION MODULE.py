"""COLLECTION MODULE IN PYTHON """
#LIST TUPLE DICTIONARY SET ARE CONTAINER
#PYTHON HAS COLLECTION MODULE FOR THE SHORTCOMMING OF DS
#PRVIDES ALTERNATIVES CONTAINER OF BUILTIN DATA TYPES
#specializex collection datatype
"""nametupele(), chainmap, deque, counter, orderedDict, defaultdic , UserDict, UserList,UserString"""


"""** namedtuple()**"""
# return a tuple with named entry there will be named assigned to each value inside tuple to overcome the peoblem of acessing with the index
from collections import namedtuple
a=namedtuple('courses','name,technology')
b=a('machine learning','python')
print(b)
#using list
c=a._make(["artificial intelligence","python"])
print(c)

"""** deque**"""
#pronounced as deck
#is an optimised list to perform insertion and deletion  easily
#way to precisely
from _collections import  deque
l=['e','d','u','c','a','t','i','o','n']
d=deque(l)
print(d)

d.append("python") #at the end
print(d)
d.appendleft("version") #at the end
print(d)


d.pop()
print(d) #aT THE END REMOVE
d.popleft()
print(d)

"""**chain map **"""
#is a dictionary like class for creating a single view of multiple mapping
#return a list of several other dictionaries

from collections import  ChainMap
dic1 ={1:"course",2:"python"}
dic2={3:"collection mpdule",4:"chainmap"}

cm=ChainMap(dic1,dic2)
print(cm)

"""Counter"""
#dictionary subclass for counting hashable objects
from collections import  Counter
c1=[1,1,22,2,3,3,4,5,6,6,7,7,3,9]
c2=Counter(c1)
print(c2)
print(list(c2.elements())) #show elements and the times of their occurence
print(c2.most_common())
sub={3:1 , 6:1 , 22:1} #subtrac elemets times
print(c2.subtract(sub))
print(c2.most_common())

""""OrderedDict """
#dict subclass which remembers the order in which entries is done
#postion will not change
from collections import  OrderedDict
od=OrderedDict()
od[1]="e"
od[2]="d"
od[3]="u"
print(od)
print(od.keys())

print(od.items())

print(od)
od[1]="k"
print(od)


""" defaultdic"""
#dic subclass which cALLS A FACTORY FUNCTION TO SUPPLY MISSING VALUE
#doesnt show any error when a missing key value is call in a dictionary

from collections import  defaultdict
defdic=defaultdict(int)
defdic[1]='python'
defdic[2]='numpy'
defdic[3]='matplotlib'
print(defdic)
print(defdic[4]) #no error 0 o/p
#keyerror

""" UserDict """
#wrapper around dic object for easier dic sub classing
""" Userlist """
#wrapper around list object for easier lisxt sub classing
""" Userstring """
#wrapper around string object for easier string sub classing

