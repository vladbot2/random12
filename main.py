import random

length = int(input("Enter the number of items in the lists: "))
choice = int(input("1) Elements of both lists \n 2) Elements of both lists without repetitions \n 3) Elements common to both lists \n 4) Only unique elements of each list \n 5) All of the above \n Enter your choice:"))
list1 = []
list2 = []

if length > 0:
   for i in range(length):
       list1.append(random.randint(0, 100))
       list2.append(random.randint(0, 100))

   print(" List 1: ", list1)
   print("List 2: ", list2)

   if choice == 1 or choice == 5:
       list3 = list1 + list2
       print("Elements of both lists: ", list3)

   if choice == 2 or choice == 5:
       list3 = list(set(list1 + list2))
       print("Elements of both lists without repetitions: ", list3)

   if choice == 3 or choice == 5:
       list3 = list(set(list1) & set(list2))
       print("Elements common to the two lists: ", list3)

   if choice == 4 or choice == 5:
       list3 = list(set(list1) ^ set(list2))
       print("Only unique elements of each of the lists: ", list3)

else:
   print("Items in lists must be positive")
