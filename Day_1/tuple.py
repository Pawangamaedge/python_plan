# tuples are immutable and ordered

tup=tuple()
print(type(tup))

tup1=('shailesh',23,'age',56.234)
# print(tup1)
# tup1[0]='rohan'  # changing not allowed in tuple
# print(tup1)

# methods of tuple in python 
# print(len(tup1))

new_tup=(2,3,5,'players','rohan')
lst=list(new_tup)
lst[3]=6
lst[4]=7
new_tup=tuple(lst)
# print(new_tup)

# unpacking the tuple
tuple_1=('tuple_1','tuple_2','tuple_3')
(first,second, third)=tuple_1
#   print(first,second,third)

tuple_1=('tuple_1','tuple_2','tuple_3','tuple_4','tuple_5','tuple_6')
(first,second, *third)=tuple_1
# print(tuple_1)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x=thistuple.count(5)
print(x)