class String():
    def __init__(self):
        self.s=""
    def getstr(self):
        self.s=input()
    def prntstr(self):
        print(self.s.upper())
q=String()
q.getstr()
q.prntstr()