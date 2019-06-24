#This project is to develope a program to calculate meal tips.
#06/23/2019
#CTI-110-P2HW2
#Chris Denno
#Enter meal cost.
#Calculate tip based on percentages.
#Calculate total price.
#Display tip and total price.
cost=float(input('Enter meal cost.'))
Tip1=float(format(cost*0.15, '.2f'))
Tip2=float(format(cost*0.18, '.2f'))
Tip3=float(format(cost*0.20, '.2f'))
Cost1=float(Tip1+cost)
Cost2=float(Tip2+cost)
Cost3=float(Tip3+cost)
print('15% Tip $', Tip1,'Total Cost $', Cost1)
print('18% Tip $', Tip2,'Total Cost $', Cost2)
print('20% Tip $', Tip3,'Total Cost $', Cost3)


