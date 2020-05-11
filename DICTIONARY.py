dic={1:"jvascript",2:"java"}
print(dic)
#change
dic[1]="python"
print(dic)
#add
dic[3]="ruby"
print(dic)

#poping
print(dic.pop(1))
print(dic)
#del
del dic[3]
print(dic)
#popitem : value at the end will be poped as a tuple
dic1={1:"first",2:"2nd",3:"third and last"}
print(dic1.popitem())
print(dic1)
print(dic1.keys())
print(dic1.values())
print(dic1.items())