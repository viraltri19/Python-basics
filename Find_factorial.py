# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))


def find_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)


# 5! = 5 * 4 *3 *2*1
find_factorial(5)