class Majors:
    majorsname: str
    idmajors: str

    def __init__(self, majorsname, idmajors) -> None:
        super().__init__()
        self.majorsname = majorsname
        self.idmajors = idmajors

    def getmajorsname(self):
        return self.majorsname

    def getidmajors(self):
        return self.idmajors