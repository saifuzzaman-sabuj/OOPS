class StackOverflowUser:
    def __init__(self, name, userid, age):
        self.name = name
        self.userid = userid
        self.age = age


name = input("Enter name: ")
userid = int(input("Enter user id: "))
age = int(input("Enter age: "))

dave = StackOverflowUser(name, userid, age)
print(dave.name, dave.userid, dave.age)