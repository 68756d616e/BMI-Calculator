# BMI Calculator basic
# How it works! You input your Height and Weight and you will receive a BMI result.
# The process : Weight / Height & then height squared by itself
# Example 70kg divided by 183m squared

Weight = input("Please type your weight in kg: ")
Height = input("Please type your hieght in m: ")

BMI = (int(Weight) / float(Height) ** 2)
BMI_INT = (int(BMI))

print(BMI_INT)

#Alternative BMI = Weight / float(Height) * float(Height)
#Alternative print(int(BMI)




