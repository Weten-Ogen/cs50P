x, y = input("Enter a fractions : ").split('/')
x , y = int(x), int(y)


try:
    per = int(x/y * 100)
    if per <= 1:
        print('E')
    elif per >= 99:
        print('F')
    else:
        print(f"{per}%")
except ValueError:
    print("Enter a correct Formats")
except ZeroDivisionError:
    print("You fraction can't have zero as the denominator")
 
