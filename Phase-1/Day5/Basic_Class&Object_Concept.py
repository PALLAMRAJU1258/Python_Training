#Write a program to demonstrate basic concept of classes and object
class Book:
    Author="Aditya"
    published=2005
    cost=100
    book_title="The life of Failure"
obj= Book()
print("{}\n{}\n{}\n{}".format(obj.Author,obj.published,obj.cost,obj.book_title))


class Student:
    name="Raju"
    roll="20A31A1258"
    def print_Details(self):
        print("Name of Student:{}\nRoll no:{}".format(self.name,self.roll))
obj=Student()
obj.print_Details()

