class shareef:
    def __init__(self,fname,id,roll_no):
        self.fullname=fname
        self.collageid=id
        self.rolln=roll_no
    def printdetails(self):
        return f"THE STUDENT FULL NAME IS -{self.fullname}\n the collageid is-{self.collageid}\n the rollnum is-{self.rolln}"
one=shareef("masthan shareef","mits","17691A0497")
print(one.printdetails())

