# try-> contains the code that may raise the exception
# except-> code of block that handle the exception that may occur
# finally-> code of block that will always execute whether the exception will occur or not 
# raise-> used to raise the exceptions

# while True:
#      try:
#           number=int(input("enter the number ")) 
#           if number:
#                print(number)
#      except ValueError:
#           print('Enter the number, your have given me name')
#      finally :
#           print(f"the number will be: {number}")



x = int(input("enter here "))
if not type(x) is str:
     raise TypeError('only strings are allowed')
else:
     print(type(x))
     print("this is string")



