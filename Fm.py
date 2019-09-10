import time 

print('welcome to the FV calculator')

def funv():
    print('what do want to calculate? Future value or present')
    n = input('write fv or pv')
    if n == 'pv':
        ha() 
    elif n == 'fv' :
        ba() 
    else:
        print('wrong command')
def ba ();

    pv = float(input('write the present value'))
    i = float(input('write the interest rate/n>>'))
    m = i/100
    year = float(input('write the number of years/n>>'))
    h = float(input('write the year of compounding'))
    l = year*h 
    fv =(pv*(1+m/h)**l)
    print (round(pv,2))
def ha ():
    fv = float(input('write the future value'))
    i = float(input('write the interest rate/n>>'))
    m = i/100
    year = float(input('write the number of years/n>>'))
    h = float(input('write the year of compounding'))
    l = year*h 
    pv =(fv/(1+m/h)**l)
    print (round(pv,2))
