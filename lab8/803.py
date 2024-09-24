import math
def simple_interest(prin, rate, time):
    x = (prin*(rate/100)*time)+prin
    return x
def compound_interest(prin, rate, time):
    summ = prin*math.pow(1+(rate/100),time)
    return summ

p = float(input('Enter principle: '))
r = float(input('Enter interest rate: '))
t = float(input('Enter time: '))
print('Return money for simple interest calculation is {:.2f} Baht.'.format(simple_interest(p, r, t)))
print('Return money for compound interest calculation is {:.2f} Baht.'.format(compound_interest(p, r, t)))