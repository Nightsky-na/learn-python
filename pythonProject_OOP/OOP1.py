class Player():
      def __init__(self): #dunder -> double underscore
          self.fname = ""
          self.lname = ""
          self.number = ""

class Player2:
    def __init__(self,fname,lname,number):
        self.fname = fname
        self.lname = lname
        self.number = number

if __name__ == '__main__':

    p1 = Player()
    p1.fname = "Kontawat"
    p1.lname = "Wisetpaitoon"
    p1.number = 1

    p2 = Player()
    p2.fname = "Titaya"
    p2.lname = "Wisetpaitoon"
    p2.number = 2

    p1a = Player2("Nantarat","Wisetpaitoon",3)
    p2a = Player2("Wutichai","Wisetpaitoon",4)

    print(p1a.fname)
    print(p2a.lname)

    p1t = ("Pratum","Chaipracit",5) #tuple
    print(p1t)
    print(p1t[0])

    p1d = {"fname" : "Vichai","lname" : "chaipracit", "number" : 6} #Dic...
    print(p1d)
    print(p1d["fname"])