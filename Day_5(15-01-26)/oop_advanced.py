# (1)Create a base class Animal and subclasses Dog and Cat. 

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Bhaow!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Jackey")
cat = Cat("Manii")

dog.speak()
cat.speak()

# (2)Create a class hierarchy for Vehicle → Car → ElectricCar.  

class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def display_info(self):
        print(f"Brand:{self.brand}, Max Speed: {self.max_speed} km/h")

class Car(Vehicle):
    def __init__(self,brand, max_speed,doors):
        super().__init__(brand,max_speed)
        self.doors = doors
    def display_info(self):
        super().display_info()
        print(f"The Doors are: {self.doors}")

class ElectricCar(Car):
    def __init__(self,brand, max_speed,doors, battery_capacity):
        super().__init__(brand, max_speed, doors)
        self.battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print(f"The Battery Capacity is: {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Hyundai", 180, 4, 75)
my_electric_car.display_info()

# (3)Implement method overriding in a base and derived class.

class People:
    def greet(self):
        print("Hello ")
class Dancer(People):
    def greet(self):
        print("Hello , I am a Dancer!!!")
student = Dancer()
student.greet()

# (4)Demonstrate multiple inheritance with two parent classes.

class Flyer:
    def fly(self):
        print("Heyy I'm Flying in the sky")

class Swimmer:
    def swim(self):
        print("Heyy I'm Swimming in the water")

class Flyingfish(Flyer,Swimmer):
    def display(self):
        print("Hello I'm a flying fish!!")

flying_fish =Flyingfish()
flying_fish.display()

# (5) Create a polymorphic function that works with different shapes.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

def print_area(shape):
    print("Area:", shape.area())

rect = Rectangle(45, 30)
circle = Circle(23)
print_area(rect)
print_area(circle)

# (6)Create a Bank system with SavingsAccount and CurrentAccount classes. 

class BankAccount:
    def __init__(self, ac_num, holder_name, balance=0):
        self.account_number = ac_num
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")
    def display_balance(self):
        print("Account Holder:", self.holder_name)
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def apply_interest(self, rate):
        interest = (rate / 100) * self.balance
        self.balance += interest
        print("Interest added:", interest)

class CurrentAccount(BankAccount):
    def overdraft(self, limit):
        self.balance += limit
        print("Overdraft limit added:", limit)

savings = SavingsAccount("NB23", "Nij", 5000)
current = CurrentAccount("CA201", "Rohit", 3000)

savings.deposit(2500)
savings.apply_interest(5)
savings.display_balance()

print()

current.withdraw(1000)
current.overdraft(2000)
current.display_balance()

# (7)Create a class with private attributes and getter/setter methods.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
person = Person("Nij", 21)
print("Name:", person.get_name())
print("Age:", person.get_age())

person.set_name("Dhoni")
person.set_age(43)

print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())

# (8) Create a Teacher and Student class to show inheritance.

class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject 
    def display_info(self):
        print(f"Teacher Name: {self.name}, Subject: {self.subject}")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")
teacher =Teacher("Nij Bhavsar","Python")
student =Student("Dhoni","A")
teacher.display_info()
student.display_info()

# (9)Create a MusicPlayer class and subclass Spotify to override play method.

class MusicPlayer :
    def __init__(self):
        pass
    def play(self,song):
        print(f"Playing song: {song}")

class Spotify(MusicPlayer):
    def play(self, song):
        print(f"Streaming song from Spotify: {song}")

spotify_player = Spotify()
spotify_player.play("Ez-Ez")

# (10)Demonstrate the use of super() in inheritance.

class Parent:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def display(self):
        super().display()
        print(f"Child Age: {self.age}")

child = Child("Ved", 12)
child.display()