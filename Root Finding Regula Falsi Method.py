# Root Finding - Regula Falsi Method

# FUNCTIONS

# function calculation based on given x value


def f(x):
    result = 0  # initial sum = 0
    for i in range(degree, 0, -1):
        temp = x  # exponent base
        for j in range(i, 1, -1):  # power calculation
            temp *= x
        result += coeff[i]*temp
    return result + coeff[0]  # add with constant


def regulafalsi(x1, x2, iterations):
    while((not(f(x1) < precision and f(x1) > -precision)) and (not(f(x2) < precision and f(x2) > -precision))):
        print("Iteration", iterations, "x1 =", x1, "f(x1) =",
              f(x1), ":: x2 =", x2, "f(x2) =", f(x2), ":: f(x1)-f(x2) =", f(x1) - f(x2))
        m = (f(x2)-f(x1))/(x2-x1)  # finding gradient of new line
        xnew = -f(x1)/m + x1  # new x
        if(f(xnew) == 0):  # exception : exact mid-cut
            return(print("One of the root is approximately", str(xnew)))
        elif(f(xnew)*f(x1) < 0):
            x2 = xnew
        elif(f(xnew)*f(x2) < 0):
            x1 = xnew
        iterations += 1
        if(iterations > 900):  # exception : iteration limit/no solution
            return(print("Iteration limit exceeded, bad guess or no real roots"))
        return(regulafalsi(x1, x2, iterations))  # recursion
    print("Iteration", iterations, "x1 =", x1, "f(x1) =",  # solution print
          f(x1), ":: x2 =", x2, "f(x2) =", f(x2), ":: f(x1)-f(x2) =", f(x1) - f(x2))
    print("\nOne of the root(s) is approximately", str(x1))


# BODY
# declaring degree of polynomial
degree = int(input("Enter the degree of the polynomial : "))

coeff = [0]*(degree+1)  # preparing list by filling with 0

# entering the coefficients of the polynomial
print("\nEnter the coefficients for : ")
for i in range(degree, -1, -1):
    print("x^"+str(i), ":", end=" ")
    coeff[i] = int(input())

# displaying function f(x)
print("\nFunction f(x)= ", end="")
for i in range(degree, 0, -1):
    if(coeff[i] > 0):
        print(coeff[i], end="")
        print("x^"+str(i), end=" + ")
print(coeff[0])

# guessing x1 and x2
precision = 0.01  # set precision of the result
print("\nPick 2 points : ")
x1 = float(input("Point 1 : "))
x2 = float(input("Point 2 : "))

while(f(x1)*f(x2) > 0):  # loop to ensure guess validity
    print("Invalid guess, f(x1)*f(x2)>0", "f(x1) =", f(x1), "f(x2) =", f(x2))
    x1 = float(input("Point 1 : "))
    x2 = float(input("Point 2 : "))

print("Accepted guess, f(x1)*f(x2)<0 =>",
      "f(x1) =", f(x1), "f(x2) =", f(x2))

# exception : guessed right
if(f(x1) == 0):
    print("Guessed right, one of the root is approximately", str(x1))
elif(f(x2) == 0):
    print("Guessed right, one of the root is approximately", str(x2))
else:
    # initiallizing iterations
    iterations = 0
    regulafalsi(x1, x2, iterations)
