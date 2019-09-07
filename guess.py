import random, time  
print ('WELCOME')
time.sleep (1.25)
hashi = int (input('enter the lower range'))
beshi = int (input('enter the upper range'))
nice = random.randint ( int(hashi),int(beshi) )
def amar ():
    nice = random.randint ( int(hashi),int(beshi) )
    goru()

def goru () :
    take =int( input ( 'guess a  number '))
    if take == nice :
        print ( 'congrats')
        ball()
    elif int (take) > int (nice):
        print ('try decreasing the number')
        goru ()
    elif int (take) < int (nice):
        print('try increasing the number')
        print()
        goru()
def ball ():
    time.sleep (.75)
    print ('do you want to try again')
    value = input()
    if value == 'yes':
        amar()
    else :
        print('thank you for playing')
        quit () 
amar()
