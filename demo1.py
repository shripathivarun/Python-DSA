class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.mac=self.Macbook()# creating inner class object

    def show(self):
        print(self.name,self.rollno)
        self.mac.show()
# INNer class:
    class Macbook:
        def __init__(self):
            self.brand='Apple'
            self.cpu='m3pro'
            self.ram='16'
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student("Varun",1)
s2=Student("Hyd",2,)
print(s1.name,s1.rollno)
s1.show()

