def calculate_bmi(height, weight): 
 print("Height = " + str(height)) 
 print("Weight = " + str(weight)) 
 BMI=weight / (height * height)
 print("BMI = " + str(BMI))
 if BMI < 18.5: 
   print("Underweight")
   return -1
 elif BMI >= 18.5 and BMI <= 25:
    print("Normal weight")
    return 0
 elif BMI > 25:
    print("Overweight")
    return 1
