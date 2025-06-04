# marks = float(input("Enter Your Percentage: "))

# if(marks>= 90):
#     print("Grade A")
# elif(marks>=80 and marks < 90):
#     print("Grade B")
# elif(marks>=70 and marks < 80 ):
#     print("Grade C")
# elif(marks < 70 ):
#     print("Grade D")

a = int(input("Enter a value of A :"))
b = int(input("Enter a value of B :"))
c = int(input("Enter a value of C :"))
d = int(input("Enter a value of D :"))

if(a > b and a > c and a > d):
    print("A is Largest Number: ", a)
elif(b > c and b > d):
    print("B is Largest Number: ", b)
elif(c > d):
    print("C is Largest Number: ", c)
else:
    print("D is Largest Number: ", d)