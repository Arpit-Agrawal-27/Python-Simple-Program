#validation of student Number
while(True):
    sno=input("Enter Student Number:")
    if (sno.isdigit()):
        if (int(sno) in range(100, 200)):
            break
        else:
            if (int(sno) is not range(100, 200)):
                print("\t{} is invalid Number--try again".format(sno))
    elif(sno.isalnum()):
        print("\t{} Is Invalid Number-try Again".format(sno))
#Vaildation of student name
while(True):
    name=input("Enter Ur Name:") # Guido Van Ross2m
    words=name.split() # [Guido,Van,Ross2m]
    jname="".join(words)
    if(jname.isalpha()):
        break
    print("\t{} is invalid Name--try again".format(name))
#validation of student  marks in C
while(True):
    cm=input("Enter C Lang Marks:")
    if (cm.isdigit()):
        if (int(cm) in range(0, 101)):
            break
        else:
            if (int(cm) not in range(0,101)):
                print("\t{} is invalid Marks--try again".format(cm))
    elif (cm.startswith("-")):
        print("\t{} is invalid Marks--try again".format(cm))
    elif(cm.isalnum()):
        print("\t{} Is Invalid Marks-try Again".format(cm))
#validation of student  marks in CPP
while(True):
    cppm=input("Enter CPP Lang Marks:")
    if (cppm.isdigit()):
        if (int(cppm) in range(0, 101)):
            break
        else:
            if (int(cppm) not in range(0,101)):
                print("\t{} is invalid Marks--try again".format(cppm))
    elif (cppm.startswith("-")):
        print("\t{} is invalid Marks--try again".format(cppm))
    elif(cppm.isalnum()):
        print("\t{} Is Invalid Marks-try Again".format(cppm))
#validation of student  marks in Python
while(True):
    pym=input("Enter PYTHON Lang Marks:")
    if (pym.isdigit()):
        if (int(pym) in range(0, 101)):
            break
        else:
            if (int(pym) not in range(0,101)):
                print("\t{} is invalid Marks--try again".format(pym))
    elif (pym.startswith("-")):
        print("\t{} is invalid Marks--try again".format(pym))
    elif(pym.isalnum()):
        print("\t{} Is Invalid Marks-try Again".format(pym))
totmarks=int(cm)+int(cppm)+int(pym)
percent=(totmarks/300)*100
if(int(cm)<40) or(int(cppm)<40) or (int(pym)<40):
    grade="FAIL"
else:
    if(totmarks in range(250,301)):
        grade="DISTINCTION"
    elif(totmarks in range(200,250)):
        grade="FIRST"
    elif (totmarks in range(150, 200)):
        grade = "SECOND"
    elif (totmarks in range(120, 150)):
        grade = "THIRD"
print("="*50)
print("\t\tSTUDENT MARKS REPORT")
print("="*50)
print("\t\tStudent Number:{}".format(sno))
print("\t\tStudent Name:{}".format(name))
print("\t\tStudent Marks in C:{}".format(cm))
print("\t\tStudent Marks in C++:{}".format(cppm))
print("\t\tStudent Marks in Python:{}".format(pym))
print("\t\tStudent Total Marks:{}".format(totmarks))
print("\t\tStudent Percentage of Marks:{}".format(round(percent,2)))
print("\t\tStudent Grade:{}".format(grade))
print("="*50)
