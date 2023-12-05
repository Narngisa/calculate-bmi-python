import os
import json

# Read JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

below_data = data['below']
normal_data = data['normal']
over_data = data['over']
obese_data = data['obese']
severely_data = data['severely']

# Input float value for weights and height
weight = float(input("Weight: "))
height = float(input("Height: "))

def calculate(weight, height) -> float:

    bmi = weight / (height / 100) ** 2

    # Clear Terminal
    os.system("cls")
    # Output Title
    print("BMI: ", bmi)

    if bmi < 18.5:
        category_data = below_data
    elif 18.5 <= bmi <= 24.9:
        category_data = normal_data
    elif 25.0 <= bmi <= 29.9:
        category_data = over_data
    elif 30.0 <= bmi <= 34.9:
        category_data = obese_data
    else:
        category_data = severely_data

    # Output BMI category information
    print(f"BMI Category: {category_data['BMI']}")
    print(f"Interpretation: {category_data['IPT']}")
    print(f"Risk of complications: {category_data['ROC']}")

# Call the calculate function with the provided weight and height
calculate(weight, height)