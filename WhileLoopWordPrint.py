#Program for Print Word With the help of While loop
word=input("Enter the Word:")
print("-"*50)
print("Word in FordWard Direction")
print("-"*50)
index=0 #Initilization
while index<len(word): #condition
    print(word[index])
    index+=1 # Updation
else:
    print("-"*50)
    print("Word in backward direction")
    print("-" * 50)
    index=-1 #Initilization
    while index>=-len(word): #condition
        print(word[index])
        index=index-1 #
