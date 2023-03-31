# Excercise 2 - BMI 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2
round_bmi = round(bmi)

if bmi < 18.5:
    print(f'Your BMI is {round_bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {round_bmi}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {round_bmi}, you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {round_bmi}, you are obese.')
else:
    print(f'Your BMI is {round_bmi}, you are clinically obese.')