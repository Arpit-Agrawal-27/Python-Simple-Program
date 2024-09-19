#Program for to Generate 1 To N number of multiplication Table
n=int(input("Enter How many Mul. Table U want:"))
if n<=0:
    print("{} is Invalid input".format(n))
else:
    for num in range(1,n+1): #Outer loop
        print("-"*50)
        print("Multiplication for {}".format(num))
        print("-"*50)
        for i in range(1,11): #Inner Loop
            print("\t{}x{}={}".format(num,i,num*i))
     
