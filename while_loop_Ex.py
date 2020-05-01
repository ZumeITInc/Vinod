                           #while Loop
#Syntax : While (some_boolean_condition):
                #Execute this block
          #else:
                #execute this block
#==================================================
x=0
while x < 5:
    print(f'the value of x is {x}')
    x= x+1
else:
    print('the value is greater than x')
print("<=============================>")
x=0
while x<5:
    if x==3:
        pass
    print(x)
    x+=1
print("<==========================>")

#=================================================
x=0
while x<5:
    if x==3:
        break
    print(x)
    x+=1
print("<==========================>")
#====================================================
x=0
while x<5:
    if x==3:
        continue
    print(x)
    x+=1
print("<==========================>")
