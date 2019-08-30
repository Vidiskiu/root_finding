# Root Finding - Secant Method

# FUNCTIONS


def f(x):  # function calculation based on given x value
    result = 0  # initial sum = 0
    for i in range(degree, 0, -1):
        temp = x  # exponent base
        for j in range(i, 1, -1):  # power calculation
            temp *= x
        result += coeff[i]*temp
    return result + coeff[0]  # add with constant


def secant(x1, x2, iterations):  # secant iteration
    while(not(f(x1) < precision and f(x1) > -precision)):
        print("Iteration", iterations, "x1 =", x1, "f(x1) =",
              f(x1), ":: x2 =", x2, "f(x2) =", f(x2))
        m = (f(x2)-f(x1))/(x2-x1)  # finding gradient
        x2 = x1  # new x2 is old x1
        x1 = -f(x1)/m + x1  # new x1
        iterations += 1  # counting iterations
        if(iterations > 900):  # exception : iteration limit/no solution
            return(print("Iteration limit exceeded, bad guess or no real roots"))
        return(secant(x1, x2, iterations))  # recursion
    print("Iteration", iterations, "x1 =", x1, "f(x1) =",  # solution print
          f(x1), ":: x2 =", x2, "f(x2) =", f(x2))
    print("\nOne of the root(s) is approximately", x1)


# BODY
# declaring degree of polynomial
degree = int(input("Enter the degree of the polynomial : "))

coeff = [0]*(degree+1)  # preparing list by filling with 0

# entering the coefficients of the polynomial
print("\nEnter the coefficients for : ")
for i in range(degree, -1, -1):
    print("x^"+str(i), ":", end=" ")
    coeff[i] = float(input())

# displaying function f(x)
print("\nFunction f(x)= ", end="")
for i in range(degree, 0, -1):
    if(coeff[i] > 0):
        print(coeff[i], end="")
        print("x^"+str(i), end=" + ")
print(coeff[0])

# guessing x1
h = 0.1  # step-difference
precision = 0.01  # set precision of the result
print("Pick 2 points =")
x1 = float(input("Pick x1 : "))
x2 = float(input("Pick x2 : "))

# exception : guessed right
if(f(x1) < precision and f(x1) > -precision):
    print("Guessed right, one of the root(s) is approximately", x1)
elif(f(x2) < precision and f(x2) > -precision):
    print("Guessed right, one of the root(s) is approximately", x2)
else:
    # initiallizing iterations
    iterations = 0
    secant(x1, x2, iterations)