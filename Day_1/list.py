# list are mutable and ordered    

lst=[2,6,4,7,8,3]
# print(lst)
# print(type(lst))

# methods of the list
lst.append(11)
# print(lst)

lst.extend([22,33,44,55])
# print(lst)

lst.append(('first','second','third'))
# print(lst)
lst.pop(2)
# print(lst)

lst.remove(('first','second','third'))
# print(lst)

games=['football','chess','ludo','cricket']
# print(games)
#games.clear()
#print(games)

another_games=games.copy()
#  print(another_games)

fruits=['cherry','orange','avacado','orange']
# print(fruits.count('orange'))

laptop=['dell','hp','acer']
# laptop.insert(1,'preditor')
# print(laptop)


# print(laptop[1])

# for i in laptop:
#     print(i)


# list comprehensions

fruits=['orange','cherry','apple','banana']
lst_comp=[x for x in fruits if 'a' in x]
print(lst_comp)

another_lst=[fruit for fruit in fruits if len(fruit)>5]
print(another_lst)

new_lst=['Pawan','sanjay','Mohan','sUrya']
answer_lst=[name for name in new_lst if name[0].isupper()]
print(answer_lst)