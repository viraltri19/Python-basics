# append : To add value in the end of the list
# list = ['Karan',34,89,9,78,"Helo"]
# list.append(7)
# print(list)

# list1 = [34,78,90,56]

# list1.sort()
# print(list1)

# list1.reverse()
# list1.sort(reverse=True)
# print(list1)

# list1.insert(2,'j')
# print(list1)

# m1 = input("Enter a 1st Movie : ")
# m2 = input("Enter a 2nd Movie : ")
# m3 = input("Enter a 3rd Movie : ")

# movies = []
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)

# print(movies)

#Palindrom

list = [1,2,1]

list1 = list.copy()
print(list1)

list1.reverse()
print(list1)

if(list == list1):
    print("List is Palindrom")
else:
    print("List is not Palindrom")
