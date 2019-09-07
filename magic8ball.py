# Magic 8 ball game
# The basic coding of this game began with Al Sweigart's "Automate the Boring Stuff" in chapter 4. 
# I then worked his list into a function and added a function that can re-play or quit.

import random, time

messages = ['Sucks to be you.',
            'The inevitable disaster will occur.',
            'You again? Get a life.',
            'I do not know. I do not care.',
            'No. The answer will always be no.',
            'The ball is hazy. Your question is too stupid.',
            'Ask again when I am drunk and I want to care.',
            'Yes but with consequences',
            'Fine. Do it.',
            'That will not happen.',
            'Can you ask that again but in Pig Latin?',
            'I have a vision! It will happen!',
            'The future is bright.',
            'The future is grim.',
            'Turn 3 times, touch your toes, and all will come true.',
            'Like the sands thru the hour glass, these too are the days of our lives.',
            'Hope springs eternal.',
            'No.',
            'Maybe.',
            'Do that voodoo you do!',
            'Che sera sera.']

def playgame():
    inp = input('Oh ask your question to the mighty 8 ball! ')
    print("You asked: '" + str(inp) + "'")
    time.sleep(1)
    print("Let me see...")
    time.sleep(1.25)
    print('...Thinking...')
    time.sleep(1.5)
    print('...still thinking...')
    time.sleep(2)
    print('...I really should clean this magic 8 ball...')
    time.sleep(1.5)
    print('...Is that pizza sauce? When did I last eat pizza?')
    time.sleep(2)
    print(messages[random.randint(0, len(messages) - 1)])
    playagain()

def playagain():
    quest = input('Would you like to ask another question? ')
    if quest == 'yes':
        print('')
        playgame()
    elif quest != 'yes':
        print('')
        print('')
        print('There is a sap born every second. Have a mediocre day.')
        quit()

playgame()
