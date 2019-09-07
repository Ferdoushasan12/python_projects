 
def get_triangle_sides ():
    sides = []
    print("give the length of each side")
    while len(sides) !=3:
        sides_length = input (">")
        if sides_length.isdigit() == True and int(sides_length) >0 :
            sides.append(int(sides_length))
        else:
            print('not a proper value,try again')
    hyp = max (sides)
    c = hyp 
    sides.remove(c)
    a=sides[0]
    b=sides[1]

    triple = '(' + str(a) + str(b) + str(c) + ')'



    if a**2 + b**2 == c**2 :
        print ( triple + ' form a pythagoriean triangle')
    else :
        print ( triple + ' do not form a pythagorian triangle ')




def try_again () :
    print('type q to quit or hit enter to try again')
    us = 0
    while us == 0 :
        prefer = input()
        if prefer == 'q':
            us = -1 
        elif prefer == '' :
            get_triangle_sides()
        else :
            print ('wrong answer')
    return us 


def main () :
    print( 'welcome')
    now = 0
    while now == 0 :
        get_triangle_sides()
        now = try_again ()
main ()




