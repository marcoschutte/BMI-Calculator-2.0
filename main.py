height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / pow(height, 2)
bmi_rounded = round(bmi)

if(bmi_rounded < 18.5):
    print("Your BMI is " + str(bmi_rounded) + ", you are underweight.")
elif(bmi_rounded < 25):
    print("Your BMI is " + str(bmi_rounded) + ", you have a normal weight.")
elif(bmi_rounded < 30):
    print("Your BMI is " + str(bmi_rounded) + ", you are slightly overweight.")
elif(bmi_rounded < 35):
    print("Your BMI is " + str(bmi_rounded) + ", you are obese.")
elif(bmi_rounded > 35):
    print("Your BMI is " + str(bmi_rounded) + ", you are clinically obese.")