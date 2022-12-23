# Steve Marin
# 12/21/22
# this program will Write a function areaOfCircle(r) that returns the area of a circle of radius r.
# problem 1

import math
def area_of_circle(r):
    area_of_circle(r*r*math.pi)
    return area_of_circle
r = float (input("enter a radius of the circle:"))
result = area_of_circle(r)
print ("What is the area of the circle", result)

# problem 3
# this program will write a Python function to multiply all the numbers in a list.
def multiplylist(my_list):
    r= 1
    for a in my_list:
        r= r * a
        return r
    list = [3,6,10,14,16]
    print("list:3,6,10,14,17")
    print("multiplication list",multiplylist(list))

# problem 2
# this program will  write a Python function to check whether a number is between 1 and 10.
def test_range(n):
    if n >= 1 and n<=10:
        print(n,"is between 1 and 10,the number is true")
    else:
     print(n,"is not between 1 and 10,the number is False")
test = int(input("enter numbers between 1 and 10 "))
test_range(test)

# problem 4
# this program will Write a Python function that takes a list of numbers and returns a new list.
def unique_list (l):
    mylist = [5,5,8,8,10,10,2,1]
    x =[]
    for a in l:
        if a not in x:
            x.append(a)
            return x
        print("The list of 5,5,8,8,10,10,2,1")
        print(unique_list([5,5,8,8,10,10,2,1]))

# problem 5
# this program will Modify this code shown
import turtle

def drawsquare (t,sz):
    for i in rangen(4):
        t.foward(sz)
        t.left(sz)
        t.left(90)
        wn = turtle.screen ()
    alex = turtle.turtle()
    alex.color("blue")
    sz= 40
    for i in range (4):
        drawsquare(alex,sz)
        sz += 15
        alex.right(135)
        alex.left(135)
        alex.color(red)
        alex.forward(10)

    wn.exitonclick()