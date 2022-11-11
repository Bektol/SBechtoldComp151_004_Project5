# Samuel Bechtold Comp 151-004 Project 5.

# opens the file, reads it in, breaks up lines on |, creates
# a dictionary with four keys and assigns data for the line
# into the four keys, each dictionary is put into a list
# called studentList. Finally this list is returned
def load_data():
    my_file = open("students.txt", "r")
    fileData = my_file.readlines()
    studentList = []
    for line in fileData:
            split_line = line.split("|")

            studentName = split_line[0]
            studentNumber = int(split_line[1])
            studentCredits = int(split_line[2])
            studentGPA = float(split_line[3])

            studentList.append ({
                'name' : studentName,
                'id' : studentNumber,
                'credits' : studentCredits,
                'gpa' : studentGPA
            })
    return studentList

# menu() simply prints a menu for the user to read for selection
def menu():
    print("Please choose an option:")
    print("[1] Add a student")
    print("[2] Find masters students")
    print("[3] Find probation students")
    print("[4] Find honors students")
    print("[5] Exit the Program")

# the process_user_input() function uses an if-elif statement
# to assign code to the possible menu selections through the
# functions associated with each selection. This function is
# called upon in the main() function.
def process_user_input(options, studentList):
    if options == "1":
        add_student(studentList)
    elif options == "2":
        find_masters(studentList)
    elif options == "3":
        find_prob(studentList)
    elif options == "4":
        find_honors(studentList)
    elif options == "5":
        exit()
    else:
        print("Invalid Option!")

def add_student(studentList):
# prompts user to enter data for new student
    studentName = input("Enter the name of the new student")
    studentNumber = int(input("Enter the new student's id number"))
    studentCredits = int(input("Enter the amount of credits the new student has"))
    studentGPA = float(input("Enter the current GPA of the new student"))
# creates a dictionary for new student and appends it to the student list
    new_student = {
        'name' : studentName,
        'id' : studentNumber,
        'credits' : studentCredits,
        'gpa' : studentGPA
    }
    studentList.append(new_student)

def find_masters(studentList):
# search for all students with fewer than 25 credits and print those students
    credits_completed = studentList[2]
    for current_credits in studentList:
        if current_credits['credits'] <= 25:
            credits_completed = current_credits
            print(f"{credits_completed['name']}")

def find_prob(studentList):
# search for all students with GPA less than 2 and print those students
    gpa_compare = studentList[3]
    for current_gpa in studentList:
        if current_gpa['gpa'] < 2:
            gpa_compare = current_gpa
            print(f"{gpa_compare['name']}")

def find_honors(studentList):
# search for all students with GPA greater than 3 and print those students
    gpa_compare = studentList[3]
    for current_gpa in studentList:
        if current_gpa['gpa'] >= 3:
            gpa_compare = current_gpa
            print(f"{gpa_compare['name']}")

def main():
# calls on the load_data function
    studentData = load_data()
# while loop that calls on menu(), asks for user input,
# and then performs the user command
    while True:
        menu()
        user_selection = input("Please choose options 1-5:")
        process_user_input(user_selection, studentData)

# main() calls on the main function to start the program
main()
