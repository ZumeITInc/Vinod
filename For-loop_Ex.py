                                #FOR LOOP
#Syntax: My_iterable=[1,2,3,4]
        #for Items_name in My_iterable:
            #print(Item_name)
My_list=[1,2,3,4,5,6]
for x in My_list:
    if x%2==0:
        print(f' even Number {x}')
        print('\n')
    else:
        print(f' odd Number {x}')
        print('\n')
print("<====================>")
#========================================
list_sum = 0
for num in My_list:
    list_sum=list_sum + num
    print(list_sum)
    print('\n')
print("<===================>")
#=========================================
mylist=[(1,2),(3,4),(5,6),(7,8)] #this is called tuple Unpacking
for (num1,num2) in mylist:
    print(num1)
    print('\n')
    print(num2)
    print('\n')
print("<======================>")
#==========================================
dic={'key1':1,'key2':2,'key3':3}
for values in dic.values():
    print(values)
    print('\n')
for keys in dic.keys():
    print(keys)
    print('\n')
for items in dic.items():
    print(items)
    print('\n')
print("<======================>")

#===========================================

