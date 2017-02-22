## Hyungchol Jun
# 2014-03-25
# 0325 - p7.13
'''
write a program that asks the user to input a set of floating-point values.
When the user enters a value that is not a number, give the user second chance to enter the value
After two chances, quit reading input. Add all correctly specified values and print the sum when the user is done \
entering data.
Use specification handling to detect improper inputs.
'''
def func0325():
    done = False
    chance = 0
    sum = 0
    while not done:
        try:
            a = float(input("Input Values: "))
            sum = sum + a
            chance = 0
        except ValueError:
            chance += 1
            if chance == 1:
                print("You have put wrong value one time. I will give you one more chance.\n")
            if chance == 2:
                print("Okay. That is enough. I will give you sum and end the program.")
                print("The total is %f" % sum)
                break