#Range Function
for n in range(0,10):
    print(n)
print('<==================================>')
for n in range(0,11,2):
    print(n)
print('<==================================>')
print('\n')
print(list(range(1,11,1)))
print('<==================================>')
#Enumerate Function
#Enumerate function provides the index of the variable in tuple format
word='vinod'
for items in enumerate(word):
    print(items)
#we can also do Tuple Unpacking
for index,letter in enumerate(word):
    print(index,letter)
print('<====================================>')
#zip function
#it is used to pack the iterables
mylist1=[1,2,3]
mylist2=['a','b','c']
zip(mylist1,mylist2)

print(list(zip(mylist1,mylist2)))
print('<====================================>')
for item in zip(mylist1,mylist2):
    print(item)
print('<====================================>')
#input Function
input('enter your name: ')
print('<====================================>')
#random library
from random import randint
print(randint(0,100))
