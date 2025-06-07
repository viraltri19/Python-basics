# Average of 3 numbers
def average(a,b,c):
    return (a + b + c)/3
avg = average(1,2,3)
print(avg)


def odd_even():
    num = int(input("enter a number: "))
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")
odd_even() 