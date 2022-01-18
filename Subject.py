class Subject:
    subjectname: str
    idsubject: str
    averagemark: float
    testmark: float

    def __init__(self, subjectname, idsubject, averagemark, testmark) -> None:
        super().__init__()
        self.subjectname = subjectname
        self.idsubject = idsubject
        self.averagemark = averagemark
        self.testmark = testmark

    def getsubjectname(self):
        return self.subjectname

    def getidsubject(self):
        return self.idsubject

    def getaveragemark(self):
        return self.averagemark

    def gettestmark(self):
        return self.testmark