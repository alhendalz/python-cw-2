my_name= input("enter your name")
my_age= input("enter your age")
print (f"my name is {my_name} and i am {my_age} years old")


first_number=int(input("enter your first number"))
second_number=int(input("enter your second number"))
operation=input("enter your operation")
if operation == "+":
    print(first_number+second_number)
elif operation == "-":
    print(first_number-second_number)
elif operation == "*":
    print(first_number*second_number)
elif operation == "/":
    print(first_number/second_number)

bus_capacity = 60
bus_capacity=int(input("enter the number of passengers"))
people_inbus=input("enter the number of people who want to ride the bus")
empty_seats = bus_capacity - people_inbus
if bus_capacity>= people_inbus:
    print(f"there is empty_seats")
elif bus_capacity < people_inbus:
    print("there is no seats")