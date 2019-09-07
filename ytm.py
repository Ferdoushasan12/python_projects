def main():

    Fv = float(input('Enter the face value'))
    mv = float(input('market value of shares'))
    cr = float(input('coupon rate'))/100
    year = float(input('number of years'))
    c =cr*Fv
   
    if mv < Fv:
        fic_r=cr
        trial = mv +1
        b_zero = []
        rates = []
        while trial > mv: 
            fic_r = fic_r+.01
            v = (c/fic_r* (1-(1/(1+fic_r)**year)))+( Fv/(1+fic_r)**year)
            trial = v 
            b_zero.append(trial)
            rates.append(fic_r)
        hr = rates [len(rates)-1]
        lr = rates [len(rates) -2]
        lv = b_zero[len(b_zero)-1]
        hv = b_zero [len(b_zero)-2]
        ytm = lr+(hv - mv)/(hv - lv) * (hr-lr)
        ytm =round(ytm * 100,2)
        print ('the ytm value is ' + str(ytm) + '%')
        null()
    else:
        fic_r=cr
        trial = mv -1
        b_zero = []
        rates = []
        while trial < mv: 
            fic_r = fic_r-.01
            v = (c/fic_r* (1-(1/(1+fic_r)**year)))+( Fv/(1+fic_r)**year)
            trial = v 
            b_zero.append(trial)
            rates.append(fic_r)
        lr = rates [len(rates)-1]
        hr = rates [len(rates) -2]
        hv = b_zero[len(b_zero)-1]
        lv = b_zero [len(b_zero)-2]
        ytm = lr+(hv - mv)/(hv - lv) * (hr-lr)
        ytm =round(ytm * 100,2)
        print ('the ytm value is ' + str(ytm) + '%')
        null()




def null () :
    ask = input('do you want to try again? type yes or no ')
    if ask == 'yes' :
        main() 
    else :
        quit() 
def void () :
    print('Welcome to the ytm calculator')
    main()
void()

    
