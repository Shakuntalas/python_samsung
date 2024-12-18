list1=[]
list2=list()
list1.append(10)
list1.append(20)
list1.insert(1,25)
print(list1)
print("popped element is",list1.pop())
list1.extend([10,19])
print(list1)
list1=list(list1)
del list2[0]
print(f'List1={list1}\nList2={list2}')
list1.clear()
print(list1)