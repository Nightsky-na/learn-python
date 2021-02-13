# Same Like We creat Costructor overload java

class Person:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.country = "Thailand"


#     def __init__ (self, fname, lname, country): #overload
#         self.fname = fname
#         self.lname = lname
#         self.country = country

class Person2:
    def __init__(self, fname=None, lname=None, country="Thailand"):
        self.fname = fname
        self.lname = lname
        self.country = country

    def __str__(self):  # Overwrite
        return "fname : {} lname : {} country : {} ".format(self.fname, self.lname, self.country)


if __name__ == '__main__':
    #     p1 = Person() # create new instance
    #     print(p1.fname)
    #     print(p1.country)
    #     p2 = Person("Kontawat","Wisetpaitoon","Thailand")
    #     print(p2)

    p1 = Person2()
    print(p1.fname)
    print(p1.country)

    p2 = Person2(fname="Kontawat")
    print(p2.fname, p2.country)

    p3 = Person2("Peter", "Parker")
    print(p3)
    # print(p3) #<__main__.Person2 object at 0x00000290B84D3E20> #Before have function str

    p4 = Person2(lname="Swift", fname="Taloy", country="USA")
    print(p4)
