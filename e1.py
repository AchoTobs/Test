age=int(input("Enter your age: \n"))
ask=input("Are you a Student? (yes/no): \n")

if age<=12:
    print("you are eligible ")

elif age>=13 and age<18 and ask=="yes":
    print("you are eligible")
    