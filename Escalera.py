'''
Created on 24 abr. 2017

@author: neogeo39
'''
number_list = []
number_list.extend([])

print "----Number Range----"

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if number1 == number2 or number2 == number3:
    print "That's not a valid number"

else:
    
    if number1 > number2:
        for i in reversed (range(number2, number1 + 1)):
            number_list.extend([i])
    
    else :
        for i in range(number1 + 1, number2 + 1):
            number_list.extend([i - 1])
            
    if number2 > number3:
        for b in reversed(range(number3, number2 + 1)):
            number_list.extend([i + 1])
    
    
    else :
        for b in range (number2 + 1, number3 + 1):
            number_list.extend([b])
            
    print number_list
