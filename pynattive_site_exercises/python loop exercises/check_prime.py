# Exercise 11: Write a program to display all prime numbers within a range

'''
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
'''


def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return
    else:
        return num


start_num = 25
end_num = 50

for num in range(start_num, end_num):
    if is_prime(num) is not None:
        print(is_prime(num))


# other solution (pynative solution)

start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)
