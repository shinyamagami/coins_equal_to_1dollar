# Shinichiro Yamagami
# Oct 8th, 2015
# This program check if the total value of the coins inputted by users equal to
# one dollar or not.

#input: get the number of each coins
pennies = float(input('Enter the number of pennies you have:  '))
nickels = float(input('Enter the number of nickels you have:  '))
dimes = float(input('Enter the number of dimes you have:    '))
quarters = float(input('Enter the number of quarters you have: '))

#calculation: get the sum of coins
total_value = pennies + nickels * 5 + dimes * 10 + quarters * 25
convert_to_cents = total_value / 100

#output: express the result
if convert_to_cents > 1.00:
    print('The total value you inputted is more than $1.00')
elif convert_to_cents < 1.00:
    print('The total value you inputted is less than $1.00')
else:
    print('Congratulations! You won!')

print('The total value you inputted is $', format(convert_to_cents, '.2f'))
