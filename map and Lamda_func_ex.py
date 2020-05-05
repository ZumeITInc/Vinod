#MAP and Lamba Functions
def square(num):
    return num**2
my_num=[1,2,3,4,5,6]
for nums in map(square,my_num):
    print(nums)
print(list(map(square,my_num)))
print('<===============================>')
def even(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]
name=['vinodh','jones','jack']
print(list( map(even,name)))
print('<===============================>')
def demo(mystring):
    if (mystring)%2==0:
        return 'Even'
mynum=range(0,11)
print(list(filter(demo,mynum)))
print('<===============================>')

    
