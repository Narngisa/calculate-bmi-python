import os

weight = int(input("Weight: "))
height = int(input("Height: "))

bmi = weight / (height / 100) ** 2

os.system("cls")

print("BMI:", bmi)

if bmi < 18.5:
    print("""     
BMI: Below normal
Interpretation: Less than 18.5
Risk of complications: Risk of malnutrition
""")
elif bmi >= 18.5 and bmi <= 22.9:
    print("""
BMI: Normal
Interpretation: 18.5-22.9
Risk of complications: Lowest risk of complications
""")
elif bmi >= 23.0 and bmi <= 24.9:
    print("""
BMI: Overweight
Interpretation: 23.0-24.9
Risk of complications: Early stage of overweight, starting to have minor complications
""")
elif bmi >= 25.0 and bmi <= 29.9:
    print("""
BMI: Obese
Interpretation: 25.0-29.9
Risk of complications: Obese, complications in the early stage
""")
elif bmi > 30.0:
    print("""
BMI: Severely obese
Interpretation: More than 30.0
Risk of complications: Obese, increased risk of complications due to obesity
""")