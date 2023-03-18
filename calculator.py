# -*- coding: utf-8 -*-


class Calc(object):
    "calculator"
    # init method
    def __init__(self, a, b):
        "initialize values"
        #attribute
        self.value1 = a
        self.value2 = b
    
    def add(self):
        "addition a + b = result -> return result"
        return self.value1 + self.value2
    
    def sub(self):
        "substraction a - b = result -> return result "
        return self.value1 - self.value2

    def multiply(self):
        "multiplication a * b = result -> return result"
        return self.value1 * self.value2
    
    def div(self):
        "division a / b = result -> return result"
        return self.value1 / self.value2
     
selection = input("choose :\n1: addition \n2: substraction\n3: multiplication\n4: division\n")  
if selection != "1" or "2" or "3" or "4" :
    print("ERROR : there is no defined selection")

v1 = int(input("value1 : "))
v2 = int(input("value2 : "))

c1 = Calc(v1,v2)
add_result = c1.add()
sub_result = c1.sub()
mul_result = c1.multiply()
div_result = c1.div()

if selection == "1" :
    print("Addition {}".format(add_result))
elif selection == "2" :
    print("Substraction {}".format(sub_result))
elif selection == "3" :
    print("Multiply {}".format(mul_result))
elif selection == "4" :
    print("Division {}".format(div_result))
 
    
    


