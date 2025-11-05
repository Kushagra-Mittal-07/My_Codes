#f-string(Easy way for using print stamtement)
'''
a = int(input("Enter number1:"))
b = int(input("Enter number2:")) 
name = input("Enter your name:")

print(f"Hello,{name} ,Good morning\nThe sum of {a} and {b} is {a+b}")
'''


#Sum of numbers
''' 
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
sum = a+b
print("Sum of the number is:",sum)
'''


#Area of square
'''
a = float(input("Enter the side of square:"))
area = a**2                                       #area = a*a
print("The area of the square is:",area)
'''


#Average
'''
a = float(input("Enter number 1:"))
b = float(input("Enter number 2:"))
avg = (a + b) / 2
print("The average of 2 numbers is:",avg)
'''


#boolean
'''
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
print(a>=b)
'''


#String
'''
str = input("Enter your firt name :")
print("Hello",str)
print("Length of your first name is:",len(str))
'''


#Occurence
'''
str = "$$bygyvb$$GGC$CEC$CC%C$EC$$$C"
print("Number of occurences of $ sign is:",str.count("$"))
'''


#loops driving license
'''
age = int(input("Enter your age: "))

if(age>=18) and(age>90):
    print("You are eligible for driving license")


elif(age<18) and (age>0):
    print("You are not eligible for driving license")


elif(age<=0):
    print("You are not even born Yet!")


elif(age>=90):
    print("You sure you can drive")


else:
    print("Age should be in integer")                    # no use as writing non integers will give error
'''


#Check for even or odd
'''
num = int(input("Enter a number: "))

if(num % 2 == 0):
    print("Entered number is Even")


else:
    print("Entered number is Odd")
'''    


#To find greatest between 3 number
'''
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if(a>b) and (a>c):
    print("Number 1 is the greatest number:",a)
    
elif(b>a) and (b>c):
    print("Number 2 is the greatest number:",b)    

else:
    print("Number 3 is the greatest number:",c)
'''    


#List of your favourite movies
'''
print("List of your favourite movies")

n1 = input("Enter your 1st favourite movie:")
n2 = input("Enter your 2nd favourite movie:")
n3 = input("Enter your 3rd favourite movie:")

movie = [n1 , n2 , n3]

print(movie)
'''


#Palindrome Check#
'''
list1 = [1,2,3,2,1]

clist1 = list1.copy()
clist1.reverse()

if(clist1 == list1):
    print("The string is palindrome")
    
else:
    print("Not palindrome")    
'''


#Dictionary 
'''
word_mean = {
    "table" : ["a piece of furniture" , "list of facts & figures"],
    "cat" : "small animal",
    3 : "fghj",
    "tuple" : ('sdzfvx'),
} 

print(word_mean)
'''


#Sets
'''
subject = {
    "python", "java", "c", "c++", "java", "c", "c++", "python", "javascript"
}

n1 = (len(subject))
print("Minimum number of classes needed are:",n1)
print("Name of the classes are:-")
print(subject)
'''


#table using range
'''
n = int(input("Enter number whose table is to be printed:"))

for i in range(1 , 11 , 1):
    print(i*n)
'''


#How to alter User define function
#Default parameters
#Example
'''
def clc_sum(a = 1 , b = 1):
    print(a+b)
    return a+b

clc_sum()#Now if i dont give any value of any one or both then it will automatically take default values assigned above
'''
'''
def clc_sum(a , b = 1):
    print(a+b)
    return a+b

clc_sum(1)
'''


#How to alter inbuilt function
#print statement
#Example
'''
print("Hello","World") #comma gives a space between both
'''
'''
print("Hello",end=(" ")) #If we want them both in one line then we can use end sttement in first print statement
print("World")
'''


#Function
'''
variables = ["a" , "s" , "d" , "f" , "g"]
numbers = ["1" , "2" , "3" , "4" , "5" , "6"]

def print_len(list):
    print(len(list))
    
print_len(variables)
print_len(numbers)
'''


#Function
'''
variables = ["a" , "s" , "d" , "f" , "g"]
numbers = ["1" , "2" , "3" , "4" , "5" , "6"]

def print_list(list):
    for i in list:
        print(i, end = "\t")
        
print_list(variables)
print("\n")
print_list(numbers)
'''


#Function (Factorial)
'''
n = int(input("Enter number whose factorial is needed:"))
# n = 5

def print_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print(fact)
        # return fact

print_fact(n)
'''


#Function (Even or Odd)
'''
num = int(input("Enter any number:"))

def even_odd(n):
    if(n%2 == 0):
        print("Even")
        
    else:
        print("Odd")
        

even_odd(num)
'''


#Recursion (Factorial)
'''
num = int(input("Enter the number whose factorial is needed:"))

def fact(n):
    if(n == 0 or n == 1):
        return 1
    return n * fact(n - 1)
    

print(fact(num))
'''


#File I/O
'''
with open("file.txt" , "w") as f:
    f.write("Hi!Everyone\nWe are learning File I/O\n")
    f.write("Using JAVA\nI like programing on JAVA")
'''   


#File I/O(Replace)
'''
with open("file.txt" , "r") as f:
    data = f.read()

new_data = data.replace("JAVA" , "Python")
print(new_data)
   
with open("file.txt" , "w") as f:
    f.write(new_data)
'''

########################**************OOPs***************###########################

'''
#OOPs 
class student :                      #THIS IS OUUR CLASS
    student = "karan"
    
s1 = student()            # THIS IS OUR OBJECT
print(s1)

s2 = student()            # THIS IS OUR OBJECT
print(s2)
'''


'''
class student:
    name = "karan"
    marks = "79"
    
s1 = student()
print(s1.name)

s2 = student()
print(s2.marks)
'''


#__init__ function 
#All clases have a function called __init__() , which always execute when object is being initiated
'''
class student:
    def __init__(self , name):
        self.name = name
        print("Adding new student to the database....")

s1 = student("Kush")
print(s1.name)

s2 = student("Luv")
print(s2.name)
'''


#Adding element in a list
'''
fruits = []

f1 = input("Enter Fruit name: ")
fruits.append(f1)
f2 = input("Enter Fruit name: ")
fruits.append(f2)
f3 = input("Enter Fruit name: ")
fruits.append(f3)
f4 = input("Enter Fruit name: ")
fruits.append(f4)
f5 = input("Enter Fruit name: ")
fruits.append(f5)
f6 = input("Enter Fruit name: ")
fruits.append(f6)
f7 = input("Enter Fruit name: ")
fruits.append(f7)

print(fruits)
'''


#Adding and sorting marks in a list
'''
marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort()

print(marks)
'''


#List methods
'''
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1, 34,62, 2, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
# value = l1.pop(3)
# print(value)
# print(l1)
'''


#Tuple methods
'''
a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))
'''


#Word meaning using dictionary
'''
words = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat"
}

word = input("Enter the word you want meaning of(madad , kursi , billi): ")

print(words[word])
'''


#Addition of elements in set
'''
s = set()
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  

print(s)
'''


#How set see different types of datatype
'''
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))
print(s)
'''


#Adding elements in a dictionary
'''
d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)
'''


#Dictionary methods
'''
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Renuka": 100})
print(marks)

print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error
'''


#Set methods
'''
s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))
'''


#Pass / Fail  (Using if else statement)
'''
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))


total_percentage = (marks1 + marks2 + marks3)/3

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congrats! You passed with:", round(total_percentage , 2))

else:
    print("You failed, try again next year:", round(total_percentage , 2))
'''


#Factorial of number   (Using for loop)
'''
n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")
'''


#Star pyramid stucture   (Using for loop)
'''
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")
'''


#Star square structure
'''
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")
'''


#Reverse table    (Using for loop)
'''
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}")
'''


#To print multiplication tables in a files in a folder
'''
def gen_tables(n):
    table = ""
    for i in range(1 , 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"Tables/table_{n}.txt","w") as f:
        f.write(table)


for i in range(2 , 21):
    gen_tables(i)
'''


#Replacing a word in a file (converting whole file to lowercase)
'''
word = "donkey"

with open("Donkey.txt" , "r") as f:
    content = f.read()

content = content.lower()

contentnew = content.replace(word , "######")


with open("Donkey.txt" , "w") as f:
    f.write(contentnew)
'''

#The real donkey text without ######
'''
The donkey saw another donkey eating grass near the donkey.
One donkey kicked another donkey for touching his donkey friend.
Donkey after donkey walked down the dusty donkey-filled village road.
A group of donkey lovers rescued a sick donkey yesterday.
Donkey shelters are now building new donkey barns for donkeys.
Every donkey deserves love, food, water, and proper donkey care.
The donkey caretaker brushed the donkey with a donkey comb.
In some stories, donkey heroes save villages using donkey brains.
Children laughed when the baby donkey followed a robot donkey.
Donkey racing has become a famous donkey sport in town.
Old donkey legends tell of flying donkey spirits helping donkeys.
Farmers trained the donkey using donkey treats and donkey rewards.
Donkey noises echoed across the donkey farm near the donkey.
A donkey museum showcases ancient donkey art and donkey tools.
During winter, every donkey wears a donkey jacket for warmth.
Donkey birthdays are celebrated with donkey cake and donkey balloons.
Tourists ride a donkey up the hill on donkey trails.
The wise donkey taught young donkeys how donkey life works.
In dreams, a magical donkey grants wishes to donkeys only.
Long live the donkey, strongest and kindest of all donkeys.
'''

#******IMPORTANT******
#Replacing a word in a file (Without converting whole file to lowercase)(chatgpt) 
'''
import re  #This is Python's regular expression module

word = "donkey"

#Step 1: Open the file and read the content
with open("donkey_nolowercase.txt", "r") as f:
    content = f.read()

#Step 2: Replace all forms of "donkey" with "######"
#re.sub() finds all case versions of "donkey" and replaces them
#all case version like -> "Donkey" "DonKey" "DONKEY" etc...
contentnew = re.sub(word, "######", content, flags=re.IGNORECASE)
#re.sub(pattern = word, replacement = "######", string = content, flags=re.IGNORECASE)

#For line no. 662
# "In the text called content, find every version of the word donkey 
# (no matter the uppercase or lowercase), and replace it with ######.
# Store the result in contentnew."

# flags=re.IGNORECASE
# This is the key part that makes it case-insensitive.
# It tells Python: "Don't care if it's donkey, Donkey, DONKEY, etc. "
# "Just treat them all as the same."


# Step 3: Write the new content back to the file
with open("donkey_nolowercase.txt", "w") as f:
    f.write(contentnew)
'''


#To copy content of one file to another file
'''
with open("test.txt" , "r") as f:
    content1 = f.read()

with open("test_copy.txt" , "w") as f:
    f.write(content1)
'''


#To check if a word is present in a file 
'''
with open("log.txt" , "r") as f:
    content = f.read()

if("python" in content):
    print("Python is present in the file")

else:
    print("Python is not present in the file")
'''


#To print the line number in which word is present
'''
with open("log.txt" , "r") as f:
    lines = f.readlines()


lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present in file at line number:{lineno}")
        break
    lineno += 1

else:
    print("No python is not present in file")
'''


#To wipe out content of a file
'''
with open("wiped_out.txt" , "w") as f:
    print("")
'''


#***********OOP's in Python************
#Class attribute
'''
class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


Kush = Employee()
Kush.name = "Kush" # This is an instance attribute
print(Kush.name, Kush.language, Kush.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class
'''


#preference of instance attri. over class attri.
'''
class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


Kush = Employee()
Kush.language = "Python"       # This is an instance attribute
print(Kush.language, Kush.salary)

rohan = Employee()
print(rohan.salary, rohan.language)
#Instance attribute take preference over class attribute during assignment and retrival of data
'''


#Self attribute
'''
class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def get_info(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    def greet(self):
        print("Hello, Good Morning")

Kush = Employee()
Kush.name = "Kushagra Mittal"
Kush.greet()
Kush.get_info()
'''

#Static method
'''
class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def get_info(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod         #now we do not need the self in greet()
    def greet():          #we used static here as there was nothing self.xyz in print
        print("Hello, Good Morning")

Kush = Employee()
Kush.name = "Kushagra Mittal"
Kush.greet()
Kush.get_info()
'''


#__init__() function
'''
class Employee: 
    language = "Python" 
    salary = 120000

    def __init__(self , name , salary , lang): #it is a dunder method therefore it is automatically called whenever a xyz = Employee() function is written
        self.name = name
        self.salary = salary
        self.lang = lang
        print("Creating a new class")

    def get_info(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod         
    def greet():          
        print("Hello, Good Morning")

Kush = Employee("Kushagra Mittal" , 2400000 , "JAVA")
Kush.greet()
print(f"Name = {Kush.name}\nSalary = {Kush.salary}\nLanguage = {Kush.lang}")
# Kush.name = "Kushagra Mittal"

# Kush.get_info()
'''


#Storing info of programmers working at a company
'''
class programmer:
    company = "Microsoft"
    def __init__(self , name , salary , emp_code):
        self.name = name
        self.salary = salary
        self.emp_code = emp_code

a = programmer("Kushagra Mittal" , 4800000 , "A001")
print(a.name , a.salary , a.emp_code , a.company)
print("\n")
a = programmer("Kush Mittal" , 4800000 , "A002")
print(a.name , a.salary , a.emp_code , a.company)
print("\n")
a = programmer("Kush" , 4800000 , "A003")
print(a.name , a.salary , a.emp_code , a.company)
print("\n")
'''


#Calculator for square , cube , square root
'''
class calculator:
    def __init__(self , n):
        self.n = n
    
    def square(self):
        print(f"The square of the number is {self.n*self.n}")
    def cube(self):
        print(f"The cube of the number is {self.n*self.n*self.n}")
    def square_root(self):
        print(f"The square_root of the number is {round(self.n**(1/2) , 3)}")

num = int(input("Enter the number:"))
a = calculator(num)

print("Enter 1 if you want square of number")
print("Enter 2 if you want cube of number")
print("Enter 3 if you want square root of number")

choice = int(input("Enter your choice:"))

if(choice == 1):
    a.square()

elif(choice == 2):
    a.cube()

elif(choice == 3):
    a.square_root()
    
else:
    print("Invalid choice!Try again\nTo Restart the code press up arrow once and then press enter key once")
'''


#Class attribute v/s Instance attribute
'''
class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present 
print(Demo.a) # Prints the class attribute

#instance attribute does not altar the class attribute
'''


#Train ticket booking and status
'''
import random
class Train:
    def __init__(self , trainNo):
        self.trainNo = trainNo

    def book(self , depart_from , arrival_to):
        print(f"Your seat in train number {self.trainNo} from {depart_from} to {arrival_to} has been booked successfully")

    def get_status(self):
        print(f"The train number {self.trainNo} is running on time")

    def fare(self , depart_from , arrival_to):
        print(f"The ticket fare of train number {self.trainNo} from {depart_from} to {arrival_to} is Rs.{random.randint(200 , 2000)}")

t = Train(12305)

depart = input("Enter from where you want to book train:")
arrival = input("Enter till where you want to book train:")

print("Enter 1 to check your bookings")
print("Enter 2 to check status of the train")
print("Enter 3 to check fare of the train")

choice = int(input("Enter your choice:"))

if(choice == 1):
    t.book(depart , arrival)

elif(choice == 2):
    t.get_status()

elif(choice == 3):
    t.fare(depart , arrival)

else:
    print("Invalid choice! Try again")
'''


#single Inheritance
'''
class Employee:
    company = "ITC"
    name = "Kush"
    salary = 4800000
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "ITC Infotech"
    # name = "Kush"
    # salary = 4800000
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()  #we didnt even written show() function in programmer still we got it as we used inheritance we wrote employee in programmer so employee act as parent to programmer so all those function that are in employee will there be in programmer and also there will be its own function
'''


#Multiple inheritance
'''
class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()
'''


#Multilevel Inheritance
'''
class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)           # Prints the a attribute
#print(o.b)          # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)      # Prints the a , b attribute
#print(o.c)          # Shows an error as there is no b attribute in Employee class

o = Manager()
print(o.a, o.b, o.c) # Prints the a , b , c attribute
'''


#super().__init__() method
'''
class Employee:
    def __init__(self):
        print("Constructor of Employee")

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    
# o = Programmer()  #only print "Constructor of Programmer"

o = Manager()     #print both "Constructor of Programmer" & "Constructor of Manager" due to     super().__init__() method
'''


#Class method
'''
class Employee:
    a = 1
    
    def show(self):    #It show 2 but if i want 1 i will use class method
        print(f"The class attribute is {self.a}")

    @classmethod   #This @ thing is called decorator
    def show1(cls):  #Use cls rather than self in class method (self also work but cls is prefered)
        print(f"The class attribute is {cls.a}")

e = Employee()
e.a = 2

e.show()
e.show1()
'''


#Property decorator and @.setter 
'''
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}" #returns first and last names when called
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0] #breaks the name from there where is a space and forms a list where it contains the 0th element
        self.lname = value.split(" ")[1] #And it contains the 1st element 

e = Employee()
e.a = 45

e.name = "Kushagra Mittal"

print(f"First name: {e.fname}")
print(f"Last name: {e.lname}")

e.show()
'''


#Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary
'''
class Employee:
    salary = 234
    increment = 20 
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self, salary):
        self.increment =  ((salary/self.salary) -1)*100 

#new sal = old sal(1+inc/100) 
#inc = ((new sal/old sal) -1 )*100
#here new sal = salary
#old sal = self.salary

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)
'''


# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them
'''
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
        
    

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1*c2)
'''


# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them
'''
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5i + 7j + 9k)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8i + 1j + 12k)
print(v1 * v3)  # Output: 50
'''


# __len()__ method
'''
class Vector:
    def __init__(self, l): 
        self.l = l

    
    
    def __len__(self):
        return len(self.l)

# Test the implementation
v1 = Vector([1, 2, 3,4,5,5,6,7,77,8]) 
print(len(v1))
'''


# Number guessing game
'''
import random

print("Welcome to number guessing game")

print("Enter 1 if you want easy level(Guess between 1 - 100)")
print("Enter 2 if you want hard level(Guess between 1 - 1000)")

choice = int(input("Enter your choice:"))

if(choice == 1):
    print("Guess a number between 1 to 100")
    n = random.randint(1,100)
    a = -1
    guess = 1
    while(n != a):
        m = int(input("Enter your guess:"))

        if(m < n):
            print("Wrong guess!Try a bigger number")
            guess += 1

        elif(m > n):
            print("Wrong guess!Try a smaller number")
            guess += 1

        elif(m == n):
            print("Congratulations!You guessed the number correctly")
            print(f"You took {guess} attempts")
            break

elif(choice == 2):
    print("Guess a number between 1 to 1000")
    n = random.randint(1,1000)
    a = -1
    guess = 1
    while(n != a):
        m = int(input("Enter your guess:"))

        if(m < n):
            print("Wrong guess!Try a bigger number")
            guess += 1

        elif(m > n):
            print("Wrong guess!Try a smaller number")
            guess += 1

        elif(m == n):
            print("Congratulations!You guessed the number correctly")
            print(f"You took {guess} attempts")
            break

else:
    print("Invalid choice")
'''


#Walrus operator 
'''
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)
'''


#types
'''
from typing import List, Union, Tuple 

n : int = 5

name: str = "Harry"


def  sum(a: int, b: int) -> int:
    return a+b

print(sum(2,3))
'''


# match_case
'''
def http_status(status): 
    match status:  
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status"  

n = int(input("Enter the error number that you are getting:"))

print(http_status(n))
'''


# try except 
'''
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:  #It does not crashes the program but just give custom made error
    print("Heyyy, That's an error , Enter integer value only.")
    print(f"The error is: {v}")
    # print(v)
    
except Exception as e:   #Works when we comment out above except
    print(e) 

print("Thank You for using my code")
'''


# raising exception 
'''
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")  #this "raise" crashes the programme i.e. the program ends by giving our custom message
else:
    print(f"The division a/b is {round(a/b , 3)}")
'''


# try else 
'''
try:
    a = int(input("Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 


else:
    print("I am inside else") #only works when try work well without error or going in exception
'''


# try finally 
'''
def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally") #In these cases (not in a function) works always even if code works with error or works well


main()
'''

# module 
'''
from module import myfunc
#if I run this code i.e. right now its an imported module so the  print __name__ in the module will print the name of the module i.e. module 
'''


# global 
'''
a = 23 #Here it act as global variable for all values of a

def fun():
    print(a)

def func():
    global a #now we have declared a as global in this function so whatever value we give to in this function will act as global value  
    a = 2
    print(a)

def funct():
    print(a)

fun()  #right now 23 is the global value
print(a)  #right now 23 is the global value

func()  #now value of a changes to 3
print(a)  #now value of a changes to 3 as once function func is called now value changes to 3

funct()  #now value of a changes to 3 as once function func is called now value changes to 3 for ever until again global function is not used to change the value
'''


# enumerate
'''
l = ["Lays", "Dairy Milk", "Banana", "Whey Protein"]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")
'''


# List comprehension
'''
myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)
'''


# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same
'''
try:
    print("File 1")
    with open("1.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)
    print("\n") 


try:
    print("File 2")
    with open("2.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e) 
    print("\n")


try:
    print("File 3")
    with open("3.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)
    print("\n")


print("Thank you For using my code")
'''


# Write a program to print third, fifth and seventh element from a list using enumerate function
'''
l = [1,2,3,4,5,6,7,8,9]

for i , item in enumerate(l):
    if(i == 2 or i == 4 or i == 6):
        print(item)
'''


# Write a list comprehension to print a list which contains the multiplication table of a user entered number
'''
n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)
'''


# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’
'''
try:
    a = int(input("Enter number 1:"))
    b = int(input("Enter number 2:"))

    print(round(a/b , 3))
    
except ZeroDivisionError as e:
    print("Infinte")
'''
 

# Store the multiplication tables in a file named Tables_in_list.txt
'''
n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
with open("Table_in_list.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")
'''
