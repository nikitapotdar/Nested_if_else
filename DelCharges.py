#program to display delivery charges
#problem statement below
'''An agency provides parcel services to two countries A and B
   and charges are according to the weight of the parcel.
   For Country A – charges are for weight <= 10 then $5,
                   weight > 10 and <= 30 then $ 10 and
                   weight above 30 then $20.
   For country B – charges are for weight <= 10 then $7,
                   weight > 10 and <= 30 then $12
                   and weight above 30 then $22.
   Take input from the user – country to deliver the parcel
   and weight of the parcel and print the cost of delivery in the output.'''

import sys
country = input('input country - A or B : ').upper() or ' '
weight = int(input('input parcel weight in Kgs : ') or 0)
if country in ['A', 'B'] and weight > 0:
      if country == 'A':
            if weight <= 10:
                  charge = '$5'
            elif weight <= 30:
                  charge = '$10'
            else:
                  charge = '$20'

      if country == 'B':
            if weight <= 10:
                  charge = '$7'
            elif weight <= 30:
                  charge = '$12'
            else:
                  charge = '$22'
else:
           print('country A or B & weight above zero only allowed')
           sys.exit()
print(f'charges for delivery in {country} are {charge}')
