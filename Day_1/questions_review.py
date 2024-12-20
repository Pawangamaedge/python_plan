# 1
# basic data types are avaiable in python are: numeric, sequence type, boolean type, mapping type

# 2
x=3
y=str(x)
# print(type(x))
# print(type(y))

# 3
x=4
if (x>3 and x<5):
     print("this is AND statement")
else:
     print("nothing")

# 4 


# 5
def def_func(first=[3,4,5,6], last=('one','two','three')):
     print(f"the list is: {first} \nthe set is: {last}")
def_func()

# 6
num=[]
for i in range(1,11):
     num.append(i)
print(num)
squared_lst=[sqr**2 for sqr in num]
print(squared_lst)

# 7
# list is mutable, means list can be changeable but 
# tuple is immutable, means tuple cant be change once it is declard

# 8
new_set={'chair','table','sofa'}
# new_set.add('dining table')
# print(new_set)
new_set.remove('sofa')
print(new_set)

# 9
lst_dct={
     'role':['programmer','chef','teacher'],
     'name':['akash','sohan','ajay'],
     'location':'indore'
}
print(lst_dct.keys())
print(lst_dct.values())
