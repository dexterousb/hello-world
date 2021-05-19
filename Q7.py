# Python Program for compound interest

#User input
p = float(input("Enter principal:"))
r = float(input("Enter rate:"))
t = float(input("Enter time:"))

#ci interest
a = float(p * (pow((1 + r / 100), t)))
ci = float(a - p)

#display
print("The Compound Interest is" , ci)
