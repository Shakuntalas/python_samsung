#arr1=[11,7,5,3,2]
#print(arr1[:])
#print(arr1[::])
#print(arr1[1:4])
#print(arr1[1:10])
#print(arr1[:5:2])
#print(arr1[4::-2])
def my_range(args):
    if len(args)==1:
      i=0
      while i<args[0]:
         yield i
         i+=1
for i in my_range(10):
     i+=2
     priint('i=',i)         