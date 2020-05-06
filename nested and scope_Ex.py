#nested and scope
x=25
def num():
    x=50
    return x
print(num())
print(x)
print('====================')
digi=123
def value():
    global digi
    print(f'this is global digit {digi}')
    digi=234
    print(f'this is reassigned digi {digi}')
value()
print('====================')

digi=20
def value(digi):
    print(f'this is global digit {digi}')
    digi=666
    print(f'this is reassigned digi {digi}')
value(digi)
