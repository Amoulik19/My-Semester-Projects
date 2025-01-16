#Aarav Moulik
#12/12/24
#Period 1
#Ticket Generator

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")

#Main
#1. Introduction (Welcoem to the Six Flags Ticket Generator)
print("Welcome to Six Flags Ticket Generator")    
#2. Collect all of the pertinent information
#Name
name = input("Enter your full name:")
#Age
age = int(input("Enter your age:"))
#Day of Week
dayofweek = input("What day of the week are you visiting?:")
#Coupon code
coupon = input("Enter any coupon codes:")
#3. Algorithms for setting the price go here
#if statements
if age<= 3:
    price = 0
elif age >=4 and age <= 17 and dayofweek == "Saturday" or dayofweek == "Sunday":
    price = 100
elif age >=4 and age <=17 and dayofweek == "Monday" or dayofweek == "Tuesday" or dayofweek == "Wednesday" or dayofweek == "Thursday" or dayofweek == "Friday":
    price = 50
elif age>=18:
    price = 100
if age >=4 and age <=17 and dayofweek == "Sunday" and coupon == "SUNDAY10":
    price = price - 10
if age >=4 and age <=17 and dayofweek == "Friday" and coupon == "FREEFRIDAY":
    price = 0
#4. Generate the ticket.
draw_ticket(name, price, dayofweek, 0)
