#Program for temperature Conversion
# Fahrenheit to Celsius: C = (F-32) (5/9)
# Fahrenheit to Kelvin: K = (F-32) (5/9) + 273.15
# Celsius to Fahrenheit: F = C(9/5) + 32
# Celsius to Kelvin: K = C + 273.15
# Kelvin to Fahrenheit: F = (K-273.15) (9/5) + 32
# Kelvin to Celsius: C = K - 273.15
import sys
s="""----------------------------------------------
    Temperature conversion calculator
----------------------------------------------
    1. F to C
    2. F to K
    3. C to F
    4. C to k
    5. K to F
    6. K to C
    7. Exit"""
print(s)
print("*"*50)
val=int(input("Enter Your Choice:"))
print("*"*50)
match val:
    case 1:
        F=float(input("Enter the Temp. In terms of F:"))
        C= (F-32)*(5/9)
        print("Temp. In terms of C={}".format(C))
    case 2:
        F = float(input("Enter the Temp. In terms of F:"))
        K = (F-32)*(5/9) + 273.15
        print("Temp. In terms of K={}".format(K))
    case 3:
        C = float(input("Enter the Temp. In terms of C:"))
        F = C*(9/5) + 32
        print("Temp. In terms of F={}".format(F))
    case 4:
        C = float(input("Enter the Temp. In terms of C:"))
        K = C + 273.15
        print("Temp. In terms of K={}".format(K))
    case 5:
        K = float(input("Enter the Temp. In terms of K:"))
        F = (K-273.15)*(9/5) + 32
        print("Temp. In terms of F={}".format(F))
    case 6:
        K = float(input("Enter the Temp. In terms of K:"))
        C = K - 273.15
        print("Temp. In terms of C={}".format(C))
    case 7:
        print("Thankyou For using this program")
        sys.exit()
    case _:
       print("You Enter the Wrong Case Please Try Again")

print("Program Execute Successfully")
