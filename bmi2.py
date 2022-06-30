from os import sys
from turtle import clear
import emoji
def main():
    print ("************************************************")
    print ("Hi! This program will guide to your healthy lifestyle\n")
    print ("Please fill in the details below")
    name=input ("Name:")
    age= int (input ("Age:"))
    gender = ""
    while(gender != "male") and (gender != "female"):
        gender= input ("Gender(male/female in small letter):")

    if gender== "male":
        weight= float(input ("Weight (in kg):"))
        height= float(input ("Height (in m):")) 
        bmi= weight/height**2
        print()
        print ("This is your BMI:",round(bmi,2))

        if bmi >= 30:
            print ("You are OBESITY!")
            print("\U0001F612\U0001F612\U0001F612\U0001F612\U0001F612\U0001F612\U0001F612\U0001F612\n")
            print ("You must have a good diet\nHere are some tips for you")
            print ("1.Improving your eating habits.\
            \n2.Increasing physical activity.\
            \n3.Eat five to six servings of fruits and vegetables daily\n")
          
        elif bmi >= 25:
            print ("You are OVERWEIGHT!")
            print("\U0001F611\U0001F611\U0001F611\U0001F611\U0001F611\U0001F611\U0001F611\U0001F611")
            print ("You must have a good diet\nHere are some tips for you")
            print ("1.Eat more fruit, vegetables, nuts, and whole grains.\
            \n2.Exercise, even moderately, for at least 30 minutes a day\n")
            
        elif bmi >= 18.5:
            print("You are HEALHTY!")
            print("\U0001F601\U0001F601\U0001F601\U0001F601\U0001F601\U0001F601\U0001F601\U0001F601\n")
            print ("Congratulation! Keep it up and stay healthy!")
        else:
            print ("You are UNDERWEIGHT!")
            print("\U0001F605\U0001F605\U0001F605\U0001F605\U0001F605\U0001F605\U0001F605\U0001F605\n")
            print ("You must have a good diet\nHere are some tips for you")
            print ("1.Eat more frequently. When you're underweight, you may feel full faster\
            \n2.Choose nutrient-rich foods\
            \n3.Try smoothies and shakes\
            \n4.Make every bite count\
            \n5.Have an occasional treat\n")
            

    elif gender== "female":
        weight= float(input ("Weight (in kg):"))
        height= float(input ("Height (in m):"))
        bmi= weight/height**2
        print("This is your BMI:",round(bmi,2))
        if bmi >= 30:
            print ("You are OBESITY!")
            print("\U0001F612\U0001F612\U0001F612\U0001F612\U0001F612\U0001F612\U0001F612\U0001F612\n")
            print ("You must have a good diet\nHere are some tips for you")
            print ("1.Improving your eating habits.\
            \n2.Increasing physical activity.\
            \n3.Eat five to six servings of fruits and vegetables daily.\n")
            
        elif bmi >= 25:
            print ("You are OVERWEIGHT")
            print("\U0001F611\U0001F611\U0001F611\U0001F611\U0001F611\U0001F611\U0001F611\U0001F611")
            print ("You must have a good diet\nHere are some tips for you")
            print ("1.Eat more fruit, vegetables, nuts, and whole grains.\
           \n2.Exercise, even moderately, for at least 30 minutes a day.\n")
            
        elif bmi >= 18.5:
            print("You are HEALHTY!")
            print("\U0001F601\U0001F601\U0001F601\U0001F601\U0001F601\U0001F601\U0001F601\U0001F601\n")
            print ("Congratulation! Keep it up and stay healthy!\n")
        else:
            print ("You are UNDERWEIGHT!\n")
            print("\U0001F605\U0001F605\U0001F605\U0001F605\U0001F605\U0001F605\U0001F605\U0001F605\n")
            print ("You must have a good diet\nHere are some tips for you")
            print ("1.Eat more frequently. When you're underweight, you may feel full faster\
            \n2.Choose nutrient-rich foods\
            \n3.Try smoothies and shakes\
            \n4.Make every bite count\
            \n5.Have an occasional treat\n")

    else:
        print ("Sorry, please key in the gender again.")

    print('''Press ENTER to check again Press "q" to quit :''')
    choice = input()
    print()
    if choice == 'q':
        sys.exit(0)
    else:

        main()

main()
