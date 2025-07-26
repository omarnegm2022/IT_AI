try:
    user_no = float(input("Enter your number: "))
except ValueError:
    user_no = float(input("no spaces, alphas or special chars. Try again:\n   "))
str_no= str(user_no)

print("It's odd." if (len(str(user_no/2)) > len(str_no)) else "It's even.")
#NOTE: that is, in case of floating-point numbers:
"""The Least Significant Digit of the result still even.
>>> 2.3/2
1.15
>>> 2.4/2
1.2
>>> 1.2/2
0.6
>>> 1.15/2
0.575
"""