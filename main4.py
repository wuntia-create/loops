num = int(input("Enter a number to be checked:"))
is_not_prime = False
if num > 1:
    #Check for factors
    for i in range(2, num):
        if (num % i) == 0:
            is_not_prime = True
            break
if is_not_prime:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")