#Program for generating Mul Table for a Given +VE Number With the  help of While Loop
n=int(input("Enter a Number for generating mul table:"))
if n<=0:
    print("{} is Invalid")
else:
    print("-"*50)
    print("Mul Table for {} ".format(n))
    print("-"*50)
    i=1
    while i<=10:
        print("\t\t{}x{}={}".format(n,i,n*i))
        i=i+1
        print("-"*50)
    else:
        print("*"*50)
#Program for to Generate the table with the help of for loop
n=int(input("Enter the number:"))
if n<=0:
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Multiplication Table for {}".format(n))
    print("-"*50)
    for i in range(1,11):
        print("\t\t{} x {}={}".format(n,i,n*i))
        print("-"*50)
