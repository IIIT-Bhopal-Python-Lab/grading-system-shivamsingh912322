student_input="" #Starting with dummy value

while student_input.upper() != "EXIT":
    student_input = input("Enter marks between 0 and 100 (or type 'EXIT' to quit): ")

    if  student_input.upper() == "EXIT":#If entered exit then say bye
        print("Program Exiting.Bye!")
        break

    if not student_input.isdigit():#if input is valid number
        print("Enter a valid input between 0 and 100")
        continue

    marks=int(student_input)#Converting string to integer

    if marks <0 or marks > 100:#Checking if Value is in the range
        print("Enter a valid input between 0 and 100")
        continue
#Grading according to their marks
    if 90 <= marks <= 100:
        print("You got A")
    elif 75 <= marks <= 89:
        print("You got B")
    elif 60 <= marks <= 74:
        print("You got C")
    elif 40 <= marks <= 59:
        print("You got D")
    else:
        print("You got F")

