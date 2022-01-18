import math
from Person import Student
from Person import Teacher


class Test:
    listStudent = []

    def generateIDst(self):
        maxidstudent = 1
        if (self.studentmember() > 0):
            maxidstudent = self.listStudent[0]._id
            for st in self.listStudent:
                if (maxidstudent < st._id):
                    maxidstudent = st._id
            maxidstudent = maxidstudent + 1
        return maxidstudent

    def studentmember(self):
        return self.list[Student].__len__()

    def importStudent(self):
        idstudent = self.generateIDst()
        name = input("Import Name: ")
        phone = input("Import Phone: ")
        email = input("Import Email: ")
        mathmark = float(input("Import Math Mark: "))
        englishmark = float(input("Import English Mark : "))
        literaturemark = float(input("Import Literaturemark: "))
        testmark = float(input("Import Test Mark: "))
        st = Student(idstudent, name, phone, email, mathmark, englishmark, literaturemark, testmark)
        self.averagemark(st)
        self.learningresults(st)
        self.listStudent.append(st)

    def averagemark(self, st: Student):
        averagemark = (st._mathmark + st._englishmark + st._literaturemark) / 3
        st._averagemark = math.ceil(averagemark * 100) / 100

    def learningresults(self, st: Student):
        if (st._averagemark >= 8):
            st._learningresults = "A"
        elif (st._averagemark >= 6.5):
            st._learningresults = "B"
        elif (st._averagemark >= 5):
            st._learningresults = "C"
        else:
            st._learningresults = "D"

    def findByIdStudent(self, idstudent):
        searchResult = None
        if (self.studentmember() > 0):
            for st in self.listStudent:
                if (st._id == idstudent):
                    searchResult = st
        return searchResult

    def findByNameStudent(self, keyword):
        listStudent = []
        if (self.studentmember() > 0):
            for st in self.listStudent:
                if (keyword.upper() in st._name.upper()):
                    listStudent.append(st)
        return listStudent

    def showStudent(self, listStudent):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("idstudent"," name"," phone"," email"," mathmark"," englishmark"," literaturemark"," testmark"))
        if (listStudent.__len__() > 0):
            for st in listStudent:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(st._id, st._name, st._phone, st._email, st._mathmark, st._englishmark,
                              st._literaturemark, st._averagemark, st._testmark))
        print("\n")



    listTeacher = []

    def generateIDtea(self):
        maxidteacher = 1
        if (self.teachermember() > 0):
            maxidteacher = self.listTeacher[0]._id
            for tea in self.listTeacher:
                if (maxidteacher < tea._id):
                    maxidteacher = tea._id
            maxidteacher = maxidteacher + 1
        return maxidteacher

    def teachermember(self):
        return self.list[Teacher].__len__()

    def importTeacher(self):
        idteacher = self.generateIDtea()
        name = input("Import Name: ")
        phone = input("Import Phone: ")
        email = input("Import Email: ")
        teachingsubject = input(" Import Teaching Subject: ")
        tea = Teacher(idteacher, name, phone, email,teachingsubject)

    def findByIdTeacher(self, idteacher):
        searchResult = None
        if (self.teachermember() > 0):
            for tea in self.listTeacher:
                if (tea._id == idteacher):
                    searchResult = tea
        return searchResult

    def findByNameTeacher(self, keyword):
        listTeacher = []
        if (self.teachermember() > 0):
            for tea in self.listTeacher:
                if (keyword.upper() in tea._name.upper()):
                    listTeacher.append(tea)
        return listTeacher

    def showTeacher(self, listTeacher):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
              .format("idteacher"," name"," phone"," email"," teaching subject"))
        if (listTeacher.__len__() > 0):
            for tea in listTeacher:
                print("{:<8} {:<18} {:<8} {:<8}{:<8}"
                      .format(tea._id, tea._name, tea._phone, tea._email,tea._teachingsubject))
        print("\n")

