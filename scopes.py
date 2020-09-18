###
globalvariable  = 100

def addMoney():
    globalvariable = 10
    tmpVariable = globalvariable + 100
    return tmpVariable

def addMoneyByRef(tmpvariable):
    tmpVariable = tmpvariable + 100
    return tmpVariable

def addMoneyByglobal():
    global globalvariable
    globalvariable = globalvariable + 100
    return globalvariable


#print( globalvariable,  addMoney(), globalvariable) #100 110 100

#print( globalvariable,  addMoneyByRef(globalvariable), globalvariable) #100 200 100
#print( globalvariable,  addMoneyByglobal(), globalvariable) #100 200 200










globalvariable = 100              #global
def addmoney():
    globalvariable = 10           #local
    tempvariable = globalvariable + 100
    return tempvariable

#print( globalvariable , addmoney() )


def addmoneybyref(tempvariable):
    tempvariable = tempvariable + 100
    return tempvariable

#print( globalvariable , addmoneybyref(globalvariable) , addmoneybyref(500) )




def addmoneybyglobal():
    global globalvariable
    globalvariable = globalvariable + 1000
    return globalvariable

print( globalvariable, addmoneybyglobal() )









