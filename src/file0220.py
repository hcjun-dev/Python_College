    # Hyungchol Jun
    # 2014-02-20 P5.1b

    # defining average function
def func0220():
    def average(x, y, z):
        averageV = float((x+y+z)/3)
        print("Your average would be %.3f"% averageV)

    # getting 3 inputs from user
    x = int(input("Input first value "))
    y = int(input("Input second value "))
    z = int(input("Input third value "))
    average(x, y, z)
