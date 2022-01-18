from Person import Student
from Subject import Subject

class Learningresults:
    semester: int
    studentname: Student
    idstudent: Student
    subjectname: Subject
    averagemark: Subject
    testmark: Subject

    def __init__(self, semester: int, studentname: str, idstudent: str, subjectname: str, averagemark: float, testmark: float) -> None:
        self.semester = semester
        self.studentname = studentname
        self.idstudent = idstudent
        self.subjectname = subjectname
        self.averagemark = averagemark
        self.testmark = testmark

    def getSemester(self):
        return self.semester

    def getStudentname(self) -> Student:
        return  self.studentname

    def getIdstudent(self) -> Student:
        return self.idstudent

    def getSubjectname(self) -> Subject:
        return self.subjectname

    def getAveragemark(self) -> Subject:
        return self.averagemark

    def getTestmark(self) -> Subject:
        return self.testmark

    def outputInfo(self) -> str:
        result = "Semester: " + self.semester + ", Student name:" + self.studentname + ", ID Student: " + self.idstudent + ", Subject name:" + self.subjectname + ", Average mark: " + self.averagemark + ", Test mark:" + self.testmark
        return result