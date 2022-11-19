#first we need to import datetime module...
import datetime
#now create a func which takes 3 parameters
def Agecalculator(y,m,d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = float((today-dob).days/365.25)
    print(age)
    month = float(input("enter value after point to count month: "))
    m1 =int(month*12)
    m2 = str(m1)
    y1 = int(age)
    y2 = str(y1)
    print("your age is  " + y2 + " year"  + " and " + m2 + "months..")
    #this is a + point we can take date input from user like this ....
d = int(input("enter date of birth :"))
m = int(input("enter month of birth :"))
y = int(input("enter year of birth :"))
Agecalculator(y,m,d)
# so over code is ready to use just run the program and have some fun...
