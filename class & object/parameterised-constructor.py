class person:
    def __init__(self ,n,o,p):
        print("hey i am a person")
        self.name = n
        self.occupation = o
        self.package =p

    def info(self):
        print(f"{self.name} is a {self.occupation} and his package is {self.package}")

a = person("vadai","aws or devops engineer","7 lakh/anuum")
a.info()