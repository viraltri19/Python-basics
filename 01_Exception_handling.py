a = 5
b = 2

try:
    print("Resources Open")
    print(a/b)
    k= int(input("Enter a number: "))
    print(k)
except ZeroDivisionError as e:
    print("Number can not divied by zero",e)
except ValueError as e:
    print("Invalid Input",e)
except Exception as e :
    print("Something went wrong")
finally:
    print("Resources closed")


