marks = 80
attendance = 90
print(marks > 75 and attendance > 80)
print(marks > 75 or attendance > 80)
print(not marks > 75)

#if statements

num=int(input("Enter a number:"))
if num%2==0:
    print("The number is even")
else:
    print("Odd Number")

#if elif statements
day=int(input("Enter a day between 1-7:"))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid day")

#match statement
choice=int(input("Enter a number between 1-3:"))
match choice:
    case 1:
        print("Your choice pizza")
    case 2:
        print("Your choice burger")
    case 3:
        print("Your choice pasta")
    case _:
        print("Invalid choice")

