class Student:
    def __init__(self, studentID, firstName, lastName, email, section):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.section = section
    
    def values(self):
        return ("{:<40} {:<40} {:<40} {:<40} {:<40}".format(self.studentID, self.firstName, self.lastName, self.email, self.section))

def printMenu():
    print('STUDENT RECORD SYSTEM\n')
    print('1. Add')
    print('2. Search')
    print('3. Edit')
    print('4. Delete')
    print('5. Display all')
    print('6. Display sections')
    print('7. Exit')

def addStudent():
    studentId = int(input('Enter your Student ID: '))
    firstName = input('Enter Firstname: ')
    lastName = input('Enter Lastname: ')
    email = input('Enter Email: ')
    section = input('Enter Section: ')

    student = Student(studentId,firstName,lastName,email,section)

    with open("StudentRecord.txt", "a") as myfile:
        myfile.write("\n")
        myfile.write(student.values())
    
    print('Successfully Added!')

def searchStudent():
    choice = input("Search by \n1. lastname\n2. Student ID Number\n:")

    if choice == '1':
        lastname = input('Enter lastname: ')
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for studentRecords in lines:
                if lastname in studentRecords:
                    print('\n',studentRecords)
    elif choice == '2':
        studentId = input('Enter Student ID Number: ')
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for studentRecords in lines:
                if studentId in studentRecords:
                    print('\n',studentRecords)

choice = ""
while (choice != '7'):
    printMenu()
    choice = input('\nSelect your choice of action: ')
    if choice == '1':
        addStudent()
    elif choice == '2':
        searchStudent()
    elif choice == '3':
        print('edit')
    elif choice == '4':
        print('delete')
        promptDelete();
    elif choice == '5':
        print('display all')
    elif choice == '6':
        print('display all')
    elif choice == '7':
        print('exit')
    else:
        print('Invalid Choice')
