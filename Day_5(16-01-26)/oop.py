# (1)Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0 

    def accelerate(self, increase):
        self.speed += increase
        print(f"Car accelerated. Current speed: {self.speed} km/h")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"Car slowed down. Current speed: {self.speed} km/h")


my_car = Car("Toyota", "Corolla")
my_car.accelerate(60)
my_car.brake(15)
my_car.brake(30)
my_car.accelerate(60)

#(2) Create a BankAccount class with deposit and withdraw methods.
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")
my_account = BankAccount("Nij", 10000)
my_account.deposit(6500)
my_account.withdraw(17500)

# (3)Create a Student class with a method to calculate average marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

student1 = Student("NB", [90, 89, 70, 99])
print(f"{student1.name}'s average marks: {student1.calculate_average()}")

# (4) Create a Rectangle class with methods to find area and perimeter.

class rec:
    def __init__(self, length, width ):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length * self.width)

rect = rec(11, 4)
print("The area of rectangle is:", rect.area())
print("The perimeter of rectangle is:", rect.perimeter())

# (5)Create an Employee class that displays salary details.

class employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def display_salary(self):
        print("The name is:", self.name)
        print("The Employee-id is:", self.emp_id)
        print("The salary is:", self.salary)

emp = employee("NB", 3315432, 30000)
emp.display_salary()

# (6)Create a Book class to store title, author, and price, and display details.

class book_d:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display_details(self):
        print("The Title of the book is:", self.title)
        print("The author of the book is:", self.author)
        print("The Price of the book is:", self.price)

book =  book_d("Mahabharat", "Ved Vyas", 11000)
book.display_details()

# (7) Create a Circle class to find area and circumference.

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius*self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
rad = circle(23)
print("The Area of circle is:", rad.area())
print("The Circumference of circle is:", rad.circumference())

# (8)Create a Laptop class with a method to apply discounts on price.

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price = self.price - discount_amount
        return self.price
    
lap = Laptop("Dell", "G15", 76500)
final_price = lap.apply_discount(10)

print("Brand:", lap.brand)
print("Model:", lap.model)
print("Price after discount:", final_price)

# (9)Create a Flight class with seat booking functionality.

class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = 0
    
    def book_seat(self, seats):
        if seats <= 0:
            print("Invalid Number of seats!!")
        elif self.booked_seats + seats > self.total_seats:
            print("Enough seats are not available!!")
        else:
            self.booked_seats += seats
            print(seats, "seat(s) booked successfully.")

    def available_seats(self):
        return self.total_seats - self.booked_seats
    
flight = Flight("E45121", 100)

flight.book_seat(50)
flight.book_seat(50)

print("Available seats:", flight.available_seats())

# (10)Create a Shop class with a method to add and list products.

class shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)
        print(product_name, "is added to the shop.")

    def list_products(self):
        print("Products available in", self.shop_name + ":")
        for product in self.products:
            print("-", product)

shop_n = shop("MCS")

shop_n.add_product("shorts")
shop_n.add_product("Shirt")
shop_n.add_product("Trouser")

shop_n.list_products()