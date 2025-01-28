def bmi_cal(weight, height):
    return weight/(height**2)

def bmi_category(bmi):
    if bmi<18.5:
        return"Underweight"
    elif 18.5<=bmi<25:
        return"Normal"
    elif 25<=bmi<30:
        return"Overweight"
    else:
        return"Obese"

def main():
    weight = float(input("Please enter weight in kilograms: "))
    height = float(input("Please enter height in meters: "))

    bmi = bmi_cal(weight, height)
    category = bmi_category(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    main()