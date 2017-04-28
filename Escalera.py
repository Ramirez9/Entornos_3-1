'''
Created on 24 abr. 2017

@author: neogeo39
'''
numero_lista = []
numero_lista.extend([])

print "----Number Range----"

numero = int(input("Enter first number: "))
numero2 = int(input("Enter second number: "))
numero3 = int(input("Enter third number: "))
if numero == numero2 or numero2 == numero3:
    print "That's not a valid number"

else:
    
    if numero > numero2:
        for i in reversed (range(numero2, numero + 1)):
            numero_lista.extend([i])
    
    else :
        for i in range(numero + 1, numero2 + 1):
            numero_lista.extend([i - 1])
            
    if numero2 > numero3:
        for b in reversed(range(numero3, numero2 + 1)):
            numero_lista.extend([i + 1])
    
    
    else :
        for b in range (numero2 + 1, numero3 + 1):
            numero_lista.extend([b])
            
    print numero_lista
