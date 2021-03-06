#!C:/Python27.python.exe
'''
Programmer: Jessica Joseph
Description: This program is designed to present a customer with an itemized bill

'''

from __future__ import print_function
import os

'''<-----------Defining my Global Constants----------->'''

TAX_RATE = 0.0846;    COFFEE_COST = .77;    DOUGHNUT_COST = .64;   NUMBER_OF_SLASHES = 22

'''<---------------Defining my Functions--------------->'''

'''<-Creating the Banner Design-->'''

def forwardSlashDesign():
    '''Creates a row of  /\ '''
    forwardSlashDesign = '/\\'
    print( forwardSlashDesign*NUMBER_OF_SLASHES)

def printNameDesign():
    ''' Prints the name that will be used in a design'''
    print('THE COFFEE AND DOUGHNUT SHOPPE')

def backwardSlashDesign():
    '''Creates a row of \/ '''
    backwardSlashDesign = '\/'
    print( backwardSlashDesign*NUMBER_OF_SLASHES)

def mainBillDesign(x,y):
    '''Creates the design for the main bill'''
    cupsOfCoffee, numbOfDoughnuts, costOfCoffee, costOfDoughnuts, taxTotal, amountOwed = showBill(x,y)
    print('\t_%i_ cups of coffee : $_%.2f_'  % (cupsOfCoffee, costOfCoffee ))
    print('\t        _%i_ doughnuts : $_%.2f_'  % (numbOfDoughnuts, costOfDoughnuts))
    print('\t\t      tax : $_%.2f_' %(taxTotal))
    print('\n\t\t Amount Owed : $__%.2f__' % (amountOwed))
    print('\nThank you for buying local.')
    

'''<----------Creating the Bill---------->'''
def getInputs():
    '''Retrieves input from the user or caller'''
    cupsOfCoffee = int(raw_input('How many cups of coffee will you have?'))
    numbOfDoughnuts = int(raw_input('How many doughnuts will you have?'))
    return cupsOfCoffee, numbOfDoughnuts

def showBill(cupsOfCoffee=0, numbOfDoughnuts=0):
          '''Will calculate the Bill. Takes two parameters'''
          costOfCoffee = cupsOfCoffee*COFFEE_COST
          costOfDoughnuts = numbOfDoughnuts*DOUGHNUT_COST
          taxTotal = (costOfCoffee + costOfDoughnuts)*TAX_RATE
          amountOwed = costOfCoffee + costOfDoughnuts+taxTotal

          return cupsOfCoffee, numbOfDoughnuts, costOfCoffee, costOfDoughnuts, taxTotal, amountOwed


'''<---Organizing and Calling my Functions----->'''
def main():
    cupsOfCoffee, numbOfDoughnuts = getInputs()
    forwardSlashDesign()
    printNameDesign()
    backwardSlashDesign()
    mainBillDesign(cupsOfCoffee, numbOfDoughnuts)
          
main()



