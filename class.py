class StackOverflowUser:
    def __init__(self, name, userid, age):
        self.name = name
        self.userid = userid
        self.rep = age


name = input("Enter name: ")
userid = int(input("Enter user id: "))
rep = int(input("Enter age: "))

dave = StackOverflowUser(name, userid, rep)
print(dave.name, dave.userid, dave.rep)