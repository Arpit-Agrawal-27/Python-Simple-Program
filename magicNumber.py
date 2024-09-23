#Program for finding magic number if input number's squre last digit is same of input number
n = int(input("Enter a number: "))
s = n**2
if str(s).endswith(str(n)):
    print(f"{n} Is A Magic Number")
else:
    print(f"{n} Is Not Magic")
