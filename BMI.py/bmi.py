# Just a normal BMI calculator using basic python.



# Enter your hight in cm and not in feet/inches.
height = float(input("Enter your height in centimeters: "))

# Enter your weight in Kg
weight = float(input("Enter your weight in Kg: "))

height = height / 100

# Formula of BMI is weight /
bmi = weight / (height * height)

print(f"Your Body-Mass index is: {bmi:.2f}")

if bmi > 0:
    if bmi <= 16:
        print("You are severely under-weight.")
    elif bmi <= 18.5:
        print("You are under-weight.")
    elif bmi <= 25:
        print("You are Healthy.")
    elif bmi <= 30:
        print("You are overweight.")
    else:
        print("You are severely overweight.")
else:
    print("Please Enter a valid details.")
