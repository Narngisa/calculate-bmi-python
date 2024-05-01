# Calculate BMI in Python

The script calculates BMI using the formula: body weight in kilograms divided by the square of height in meters or centimeters divided by 100. It then determines the body mass index (BMI) using the formula Body Weight [kg] / Height [m] squared, and provides information about BMI and associated complications for each value.

![image](https://github.com/Narngisa/calculate-bmi-python/assets/100367855/748dc125-f6ce-49e2-ac7e-a84706377aaf)

> [!IMPORTANT]
> Install *[Python](https://www.python.org/) 3.9 or higher*

- **Calculate BMI**
```py
bmi = weight / (height / 100) ** 2
```

- **Read JSON file**
```py
with open('data.json', 'r') as file:
    data = json.load(file)
```

- **Condition BMI**
```py
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
```

- **Output BMI category information**
```py
print(f"BMI Category: {category_data['BMI']}")
print(f"Interpretation: {category_data['IPT']}")
print(f"Risk of complications: {category_data['ROC']}")

```
