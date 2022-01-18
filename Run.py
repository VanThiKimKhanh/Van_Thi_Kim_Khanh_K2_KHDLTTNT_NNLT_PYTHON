from Test import  Test
test = Test()
while (1 == 1):
    print(" Selective menu ")
    print("--------------------------------")
    print("1.Import Studet")
    print("2.Search list Student")
    print("3.Import Teacher")
    print("4.Search list Teacher")
    print("0.Exit program")
    print("--------------------------------")
    key = int(input("Selective: "))
    if (key == 1):
        print("\n1. Import Student.")
        test.importStudent()
        print("\n OK !")
    elif (key == 2):
        if (test.studentmember() > 0):
            print("\n2. Studentmember.")
            test.showStudent(test.getListStudent())
        else:
            print("\n Studentmember!")
    elif (key == 3) :
        print("\3. Import Teacher.")
        test.importTeacher()
        print("\n OK !")
    elif (key == 4):
        if (test.teachermember() > 0):
            print("\n4. Teachermember.")
            test.showTeacher(test.getListTeacher())
        else:
            print("\n Teachermember!")
    elif (key == 0):
        print("\n Exit program!")
        break
    else:
        print("\n Selective no menu!")
        print("\n Selective heve menu.")