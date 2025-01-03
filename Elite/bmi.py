def calculate_bmi(weight, height):
    """
    Calculate BMI given weight in kilograms and height in meters.
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight / (height ** 2)

def bmi_category(bmi):
    """
    Determine the BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        print(f"Your BMI is {bmi:.2f}. You are in the '{category}' category.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()