from Person import Student
from Person import Teacher
from Majors import Majors

class Class:
    classname: str
    majorsname:  list[Majors]
    idmajors: list[Majors]
    studentmember: Student
    teachermember: Teacher

    def __init__(self, classname: str, majorsname: str, idmajors: str, studentmember: int, teachermember: int) -> None:
        Majors.__init__(majorsname)
        Majors.__init__(idmajors)
        self.classname = classname
        self.studentmember = studentmember
        self.teachermember = teachermember
        majorsname = []
        idmajors = []

    def __init__(self, classname: str, majorsname: str, idmajors: str, studentmember: int, teachermember: int, majors: list[Majors],) -> None:
        Majors.__init__(majorsname, idmajors)
        self.classname = classname
        self.studentmember = studentmember
        self.teachermember = teachermember
        majorsname = majorsname
        idmajors = idmajors

    def getclassname(self):
        return self.classname

    def getStudentmember(self) -> Student:
        return self.studentmember

    def studentmember(self):
        return self.list[Student].__len__()

    def getTeachermember(self) -> Teacher:
        return self.teachermember

    def teachermember(self):
        return self.list[Teacher].__len__()

    def addMajorsname(self, majors: Majors) -> None:
        self.majorsname.append(majors)

    def getMajorsname(self) -> list[Majors]:
        return self.majorsname

    def addIdmajors(self, majors: Majors) -> None:
        self.idmajors.append(majors)

    def getIdmajors(self) -> list[Majors]:
        return self.idmajors

    def outputInfo(self) -> str:
        result = "Class name:" + self.classname + ", Majors name:" + self.majorsname + ", ID Majors:" + self.idmajors + ", Student member:" + self.list[Student].__len__() + ", Teacher member:" + self.list[Teacher].__len__()
        return result
