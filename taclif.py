#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(x)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


###################################################

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

####################################################

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#####################################################

thislist = ["apple", "banana", "cherry"]
print(thislist)

#########################################################

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

############################################################

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#########################################################

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#########################################################

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

###########################################################

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

##########################################################

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:5])

##############################################################

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

############################################################

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

################################################################

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

###################################################################

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#################################################################

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

###################################################################

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

###################################################################

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

########################################################################

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#######################################################################

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

#########################################################################

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#########################################################################

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#########################################################################

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#########################################################################3

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

###########################################################################

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

############################################################################3

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

##################################################################################3

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#######################################################################


