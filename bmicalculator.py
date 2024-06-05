def get_float_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            elif min_value is not None and value < min_value:
                print(f"Please enter a value greater than or equal to {min_value}.")
            elif max_value is not None and value > max_value:
                print(f"Please enter a value less than or equal to {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


print("Welcome to the BMI Calculator!")

weight = get_float_input("Please enter your weight in kilograms: ")
height = get_float_input("Please enter your height in meters (e.g., 1.75): ", min_value=0.5, max_value=2.5)

bmi = calculate_bmi(weight, height)
category = categorize_bmi(bmi)
print(f"\nYour BMI is: {bmi:.2f}")
print(f"This is considered: {category}")

