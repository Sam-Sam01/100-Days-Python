print("This is a BMI calcultator")
height = float(input("Enter the height in M: "))
weight = float(input("Enter the weight in kg: "))
bmi = weight/(height*height)
if bmi <= 18.5:
    print(f"Your BMI score is {bmi}")
    print("Underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI score is {bmi}")
    print("Normal")
elif bmi >= 25 and bmi <= 30:
    print(f"Your BMI score is {bmi}")
    print("Overweight.")
elif bmi >= 30 and bmi <= 35:
    print(f"Your BMI score is {bmi}")
    print("oBESE")
else:
    print(f"Your BMI score is {bmi}")
    print("Clinically Obese.")