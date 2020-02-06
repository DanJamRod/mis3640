def bmi_calc(w,h):
    """
    BMI calculator when inputting weight(kg), and height(m^2)
    """
    bmi = w*h**-2
    print(f"Your BMI is {bmi:.2f}")
    if bmi<18.5:
        print(f"As your BMI is under 18.5 you are in the underweight category")
    elif bmi<25:
        print(f"As your BMI is between 18.5 and 25 you are in the underweight category")
    elif bmi<30:
        print(f"As your BMI is between 25 and 30 you are in the overweight category")
    else:
        print(f"As your BMI is over 30 you are in the obese category")

bmi_calc(90, 1.85)