def Mynew():
    print('1.Hello Vinod')
Mynew()
print('<============================>')
def myfunc(name):
    print('2.Hello' " "+name)
myfunc('vinod')
print('<============================>')
def slide(add1,add2):
    return(add1+add2)
sum=slide(20,25)
print('<============================>')
def new(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False
newstring1=new('I have a Dog')
print('<============================>')
def new(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False
newstring2=new('this is a cat')
print('<============================>')
def new_dog(mystring):
    return 'dog' in mystring.lower()
dog=new_dog('I dont have a dog')

