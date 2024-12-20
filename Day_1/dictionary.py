#dictionary stores the data in tht form of key and value pair

dct={'brand':'ford','model':'mustang','year':1965}
print(dct)
# print(type(dct))

print(dct['brand'])
dct['brand']='toyota'
# print(dct)

lst_dct={
     'role':['programmer','chef','teacher'],
     'name':['akash','sohan','ajay'],
     'location':'indore'
}
print(lst_dct)
print(lst_dct['role'][1])
lst_dct['role'][1]='student'
print(lst_dct)

# methods 

print(lst_dct.get('role'))
print(lst_dct.keys())
print(lst_dct.values())
print(lst_dct.items())