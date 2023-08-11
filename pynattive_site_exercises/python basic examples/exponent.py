# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# Note here exp is a non-negative integer, and the base is an integer.

'''
5 ^ 3 = 5 * 5 * 5 = 125

'''


def exponent(base, exp):
    output = 0
    for i in range(exp):
        if i == 0:
            output = base
        else:
            output = output * base
    return output


base = 4
exp = 3

print(f'{base} rasises to the power of {exp}: {exponent(base, exp)} ')


# other solution

def exponent1(bse, ex):
    num = exp
    output = 1

    while num > 0:
        output *= bse
        num -= 1

    return output


print(exponent1(5, 3))
