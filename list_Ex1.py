                     #LIST
#list is a Ordered collection of objects
list=['one',2,3.12]
print(list)
print('\n')
#====================
#INDEXING
list=['one','two','three']
print(list[0])
print('\n')
print(list[1])
print('\n')
list[0]='1'
print(list)
print('\n')

#=======================
#SLICING
list=[1,2,3,4,5,6]
print(list[0::3])
print('\n')
print(list[::-1])
print('\n')
#=======================
#CONCATINATION
list1=['one',',two','three']
list2=[ 'four','five','six']
print(list1+list2)
print('\n')
#========================
#METHODS
#APPEND()   This method will add objects at the end
list1=[1,2,3]
list1.append(4)
print(list1)
print('\n')
#POP    This method will delete the last object
list1.pop()
print(list1)
print('\n')
#You can Also use index position to remove an Object
list1.pop(0)
print(list1)
print('\n')
#SORT This method will arrange the object in a order
list1=[1,5,3,7,9]
list2=['a','d','h','q']
list1.sort()
list2.sort()
print(list1)
print('\n')
print(list2)
print('\n')
list1.reverse()
print(list1)
