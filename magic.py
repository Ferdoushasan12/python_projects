import time, random 



KO = [     'You have an intense desire to get people to accept and like you.',
    'Sometimes you give too much effort on projects that don’t work out.',
    'You prefer change and do not like to feel limited in what you can do.',
    'You are an independent thinker who takes pride in doing things differently than others.',
    'Sometimes you can be loud, outgoing, and a people person, but other times you can be quiet, shy, and reserved.',
    'You can be overly harsh on yourself and very critical.',
    'Although you do have some weaknesses, you try very hard to overcome them and be a better person.']
def main ():
     easy = " ask a question"
     print (easy)
     question = input ('>>')
     print ('you have asked')
     time.sleep (1)
     print ('plz wait ')
     time.sleep (1.25)
     print ( 'loading')
     time.sleep (1.50)
     print ('just a bit ')
     time.sleep (2) 
     print(KO [random.randint (0, len(KO) - 1)] )
     mundane ()

def mundane ():
    rogue = input ('want to ask a another question. type yes or no ')
    print (rogue)
    if rogue == 'yes':
        main ()
    elif rogue == 'no':
        print ('have a nice day ')
        quit ()
    elif rogue == '' :
        print (' dont act smart you dickhead')
        main ()

main ()
# you can add mundane function in mundane 
