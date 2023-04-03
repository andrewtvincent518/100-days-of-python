# Exercise 3 - Life in Weeks

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days = int(age) * 365
weeks = int(age) * 52
months = int(age) * 12

final_days = 90 * 365
final_weeks = 90 * 52
final_months = 90 * 12

days_until_90 = final_days - days
weeks_until_90 = final_weeks - weeks
months_until_90 = final_months - months

print(f'You have {days_until_90} days, {weeks_until_90} weeks, and {months_until_90} months left')