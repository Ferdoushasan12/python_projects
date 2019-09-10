fv = float(input('write the numbers/n>>'))
i = float(input('write the interest rate/n>>'))
m = i/100
year = float(input('write the number of years/n>>'))
h = float(input('write the year of compounding'))
l = year*h 
pv =(fv/(1+m/h)**l)
print (round(pv,2))


