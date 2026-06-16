def calculate_bmi(weight, height):
    bmi = weight / (height**2)

    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Healthy"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


print(calculate_bmi(50, 1.75))  # Underweight
print(calculate_bmi(70, 1.75))  # Healthy
print(calculate_bmi(90, 1.75))  # Overweight
