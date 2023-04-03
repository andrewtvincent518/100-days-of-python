# Day 2 Project: Tip Calculator

print('Welcome to the tip calculator!')
total_bill = input('What was the total bill?')
desired_tip = input('How much would you like to give? 10, 12, or 15?')
num_of_people = input('How many people to split the bill?')

ten_percent = (int(total_bill) / int(num_of_people)) * 1.1
ten_percent_rounded = round(ten_percent, 2)

twelve_percent = (int(total_bill) / int(num_of_people)) * 1.12
twelve_percent_rounded = round(twelve_percent, 2)

fifteen_percent = (int(total_bill) / int(num_of_people)) * 1.15
fifteen_percent_rounded = round(fifteen_percent, 2)

if desired_tip == '10':
    print(f'Each person should pay: {ten_percent_rounded}')
elif desired_tip == '12':
    print(f'Each person should pay: {twelve_percent_rounded}')
elif desired_tip == '15':
    print(f'Each person should pay: {fifteen_percent_rounded}')