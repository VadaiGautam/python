class person:
    name = "vadai"
    occupation = "AWS & DevOps Engineer"
    package = "7 lakh/annum"

    def info(self):
        print(f"{self.name} is a {self.occupation} and his package is {self.package}")


a = person()
b=person()
c=person()

a.name="vadai gautam "
a.occupation = "Data Analyst"
a.package = "10 lakh/annum"

b.name = "pooja sharma"
b.occupation = " aws & devops engineer"
b.package ="8 lakh/annum"

a.info()
b.info()
c.info()