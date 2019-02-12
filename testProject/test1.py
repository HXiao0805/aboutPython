# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:08:21 2019

@author: Administrator
"""
def account_longin():
    password=input('put password:')
    if password=='12345':
        print('log success!')
    else:
        account_longin()

account_longin()

for every_letter in 'hello world!':
    print(every_letter)
    
for num in range(1,11):
    print (str(num)+'+1='+str(num+1))

for i in range(1,10):
    for j in range(1,10):
        print('{}x{}={}'.format(i,j,i*j))

print(type(range(1,4)))

#for a,b in zip(num,str):
#    print(b,"is",a)
    
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self): 
        for element in self.formula: 
            print('Coke has {}!'.format(element))    
    def drink(self): 
        print('Energy!') 
coke = CocaCola()