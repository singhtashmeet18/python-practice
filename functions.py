#import time
#ticks = time.time()        #time in seconds since 1 jan,1970
#print (ticks)
#print ("number of ticks since 12:00am,january 1, 1970:", ticks)
import time;
#localtime = time.localtime(time.time())
#print = ("local current time:", localtime)

#import calendar
#cal = calendar.month(2020,6)
#print (cal)


########

#def changeme( mylist ):
    #mylist.append([1,2,3,4])
    #print("values inside the function:", mylist )
    #return

#mylist= [10,20,30]
#changeme( mylist )
#print("values outside thr function:", mylist)


#######
#def printinfo(name,age):
    #print("name",name)
    #print("age",age)
    #return


#printinfo(name ='tashmeet',age = 22)


#######

#def absolute_value(num):
    #if num >= 0:
        #return num
    #else:
        #return num

#print(absolute_value(5))
#print(absolute_value(-10))








########
#def greet(name, msg):

    #print("Hello", name + ', ' + msg)

#greet("Monica", "Good morning!")





########
#def greet(name,msg = "good morning"):
    #print("heloo",name + ','+ msg)


#greet("tashmeet")
#greet("sam","how are you")

########
#def changeme(mylist):
    #Wmylist = [1,2,3,4]
    #print("values inside the function:" , mylist)
    #return

#mylist = [10,20,30]
#changeme(mylist)
#print("values outside the function:" , mylist)

##########
#def printme(str):
    #print("this str will print string in the function" ,str)
    #return

#printme(str)
#########


#def sum(arg1,arg2):
    #total = arg1 + arg2
    #print("inside the function:" , total)
    #return total

#total = sum(10,20)
#print("outside the function:", total)
############

#def printinfo(name,age = 18):
    #print("name:" , name)
    #print("age:" , age)

    #return

#printinfo(name = "tashmeet", age = 32)
#printinfo(name = "virat")

#################


def greet(*names):
    for name in names:
        print("heloo:" , name)



greet("monika","priyanka","john","steve smith")

