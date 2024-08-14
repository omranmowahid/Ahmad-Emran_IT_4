
from math import *

# # 1
# class Person:
#     def __init__(self):
#         self.name = 'ahmad'
#         self.age = 20
#
#
# person = Person()
# print(person.name, '\n', person.age)

#2
# class Person:
#     def __init__(self):
#         self.name = 'ahmad'
#         self.age = 20
#
#     def greet(self):
#         print(f'hello {self.name}, how are you doing.')
#
#
# person = Person()
# person.greet()


#3
# class Car:
#     def __init__(self):
#         self.make = 'corolla'
#         self.model = '2015'
#         self.year = 2020
#
#     def details(self):
#         print(f'this is a {self.make} car, model of {self.model} ,from {self.year} year.')
#
#
# car = Car()
# car.details()

#4
# class Circle:
#     def __init__(self, radius):
#         self.r = radius
#
#     def calc_area(self):
#         print(f'the area of the circle "{self.r}" is {round(self.r ** 2 * 0.5 * pi)}')
#
#
# circle = Circle(12)
# circle.calc_area()

#5


# class Rectangle:
#     def __init__(self, length, width):
#         self.l = length
#         self.w = width
#
#     def area(self):
#         print(f'the area of rectangle is {self.l * self.w}')
#
#     def perimeter(self):
#         print(f'the per of rectangle is {self.l + self.w}')
#
#
# rectangle = Rectangle(4,5)
# rectangle.area()
# rectangle.perimeter()

#6


# class Animal:
#
#     def speak(self):
#         print("the animal is speaking")
#
#
# class Dog(Animal):
#
#     def speak(self):
#         super().speak()
#         print('i am a dog')
#
#
# class Cat(Animal):
#
#     def speak(self):
#         super().speak()
#         print('i am a cat')
#
#
# dog = Dog()
# dog.speak()
# cat = Cat()
# cat.speak()

#7
# class Shape:
#
#     def area(self):
#         print('this is an area method')
#
#
# class Square(Shape):
#     pass
#
#
# class Triangle(Shape):
#     pass
#
#
# shape = Shape()
# shape.area()
#
# square = Square()
# square.area()
#
# triangele = Triangle()
# triangele.area()

#8
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#
# employee = Employee('employee', 1000)
# manager = Manager('manager', 2000, 'IT')
#
# print(employee.name)
# print(manager.name)


#9

# class Vehicle:
#
#     def drive(self):
#         print('this vehicle is driving')


# class Bike(Vehicle):
#     def drive(self):
#         super().drive()
#         print('the bike is driving')
#
#
# class Truck(Vehicle):
#     def drive(self):
#         super().drive()
#         print('truck is driving')
#
#
# vehiclel = Vehicle()
# vehiclel.drive()
#
# bike = Bike()
# bike.drive()
#
# truck = Truck()
# truck.drive()

#10

# class Bird:
#
#     def fly(self):
#         print('the bird is flying')
#
#
# class Eagle(Bird):
#
#     def fly(self):
#         super().fly()
#         print('i am bird and can fly')
#
#
# class Penguin(Bird):
#
#     def fly(self):
#         super().fly()
#         print('i am bird and cant fly')
#
#
# bird = Bird()
# bird.fly()
#
# eagle = Eagle()
# eagle.fly()
#
# penguin = Penguin()
# penguin.fly()


#11
# class Account:
#     def __init__(self, initial_balance=0):
#         self.__balance = initial_balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return True
#         else:
#             print('deposit amount must be positive')
#             return False
#
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.__balance:
#                 self.__balance -= amount
#                 return True
#             else:
#                 print('insufficient funds')
#                 return False
#         else:
#             print('withdraw must be positive')
#             return False
#
#     def getbalance(self):
#         return self.__balance
#
#
# account = Account(100)
# print(account.getbalance())
#
# account.deposit(50)
# print(account.getbalance())
#
# account.withdraw(150)
# print(account.getbalance())
#
# account.withdraw(50)
# print(account.getbalance())
#
# '''here we cant change balance from outside directly like
# account.balance = 200
# if we didnt private it anyone can change its value from outside'''


#12
# class Book:
#     def __init__(self, initial_author='ahmad', initial_page=200, initial_title='world'):
#         self.__author = initial_author
#         self.__pages = initial_page
#         self.__title = initial_title
#
#     def get_author(self):
#         return self.__author
#
#     def set_author(self, author):
#         self.__author = author
#
#     def get_page(self):
#         return self.__pages
#
#     def set_page(self, page):
#         self.__pages = page
#
#     def get_title(self):
#         return self.__title
#
#     def set_title(self, titles):
#         self.__title = titles
#
#     def detail(self):
#         print(f'this is the book from {self.__author} it has {self.__pages} pages and the title is about {self.__title}')
#
#
# book = Book(initial_author='ahmad emran', initial_page=300, initial_title='OOP')
# book.detail()
#
#
# book.set_author('ali')
# book.set_page(200)
# book.set_title('hello world')
# book.detail()

#13
# class Laptop:
#     def __init__(self, init_brand, init_price, init_model):
#         self.__brand = init_brand
#         self.__model = init_model
#         self.__price = init_price
#
#     def discount(self, amount):    #give amount by percentage(10)'''
#
#         self.__price = self.__price - self.__price * amount/100
#         return self.__price
#
#     def detail(self):
#         return f'this is the {self.__brand} laptop, its model is {self.__model} and its price is {self.__price}'
#
#
# laptop = Laptop('dell', 10000, 'gen7')
# laptop.discount(2)
# print(laptop.detail())

# 14. Create a class BankAccount with private attributes account_number and balance. Provide
# methods to deposit, withdraw, and check the balance.

# class BankAccount:
#     def __init__(self, init_account_number, init_balance=0):
#         self.__account_number = init_account_number
#         self.__balance = init_balance
#
#     def deposit(self, amount):
#         if amount < 0:
#             print('should not negative')
#             return False
#         else:
#             self.__balance += amount
#             return True
#
#     def with_draw(self, amount):
#         if amount < 0:
#             print('should not negative')
#             return False
#         elif amount > self.__balance:
#             print('you dont have such money ')
#             return False
#         else:
#             self.__balance -= amount
#             return True
#
#     def detail(self):
#         return f'account number {self.__account_number} you have {self.__balance} in your account'
#
#
# bank_account = BankAccount('12344', 100)
# print(bank_account.detail())
# bank_account.deposit(50)
# print(bank_account.detail())
# bank_account.with_draw(150)
# print(bank_account.detail())
# bank_account.with_draw(50)
# print(bank_account.detail())

# 15. Create a class Student with private attributes name, grade, and age. Provide methods to get and
# set these attributes and a method to display the student's details.
# class Student:
#     def __init__(self, name, grade, age):
#         self.__name = name
#         self.__grade = grade
#         self.__age = age
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_grade(self, grade):
#         self.__grade = grade
#
#     def get_grade(self):
#         return self.__grade
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def details(self):
#         return f'name of sudent is {self.__name}, age {self.__age} by the grade of {self.__grade}'
#
#
# student = Student('ahmad', 'A+', 12)
# print(student.details())
#
# student.set_name('ali')
# student.set_age(13)
# student.set_grade('A')
#
# print(student.get_name(), student.get_grade(), student.get_age())
# print(student.details())


# Class Relationships and Advanced Concepts Exercises
# 16. Create a class Library with attributes name and books (a list of Book objects). Provide methods
# to add and remove books.

# class Library:
#     def __init__(self):
#         self.list = ['dari', 'pashto', 'history', 'english', 'chemistry', 'math']
#
#     def add_book(self, book):
#         if book in self.list:
#             print('we already have this book in library')
#         else:
#             self.list.append(book)
#             print('added')
#             return True
#
#     def remove_book(self, book):
#         if book not in self.list:
#             print('book is not in library')
#             return False
#
#         else:
#             self.list.remove(book)
#             print('removed')
#             return True
#
#
# library = Library()
#
# library.add_book('dari')
# library.add_book('physics')
#
# library.remove_book('biology')
# library.remove_book('physics')


# 17. Create a class School with attributes name and students (a list of Student objects). Provide
# methods to add and remove students.

# class School:
#     def __init__(self):
#         self.list = ['emran', 'munir', 'bilal', 'omar', 'ghayor', 'jasor']
#
#     def add_student(self, name):
#         if name in self.list:
#             print('we already have this student in database')
#         else:
#             self.list.append(name)
#             print('added')
#             return True
#
#     def remove_student(self, name):
#         if name not in self.list:
#             print('student is not in database')
#             return False
#
#         else:
#             self.list.remove(name)
#             print('removed')
#             return True
#
#
# database = School()
#
# database.add_student('emran')
# database.add_student('hasib')
#
# database.remove_student('sajad')
# database.remove_student('hasib')


# 18. Create a class Team with attributes name and members (a list of Person objects). Provide
# methods to add and remove members.

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name
#
#
# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.member = []
#
#     def add_member(self, person):
#         if person not in self.member:
#             self.member.append(person)
#         else:
#             print('person is in team')
#
#     def remove_member(self, person):
#         if person in self.member:
#             self.member.remove(person)
#         else:
#             print('person is not in the team')
#
#     def display_member(self):
#         if self.member:
#             return self.member
#
#
# person1 = Person('ahmad')
# person2 = Person('ali')
# person3 = Person('mohammad')
#
# team = Team('developer')
# print(team.display_member())
#
# team.add_member(person1)
# team.add_member(person2)
# team.add_member(person3)
# team.add_member(person3)
# print(team.display_member())




# 19. Create a class Company with attributes name and employees (a list of Employee objects).
# Provide methods to add and remove employees.

#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name
#
#
# class Company:
#     def __init__(self, name):
#         self.name = name
#         self.employees = []
#
#     def add_employees(self, person):
#         if person not in self.employees:
#             self.employees.append(person)
#         else:
#             print('person is in company')
#
#     def remove_employee(self, person):
#         if person in self.employees:
#             self.employees.remove(person)
#         else:
#             print('person is not in the company')
#
#     def display_employees(self):
#         if self.employees:
#             return f'{",".join(str(i) for i in self.employees)}'
#
#
# person1 = Person('ahmad')
# person2 = Person('ali')
# person3 = Person('mohammad')
#
# company = Company('facebook')
#
# company.add_employees(person1)
# company.add_employees(person2)
# company.add_employees(person3)
#
# print(company.display_employees())


# 20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods
# to add and remove animals.


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name
#
#
# class Zoo:
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#
#     def add_animal(self, person):
#         if person not in self.animals:
#             self.animals.append(person)
#         else:
#             print('person is in company')
#
#     def remove_animal(self, person):
#         if person in self.animals:
#             self.animals.remove(person)
#         else:
#             print('person is not in the company')
#
#     def display_animal(self):
#         if self.animals:
#             return f'{",".join(str(i) for i in self.animals)}'
#
#
# animal1 = Animal('dog')
# animal2 = Animal('cat')
# animal3 = Animal('monkey')
#
# zoo = Zoo('kabul zoo')
#
# zoo.add_animal(animal1)
# zoo.add_animal(animal2)
# zoo.add_animal(animal3)
#
# print(zoo.display_animal())

# 21. Create a class FileManager with methods to read from and write to a file.

# class FileManager:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def read_file(self):
#         """reads the contents of the file"""
#         try:
#             with open(self.file_path, 'r') as file:
#                 return file.read()
#         except FileNotFoundError:
#             return 'file not found'
#         except Exception as e:
#             return str(e)
#
#     def write_file(self, content):
#         try:
#             with open(self.file_path, 'w') as file:
#                 file.write(content)
#             return 'write successful'
#         except Exception as e:
#             return str(e)
#
#
# file_manager = FileManager('exampl.txt')
# print(file_manager.read_file())

# 22. Create a class Log with methods to write error messages to a log file.
# import datetime
#
#
# class Log:
#     def __init__(self, file_name='myfile.txt'):
#         self.file_name = file_name
#
#     def write_error(self, message):
#         with open(self.file_name, 'a') as log_file:
#             timestamp = datetime.datetime.now().strftime('%y-%m-%d    %H:%M:%S')
#             log_file.write(f'{timestamp} -ERROR: {message}\n')
#
#
# log = Log()
# log.write_error('this is an error message')

# 23. Create a class Config that reads configuration settings from a file and provides methods to access
# these settings.
# import configparser
#
#
# class Config:
#     def __init__(self, filename='config.ini'):
#         self.config = configparser.ConfigParser()
#         self.config.read(filename)
#
#     def get_setting(self, section, option):
#         try:
#             return self.config.get(section, option)
#         except (configparser.NoSectionError, configparser.NoOptionError) as e:
#             print(f'Error: {e}')
#             return None
#
#     def get_int_setting(self, section, option):
#         try:
#             return self.config.getint(section, option)
#         except (configparser.NoSectionError, configparser.NoOptionError, ValueError) as e:
#             print(f'Error: {e}')
#             return None
#
#     def get_float_setting(self, section, option):
#         try:
#             return self.config.getfloat(section, option)
#         except (configparser.NoSectionError, configparser.NoOptionError, ValueError) as e:
#             print(f'Error: {e}')
#             return None
#
#     def boolean_setting(self, section, option):
#         try:
#             return self.config.getboolean(section, option)
#         except (configparser.NoSectionError, configparser.NoOptionError, ValueError) as e:
#             print(f'Error: {e}')
#             return None
#
#
#
# config = Config()
# host = config.get_setting('database', 'host')
# port = config.get_int_setting('database', 'port')
# use_ssl = config.boolean_setting('database', 'use_ssl')
#
# print(f'host: {host}')
# print(f'port: {port}')
# print(f'use ssl: {use_ssl}')


# 24. Create a class Database that connects to a database and provides methods to execute queries.
# Handle exceptions if the connection fails.

# import sqlite3
# from sqlite3 import Error
#
#
# class Database:
#     def __init__(self, db_file):
#         self.db_file = db_file
#         self.conn = None
#         self.connect()
#
#     def connect(self):
#         try:
#             self.conn = sqlite3.connect(self.db_file)
#             print('connection established successfully')
#         except Error as e:
#             print(f'error connecting to the eatabase: {e}')
#
#     def execute_query(self, query, params=None):
#         try:
#             cursor = self.conn.cursor()
#             if params:
#                 cursor.execute(query, params)
#             else:
#                 cursor.execute(query)
#                 self.conn.commit()
#                 print('query executed successfully')
#         except Error as e:
#             print(f'error executing query: {e}')



# 25. Create a class Report that generates a report from data in a file. Provide methods to handle
# exceptions if the file does not exist or cannot be read.

# import os
# class Report:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def read_file(self):
#         try:
#             with open(self.file_name, 'r') as file:
#                 data = file.readlines()
#             print('file read successfully')
#             return data
#         except FileNotFoundError:
#             print(f'error: the file {self.file_name} does not exist')
#             return None
#         except IOError:
#             print(f'error: the file {self.file_name} cannot be read')
#
#     def generate_report(self):
#         data = self.read_file()
#         if data is None:
#             return 'reprot generations failed due to file read error'
#
#         report = self.process_data(data)
#         return report
#
#     def process_data(self, data):
#         report = 'report: \n'
#         for line in data:
#             report += line
#         return report
#
# if __name__ == "__main__":
#     report = Report('data.txt')
#     generated_report = report.generate_report()
#     print(generated_report)

# Real-world Application Exercises
# 26. Create a class Ticket for a movie theater with attributes movie_name, seat_number, and price.
# Provide methods to display ticket details and apply discounts.
# class Ticket:
#
#     def __init__(self, movie_name='endgame', seat_num=12, price=200):
#         self.movie_name = movie_name
#         self.seat_num = seat_num
#         self.price = price
#
#     def discount(self, amount):
#         pay = self.price - (self.price * amount / 100)
#         return f'the amount you should pay after {amount} discount is {pay}'
#
#     def ticket_detail(self):
#         return f'the movie is {self.movie_name}, your seat number is {self.seat_num} and the pay amount is {self.price}'
#
#
# ticket = Ticket()
# print(ticket.ticket_detail())
# print(ticket.discount(50))


# 27. Create a class ShoppingCart with methods to add, remove, and display items. Each item should
# be an object of a class Item with attributes name and price.

# class Item:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f'{self.name}: ${self.price:.2f}'
#
# class ShoppingCart:
#
#     def __init__(self):
#         self.items = []
#
#     def add(self, item):
#         self.items.append(item)
#         print(f'added {item.name} to the cart')
#
#     def remove(self, item_name):
#         for item in self.items:
#             if item.name == item_name:
#                 self.items.remove(item)
#                 print(f'removed {item_name} from the cart')
#                 return
#         print(f'item {item_name} vot found in the cart')
#
#     def display(self):
#         if not self.items:
#             print('the cart is empty')
#             return
#         print('items in the cart: ')
#         total_price = 0
#         for item in self.items:
#             print(f' - {item}')
#             total_price += item.price
#             print(f'total price: ${total_price:.2f}')
#
#
# cart = ShoppingCart()
# item1 = Item('apple', 0.99)
# item2 = Item('banana', 0.59)
# item3 = Item('orange', 1.29)
#
# cart.add(item1)
# cart.add(item2)
# cart.add(item3)
#
# cart.display()
#
# cart.remove('banana')
#
# cart.remove('graps')
#
# cart.display()


# 28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide
# methods to add and remove items from the menu.


# class Food:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
# class Restaurant:
#
#     def __init__(self):
#         self.menu = []
#
#     def add(self, food):
#         if food in self.menu:
#             print(f'we already have {food} in menu')
#         else:
#             self.menu.append(food)
#             print('food added')
#
#     def remove(self, food):
#         if food in self.menu:
#             self.menu.remove(food)
#             print('food removed')
#         else:
#             print('food is not in menue')
#
#     def display(self):
#         print('the menu is as this: ')
#         i = 0
#         for foods in self.menu:
#             i += 1
#             print(f'{i}: {foods}')
#
#
# food1 = Food('kabab')
# food2 = Food('qabli')
# food3 = Food('manto')
#
#
# restaurant = Restaurant()
# restaurant.add(food1)
# restaurant.add(food2)
# restaurant.add(food3)
# restaurant.display()


# 29. Create a class Flight with attributes flight_number, destination, and passengers (a list of Person
# objects). Provide methods to add and remove passengers.


# class Passenger:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
# class Flight:
#
#     def __init__(self, flight_num, destination):
#         self.flight_num = flight_num
#         self.destination = destination
#         self.names = []
#
#     def add(self, name):
#         if name in self.names:
#             print(f'we already have {name} in list')
#         else:
#             self.names.append(name)
#             print('passenger added')
#
#     def remove(self, name):
#         if name in self.names:
#             self.names.remove(name)
#             print('passenger removed')
#         else:
#             print('passenger is not in list')
#
#     def display(self):
#         print(f'the passengers is as this:   destination is {self.destination} and the number of flight is {self.flight_num}')
#         i = 0
#         for passenger in self.names:
#             i += 1
#             print(f'{i}: {passenger}')
#
#
# passenger1 = Passenger('ahmad')
# passenger2 = Passenger('ali')
# passenger3 = Passenger('mohamad')
#
#
# flight = Flight(1, 'kabul')
# flight.add(passenger1)
# flight.add(passenger2)
# flight.add(passenger3)
# flight.display()


# 30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room
# should have attributes room_number and is_occupied. Provide methods to book and check-
# out rooms.
# class Properties:
#     def __init__(self, name='ahmad',  room=0, is_occupied=True):
#         self.name = name
#         self.room = room
#         self.is_occupied = is_occupied
#
#     def __str__(self):
#         return f'{self.name}, {self.room}, {self.is_occupied}'
#
#
# class Hotel:
#     def __init__(self, properties):
#         self.rooms = {}
#         self.rooms[properties.room] = properties.name
#
#     def book(self, name, room):
#         if room in self.rooms:
#             print('this room is reserved')
#         else:
#             self.rooms[room] = name
#             print('added')
#
#     def display(self):
#         for i in self.rooms:
#             print(f'name: {self.rooms[i]} room: {i}')
#
#     def delete(self, room):
#         if room not in self.rooms:
#             print('room is not reserved')
#         else:
#             self.rooms.pop(room)
#             print('removed')
#
#
# properties = Properties('ahmad', 1)
# hotel = Hotel(properties)
# # hotel.display()
# hotel.book('ali', 2)
# # hotel.delete(1)
# hotel.display()


# GUI Application Exercises
# 36. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and
# decrement buttons.
# from tkinter import *
# window = Tk()
#
# window.minsize(500, 500)
# window.config(bg='black')
# frame = Frame(window)
# frame.pack()
# frame.config(bg='black')
# label_frame_show = LabelFrame(frame, width=100, height=100)
# label_frame_show.pack(pady=20)
# label = Label(label_frame_show, text=0, width=10, height=1, font=('modern', 40, 'bold'))
# label.pack()
#
#
# def up():
#     amount = label.cget('text')
#     label.config(text=amount + 1)
#
#
# def down():
#     if label.cget('text') < 1:
#         return
#     amount = label.cget('text')
#     label.config(text=amount - 1)
#
#
# label_frame_button = LabelFrame(frame, width=100, height=100)
# label_frame_button.pack(padx=20, pady=20)
# label_frame_button.config(bg='black')
#
# button_up = Button(label_frame_button, text='count up', font=('modern', 40, 'bold'), width=20, command=up, activebackground='black')
# button_up.pack(padx=10, pady=10)
#
# button_down = Button(label_frame_button, text='count down', font=('modern', 40, 'bold'), width=20, command=down, activebackground='black')
# button_down.pack(padx=10, pady=10)
#
#
# window.mainloop()


# 37. Create a class ToDoApp that uses tkinter to create a to-do list GUI where users can add and
# remove tasks.

#
# from tkinter import *
#
# COLOR1 = '#1A3636'
# COLOR2 = '#40534C'
# COLOR3 = '#677D6A'
# COLOR4 = '#D6BD98'
# FONT_TITLE = ('Arial', 14, 'bold')
# FONT_WRITE = ('modern', 12, 'bold')
#
# window = Tk()
# window.config(bg=COLOR1)
#
# frame = Frame(window, bg=COLOR1)
# frame.pack(expand=True, anchor='center')
# # *****************'******************************************************************************
# WIDTH_task = 100
# HEIGHT_task = 2.5
# PAD_X_task = 10
# PAD_Y_task = 2
#
# # *****************************************************************************************************
# labelframe_show = LabelFrame(frame, text='TASKS', width=200, height=200, bg=COLOR1, fg=COLOR4, font=FONT_TITLE)
# labelframe_show.pack()
#
# label_task1 = Label(labelframe_show, text='TASK 1', font=FONT_WRITE, fg=COLOR4, bg=COLOR1)
# label_task1.grid(column=0, row=0, pady=PAD_Y_task, padx=PAD_X_task)
# text_task1 = Text(labelframe_show, height=HEIGHT_task, width=WIDTH_task, font=FONT_TITLE, fg=COLOR4, bg=COLOR1,
#                   pady=PAD_Y_task, padx=PAD_X_task)
# text_task1.grid(column=1, row=0, pady=PAD_Y_task, padx=PAD_X_task)
#
# label_task2 = Label(labelframe_show, text='TASK 2', font=FONT_WRITE, fg=COLOR4, bg=COLOR1)
# label_task2.grid(column=0, row=1, pady=PAD_Y_task, padx=PAD_X_task)
# text_task2 = Text(labelframe_show, height=HEIGHT_task, width=WIDTH_task, font=FONT_TITLE, fg=COLOR4, bg=COLOR1,
#                   pady=PAD_Y_task, padx=PAD_X_task)
# text_task2.grid(column=1, row=1, pady=PAD_Y_task, padx=PAD_X_task)
#
# label_task3 = Label(labelframe_show, text='TASK 3', font=FONT_WRITE, fg=COLOR4, bg=COLOR1)
# label_task3.grid(column=0, row=2)
# text_task3 = Text(labelframe_show, height=HEIGHT_task, width=WIDTH_task, font=FONT_TITLE, fg=COLOR4, bg=COLOR1,
#                   pady=PAD_Y_task, padx=PAD_X_task)
# text_task3.grid(column=1, row=2, pady=PAD_Y_task, padx=PAD_X_task)
#
# label_task4 = Label(labelframe_show, text='TASK 4', font=FONT_WRITE, fg=COLOR4, bg=COLOR1)
# label_task4.grid(column=0, row=3)
# text_task4 = Text(labelframe_show, height=HEIGHT_task, width=WIDTH_task, font=FONT_TITLE, fg=COLOR4, bg=COLOR1,
#                   pady=PAD_Y_task, padx=PAD_X_task)
# text_task4.grid(column=1, row=3, pady=PAD_Y_task, padx=PAD_X_task)
#
# label_task5 = Label(labelframe_show, text='TASK 5', font=FONT_WRITE, fg=COLOR4, bg=COLOR1)
# label_task5.grid(column=0, row=4)
# text_task5 = Text(labelframe_show, height=HEIGHT_task, width=WIDTH_task, font=FONT_TITLE, fg=COLOR4, bg=COLOR1,
#                   pady=PAD_Y_task, padx=PAD_X_task)
# text_task5.grid(column=1, row=4, pady=PAD_Y_task, padx=PAD_X_task)
#
# label_task6 = Label(labelframe_show, text='TASK 6', font=FONT_WRITE, fg=COLOR4, bg=COLOR1)
# label_task6.grid(column=0, row=5)
# text_task6 = Text(labelframe_show, height=HEIGHT_task, width=WIDTH_task, font=FONT_TITLE, fg=COLOR4, bg=COLOR1,
#                   pady=PAD_Y_task, padx=PAD_X_task)
# text_task6.grid(column=1, row=5, pady=PAD_Y_task, padx=PAD_X_task)
#
# label_task7 = Label(labelframe_show, text='TASK 7', font=FONT_WRITE, fg=COLOR4, bg=COLOR1)
# label_task7.grid(column=0, row=6)
# text_task7 = Text(labelframe_show, height=HEIGHT_task, width=WIDTH_task, font=FONT_TITLE, fg=COLOR4, bg=COLOR1,
#                   pady=PAD_Y_task, padx=PAD_X_task)
# text_task7.grid(column=1, row=6, pady=PAD_Y_task, padx=PAD_X_task)
#
# label_task8 = Label(labelframe_show, text='TASK 8', font=FONT_WRITE, fg=COLOR4, bg=COLOR1)
# label_task8.grid(column=0, row=7)
# text_task8 = Text(labelframe_show, height=HEIGHT_task, width=WIDTH_task, font=FONT_TITLE, fg=COLOR4, bg=COLOR1,
#                   pady=PAD_Y_task, padx=PAD_X_task)
# text_task8.grid(column=1, row=7, pady=PAD_Y_task, padx=PAD_X_task)
#
# # add***********************************************************************************************
# entry_var = StringVar()
#
#
# def add():
#     popup = Toplevel(bg=COLOR3)
#     label = Label(popup, text='WHICH TASK TO ADD IN', bg=COLOR3, fg=COLOR2, font=FONT_TITLE)
#     label.grid(column=0, row=0)
#
#     def radio_output():
#         user_input = radio_state.get()
#         if user_input == 1:
#             user_entry = entry.get()
#             text_task1.insert('end', user_entry)
#             text_task1.insert('end', '\n')
#             entry_var.set("")
#         elif user_input == 2:
#             user_entry = entry.get()
#             text_task2.insert('end', user_entry)
#             text_task2.insert('end', '\n')
#             entry_var.set("")
#         elif user_input == 3:
#             user_entry = entry.get()
#             text_task3.insert('end', user_entry)
#             text_task3.insert('end', '\n')
#             entry_var.set("")
#         elif user_input == 4:
#             user_entry = entry.get()
#             text_task4.insert('end', user_entry)
#             text_task4.insert('end', '\n')
#             entry_var.set("")
#         elif user_input == 5:
#             user_entry = entry.get()
#             text_task5.insert('end', user_entry)
#             text_task5.insert('end', '\n')
#             entry_var.set("")
#         elif user_input == 6:
#             user_entry = entry.get()
#             text_task6.insert('end', user_entry)
#             text_task6.insert('end', '\n')
#             entry_var.set("")
#         elif user_input == 7:
#             user_entry = entry.get()
#             text_task7.insert('end', user_entry)
#             text_task7.insert('end', '\n')
#         elif user_input == 8:
#             user_entry = entry.get()
#             text_task8.insert('end', user_entry)
#             text_task8.insert('end', '\n')
#             entry_var.set("")
#         popup.destroy()
#
#     radio_state = IntVar()
#     radio_button1 = Radiobutton(popup, text='TASK 1', value=1, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=0, row=1, padx=40, pady=20)
#     radio_button2 = Radiobutton(popup, text='TASK 2', value=2, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=1, row=1, padx=40, pady=20)
#     radio_button3 = Radiobutton(popup, text='TASK 3', value=3, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=2, row=1, padx=40, pady=20)
#     radio_button4 = Radiobutton(popup, text='TASK 4', value=4, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=3, row=1, padx=40, pady=20)
#     radio_button5 = Radiobutton(popup, text='TASK 5', value=5, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=0, row=2, padx=40, pady=20)
#     radio_button6 = Radiobutton(popup, text='TASK 6', value=6, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=1, row=2, padx=40, pady=20)
#     radio_button7 = Radiobutton(popup, text='TASK 7', value=7, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=2, row=2, padx=40, pady=20)
#     radio_button8 = Radiobutton(popup, text='TASK 8', value=8, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=3, row=2, padx=40, pady=20)
#
#     button = Button(popup, text='Ok', command=radio_output, width=30, font=FONT_TITLE, bg=COLOR2, fg=COLOR3)
#     button.grid(column=2, row=3)
#
#
# # delete**********************************************************************************************
#
#
# def delete():
#     popup = Toplevel(bg=COLOR3)
#     label = Label(popup, text='WHICH ONE YOU WANT TO DELETE', bg=COLOR3, fg=COLOR2, font=FONT_TITLE)
#     label.grid(column=0, row=0)
#
#     def get_value():
#         user_input = radio_state.get()
#         if user_input == 1:
#             text_task1.delete('1.0', 'end')
#         elif user_input == 2:
#             text_task2.delete('1.0', 'end')
#         elif user_input == 3:
#             text_task3.delete('1.0', 'end')
#         elif user_input == 4:
#             text_task4.delete('1.0', 'end')
#         elif user_input == 5:
#             text_task5.delete('1.0', 'end')
#         elif user_input == 6:
#             text_task6.delete('1.0', 'end')
#         elif user_input == 7:
#             text_task7.delete('1.0', 'end')
#         elif user_input == 8:
#             text_task8.delete('1.0', 'end')
#         popup.destroy()
#
#     radio_state = IntVar()
#     radio_button1 = Radiobutton(popup, text='TASK 1', value=1, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=0, row=1, padx=40, pady=20)
#     radio_button2 = Radiobutton(popup, text='TASK 2', value=2, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=1, row=1, padx=40, pady=20)
#     radio_button3 = Radiobutton(popup, text='TASK 3', value=3, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=2, row=1, padx=40, pady=20)
#     radio_button4 = Radiobutton(popup, text='TASK 4', value=4, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=3, row=1, padx=40, pady=20)
#     radio_button5 = Radiobutton(popup, text='TASK 5', value=5, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=0, row=2, padx=40, pady=20)
#     radio_button6 = Radiobutton(popup, text='TASK 6', value=6, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=1, row=2, padx=40, pady=20)
#     radio_button7 = Radiobutton(popup, text='TASK 7', value=7, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=2, row=2, padx=40, pady=20)
#     radio_button8 = Radiobutton(popup, text='TASK 8', value=8, variable=radio_state, bg=COLOR3, font=FONT_TITLE,
#                                 fg=COLOR2).grid(column=3, row=2, padx=40, pady=20)
#
#     button = Button(popup, text='ok', command=get_value, width=30, font=FONT_TITLE, bg=COLOR2, fg=COLOR3)
#     button.grid(column=2, row=3)
#
#
# # ***********************************************************************************************
#
#
# labelframe_entry = LabelFrame(frame, text='WRITE YOUR TASK', bg=COLOR1, fg=COLOR4, font=FONT_TITLE)
# labelframe_entry.pack(padx=20, pady=10)
#
# button_add = Button(labelframe_entry, text='ADD', width=10, height=2, command=add, bg=COLOR1, font=FONT_WRITE,
#                     fg=COLOR4)
# button_add.grid(column=0, row=0)
#
# button_del = Button(labelframe_entry, text='DELETE', width=10, height=2, command=delete, bg=COLOR1, font=FONT_WRITE,
#                     fg=COLOR4)
# button_del.grid(column=2, row=0)
#
# entry = Entry(labelframe_entry, textvariable=entry_var, width=100, font=FONT_TITLE, fg=COLOR4, bg=COLOR1)
# entry.grid(column=1, row=0, ipady=20, padx=10, pady=3)
#
# window.mainloop()



# 38. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.
# from tkinter import *
#
# BUTTON_WIDTH = 12
# BUTTON_HEIGHT = 3
# BUTTON_PADX = 10
# BUTTON_PADY = 10
# BUTTON_FONT = ('Arial', 19, 'bold')
# SHOW_FONT = ('Arial', 20, 'bold')
# COLOR4 = '#A0937D'
# COLOR_SGN = '#ff8a22'
# COLOR_BG = '#161616'
# COLOR_BUT = '#444444'
# # *********************************
# window = Tk()
# window.title('calculator')
# window.config(bg=COLOR_BG)
#
# frame = Frame(window, bg=COLOR_BG)
# frame.pack()
# # **********************************
# label_frame_show = LabelFrame(frame)
# label_frame_show.pack()
#
# label_frame_show_result = LabelFrame(label_frame_show, bg=COLOR_BG, fg='white', width=100, height=100)
# label_frame_show_result.grid(column=2, row=0)
# label_show_result = Label(label_frame_show_result, width=8, height=2, text='', anchor='e', justify=RIGHT, bg=COLOR_BG, fg='white', font=('arial', 40, 'bold'))
# label_show_result.pack(padx=20)
#
#
#
# label_frame_show_num = LabelFrame(label_frame_show, bg=COLOR_BG, fg='white', width=50, height=100)
# label_frame_show_num.grid(column=1, row=0)
# label_show_num = Label(label_frame_show_num, width=13, height=2, text='', anchor='e', justify=RIGHT, bg=COLOR_BG, fg='white', font=('arial', 40, 'bold'))
# label_show_num.pack(padx=30)
#
# label_frame_show_history = LabelFrame(label_frame_show, bg=COLOR_BG, fg='white', width=50, height=100)
# label_frame_show_history.grid(column=0, row=0)
# label_show_history = Label(label_frame_show_history, width=3, height=2, text='', anchor='e', justify=RIGHT, bg=COLOR_BG, fg='white', font=('arial', 40, 'bold'))
# label_show_history.pack(padx=20)
#
#
# #**********************************
#
# label_frame_calc = LabelFrame(frame, height=360, width=340, bg=COLOR_BG)
# label_frame_calc.pack(padx=20, pady=20)
# new_text = 0
# a = 0
# list_operation = []
# history = None
#
#
# def append_digit(digit):
#     current_text = label_show_num.cget("text")
#     global new_text
#     new_text = current_text + str(digit)
#     label_show_num.config(text=new_text)
#
#
# def add():
#     global a
#     global list_operation
#     global history
#     list_operation.append('+')
#     label_show_num.config(text="")
#     history = str(new_text) + list_operation[-1]
#     label_show_history.config(text=history)
#     a = int(new_text)
#
#
# def subtract():
#     global a
#     global list_operation
#     global history
#     list_operation.append('-')
#     label_show_num.config(text="")
#     history = str(new_text) + list_operation[-1]
#     label_show_history.config(text=history)
#     a = int(new_text)
#
#
# def div():
#     global a
#     global list_operation
#     global history
#     list_operation.append('/')
#     label_show_num.config(text="")
#     history = str(new_text) + list_operation[-1]
#     label_show_history.config(text=history)
#     a = int(new_text)
#
#
# def mul():
#     global a
#     global list_operation
#     global history
#     list_operation.append('*')
#     label_show_num.config(text="")
#     history = str(new_text) + list_operation[-1]
#     label_show_history.config(text=history)
#     a = int(new_text)
#
# def equal():
#     global new_text
#     second = new_text
#     if '+' in list_operation[-1]:
#         b = a + int(new_text)
#         label_show_num.config(text=b)
#         list_operation.clear()
#         new_text = b
#     elif '-' in list_operation[-1]:
#         b = a - int(new_text)
#         label_show_num.config(text=b)
#         list_operation.clear()
#         new_text = b
#     elif '/' in list_operation[-1]:
#         b = a // int(new_text)
#         label_show_num.config(text=b)
#         list_operation.clear()
#         new_text = b
#     elif '*' in list_operation[-1]:
#         b = a * int(new_text)
#         label_show_num.config(text=b)
#         list_operation.clear()
#         new_text = b
#     label_show_history.config(text='')
#     label_show_result.config(text=(history + str(second) + '=' + str(new_text) ))
#
#
# def c():
#     global new_text
#     new_text = 0
#     label_show_num.config(text='')
#
#
# def button():
#     button1 = Button(label_frame_calc, text=1, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(1), bg=COLOR_BUT, fg='white')
#     button1.grid(column=0, row=0, padx=10, pady=10)
#
#     button2 = Button(label_frame_calc, text=2, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(2), bg=COLOR_BUT, fg='white')
#     button2.grid(column=1, row=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button3 = Button(label_frame_calc, text=3, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(3), bg=COLOR_BUT, fg='white')
#     button3.grid(column=2, row=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button_add = Button(label_frame_calc, text='+', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=add, bg=COLOR_SGN, fg='white')
#     button_add.grid(column=3, row=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
#     #*******************************************
#     button4 = Button(label_frame_calc, text=4, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(4), bg=COLOR_BUT, fg='white')
#     button4.grid(column=0, row=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button5 = Button(label_frame_calc, text=5, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(5), bg=COLOR_BUT, fg='white')
#     button5.grid(column=1, row=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button6 = Button(label_frame_calc, text=6, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(6), bg=COLOR_BUT, fg='white')
#     button6.grid(column=2, row=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button_sub = Button(label_frame_calc, text='-', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=subtract, bg=COLOR_SGN, fg='white')
#     button_sub.grid(column=3, row=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
#     # *******************************************
#     button7 = Button(label_frame_calc, text=7, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(7), bg=COLOR_BUT, fg='white')
#     button7.grid(column=0, row=2, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button8 = Button(label_frame_calc, text=8, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(8), bg=COLOR_BUT, fg='white')
#     button8.grid(column=1, row=2, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button9 = Button(label_frame_calc, text=9, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(9), bg=COLOR_BUT, fg='white')
#     button9.grid(column=2, row=2, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button_div = Button(label_frame_calc, text='/', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=div, bg=COLOR_SGN, fg='white')
#     button_div.grid(column=3, row=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
#     # *******************************************
#     button0 = Button(label_frame_calc, text=0, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=lambda: append_digit(0), bg=COLOR_BUT, fg='white')
#     button0.grid(column=1, row=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button_equal = Button(label_frame_calc, text='=', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=equal, bg=COLOR_SGN, fg='white')
#     button_equal.grid(column=2, row=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button_equal = Button(label_frame_calc, text='C', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=c, bg=COLOR_SGN, fg='white')
#     button_equal.grid(column=0, row=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
#     button_equal = Button(label_frame_calc, text='*', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=mul, bg=COLOR_SGN, fg='white')
#     button_equal.grid(column=3, row=2, padx=BUTTON_PADX, pady=BUTTON_PADY)
#
# button()
#
# window.mainloop()

# 39. Create a class LoginApp that uses tkinter to create a login form GUI.
# from tkinter import *
# from tkinter import messagebox
#
#
# class Login:
#     def __init__(self):
#         self.window = Tk()
#         self.window.config(bg='#333333')
#         self.window.minsize(200, 300)
#         self.frame = Frame(self.window, bg='#333333')
#         self.frame.pack(padx=40, pady=80)
#         self.window.minsize(500, 500)
#         self.label_login = Label(self.frame, bg='#333333', text='login', font=('Arial', 45, 'bold'), fg='green')
#         self.label_login.grid(column=1, row=0, pady=45)
#         self.label_username = Label(self.frame, text='USER NAME', fg='white', font=('modern', 17, 'bold'), bg='#333333')
#         self.label_username.grid(column=0, row=1, pady=20, padx=10)
#         self.entry_username = Entry(self.frame, width=35, font=('modern', 17, 'bold'))
#         self.entry_username.grid(column=1, row=1, ipady=8)
#         self.label_pass = Label(self.frame, text='PASSWORD', fg='white', font=('modern', 17, 'bold'), bg='#333333')
#         self.label_pass.grid(column=0, row=2, pady=10, padx=10)
#
#         self.entry_pass = Entry(self.frame, width=35, show='*', font=('modern', 17, 'bold'))
#         self.entry_pass.grid(column=1, row=2, ipady=8)
#
#         self.button_login = Button(self.frame, text='login', fg='white', font=('Arial', 25, 'bold'), bg='green', command=self.login)
#         self.button_login.grid(column=1, row=3, pady=45)
#         self.window.mainloop()
#
#         self.mainloop()
#     def login(self):
#         user_name = 'emran'
#         password = '786 Emran'
#         if self.entry_username.get() == user_name and self.entry_pass.get() == password:
#             messagebox.showinfo(title='valid', message='entered successfully')
#         else:
#             messagebox.showerror(title='invalid', message='invalid username or password')
#
#
#
# login = Login()


# 40. Create a class WeatherApp that uses tkinter to create a weather information GUI

# from ttkbootstrap import *
# from PIL import Image, ImageTk
# window = Window()
# frame = Frame(window)
# frame.pack()
# # ************************** def search
#
# def search():
#     info_lbl.config(text=f"Weather forecast for {entry.get()}:\n\n\n\n\nSunny\nTemperature: 25°C\nHumidity: 50%\nWind: 10 km/h")
#
#
# # ########################## up frame
# labelframe_up = LabelFrame(frame, width=700, height=130)
# labelframe_up.grid_propagate(0)
# labelframe_up.grid(row=0, column=0)
#
# city_lbl = Label(labelframe_up, text='City Name', font=('arial', 30, 'bold'))
# city_lbl.grid(column=0, row=0, padx=30, pady=20)
#
# entry = Entry(labelframe_up, width=5, font=('arial', 40, 'bold'))
# entry.grid(column=1, row=0, padx=30, pady=20)
#
# search_btn = Button(labelframe_up, text='Search', command=search)
# search_btn.grid(column=2, row=0, padx=30, pady=20)
#
# # ########################## down frame
# labelframe_down = LabelFrame(frame, width=900, height=500)
# labelframe_down.grid_propagate(0)
# labelframe_down.grid(row=1, column=0)
#
# info_lbl = Label(labelframe_down, width=30, anchor='center', font=('arial', 15, 'bold'))
# info_lbl.grid_propagate(0)
# info_lbl.grid(column=0, row=0, padx=70)
#
# img = Image.open('cloud1.png')
# img1 = ImageTk.PhotoImage(img)
# image_lbl = Label(labelframe_down, image=img1)
# image_lbl.grid_propagate(0)
# image_lbl.grid(column=1, row=0, padx=100)
#
#
# window.mainloop()























