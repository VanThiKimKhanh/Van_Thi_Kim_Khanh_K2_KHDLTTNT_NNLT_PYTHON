class Person:
    name: str
    phone: int
    email: str

    def __init__(self, name, phone, email) -> None:
       super().__init__()
       self.name = name
       self.phone = phone
       self.email = email

    def outputInfo(self) -> str:
        result = "Name: " + self.name + ", Phone number: " + self.phone + ", Email: " + self.email
        return result


class Student(Person):
    idstudent: str
    def __init__(self, name, phone, email, idstudent) -> None:
        Person.__init__(self, name, phone, email)
        self.idstudent = idstudent

    def outputInfo(self) -> str:
        result = super(Student, self).outputInfo() + ", ID Student: " + self.idstudent
        return result


class Teacher(Person):
    idteacher: str
    teachingsubject: str
    def __init__(self, name, phone, email, idteacher, teachingsubject) -> None:
        Person.__init__(self, name, phone, email)
        self.idteacher = idteacher
        self.teachingsubject = teachingsubject

    def outputInfo(self) -> str:
        result = super(Teacher, self).outputInfo() + ", ID Teacher: " + self.idteacher + ", Teaching subject: " + self.teachingsubject
        return result