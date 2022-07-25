import string


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
    print('\nSTUDENT RECORD SYSTEM\n')
    print('1. Add')
    print('2. Search')
    print('3. Edit')
    print('4. Delete')
    print('5. Display all')
    print('6. Display sections')
    print('7. Exit')

def addStudent():
    studentIdExists = False
    studentId = int(input('Enter your Student ID: '))

    with open("StudentRecord.txt", "r") as fp:
        lines = fp.readlines()
        for n in range(len(lines)):
            if str(studentId) in lines[n].split():
                print('--------------------------------------------------------')
                print('Student ID already exists!')
                studentIdExists = True
                break
            
    if not studentIdExists:
        firstName = input('Enter Firstname: ')
        lastName = input('Enter Lastname: ')
        email = input('Enter Email: ')
        section = input('Enter Section: ')
        student = Student(studentId,firstName,lastName,email,section)
        with open("StudentRecord.txt", "a") as myfile:
            myfile.write("\n")
            myfile.write(student.values())

        print('--------------------------------------------------------')
        print('Successfully Added!')

def searchStudent():
    choice = input("Search by \n1. lastname\n2. Student ID Number\n:")
    isFound = False
    foundStudents = [];
    if choice == '1':
        lastname = input('Enter lastname: ')
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if lastname in lines[n].split():
                    isFound = True
                    foundStudents.append(lines[n].split())
            if isFound:
                print('--------------------------------------------------------')
                print('Record Found!\n')
                for i in range(len(foundStudents)):
                    print(" ".join(foundStudents[i]))
                foundStudents.clear()
            else:
                print('--------------------------------------------------------')
                print("Student doesn't exist!")

    elif choice == '2':
        studentId = input('Enter Student ID Number: ')
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if studentId in lines[n].split():
                    isFound = True
                    foundStudents.append(lines[n].split())
            if isFound:
                print('--------------------------------------------------------')
                print('Record Found!\n')
                for i in range(len(foundStudents)):
                    print(" ".join(foundStudents[i]))
                foundStudents.clear()
            else:
                print('--------------------------------------------------------')
                print("Student doesn't exist!")
        
    else:
        print('--------------------------------------------------------')
        print("Invalid choice!")
        

def editStudent():
    studID = input("Enter Student ID: ")
    isFound = False
    with open("StudentRecord.txt", "r") as fp:
        lines = fp.readlines()
        for n in range(len(lines)):
            record = lines[n].split()
            if len(record) != 0:
                if studID == record[0]:
                    isFound = True
                
                    while True:
                        isUnique = True
                        newStudID = input("Enter new Student ID: ")
                        for studentRecords in lines:
                            record2 = studentRecords.split()
                            if len(record2) != 0:

                                if newStudID == studID or newStudID == record2[0]:
                                    print('--------------------------------------------------------')
                                    print("Student ID already exists! Please enter a unique student ID!")
                                    isUnique = False
                                    break
                        if isUnique:
                            break
                    newFirstName = input("Enter new first name: ")
                    newLastName = input("Enter new surname: ")
                    newEmail = input("Enter new email address: ")
                    newSection = input("Enter new section: ")
                    newRecord = [newStudID, newFirstName, newLastName, newEmail, newSection]                   
                    for i in range(len(newRecord)):
                        if newRecord[i] == "":
                            newRecord[i] = record[i]
                
                    student = Student(newRecord[0], newRecord[1], newRecord[2], newRecord[3], newRecord[4])
                    lines[n] = student.values().strip() + "\n"
                    break

        with open("StudentRecord.txt", "w") as fp:
            for line in lines:
                fp.write(line.lstrip())        
        fp.close

        if not isFound:
            print('--------------------------------------------------------')
            print("Student doesn't exist!")
        else:
            print('--------------------------------------------------------')
            print("Student Successfully Edited!")

def deleteStudent():
    choice = input("Search by \n1. lastname\n2. Student ID Number\n:")

    if choice == '1':
        lastname = input('Enter lastname: ')
        isFound = False
        count = 0
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for studentRecords in lines:
                record = studentRecords.split()
                if len(record) != 0:
                    if lastname == record[2]:
                        count = count + 1
                        isFound = True
            if not isFound:
                print("Student doesn't exist!")
            elif count > 1:
                isFound = False
                studID = input("There are multiple students with the same Last Name!\nPlease enter the Student ID instead: ")
                with open("StudentRecord.txt", "w") as fp:
                    for line in lines:
                        record2 = line.split()
                        if len(record2) != 0:
                            if record2[0] != studID:
                                fp.write(line)
                            else:
                                isFound = True
                        else:
                            fp.write(line)
                if isFound:
                    print('--------------------------------------------------------')
                    print("Student Successfully Deleted!")
                else:
                    print('--------------------------------------------------------')
                    print("Student doesn't exist!")
                
                
                fp.close
            else:
                with open("StudentRecord.txt", "w") as fp:
                    for line in lines:
                        record2 = line.split()
                        if len(record2) != 0:
                            if record2[2] != lastname:
                                fp.write(line)
                        else:
                            fp.write(line)
                print('--------------------------------------------------------')
                print("Student Successfully Deleted!")
                fp.close
    elif choice == '2':
        studentId = input('Enter Student ID Number: ')
        isFound = False
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            with open("StudentRecord.txt", "w") as fp:
                for line in lines:
                    record = line.split()
                    if len(record) != 0:
                        if record[0] != studentId:
                            fp.write(line)
                        else:
                            isFound = True
                    else:
                        fp.write(line)
            fp.close
            if not isFound:
                print('--------------------------------------------------------')
                print("Student doesn't exist!")
            else:
                print('--------------------------------------------------------')
                print("Student Successfully Deleted!")

def my_sort(line):
    line_fields = line.strip().split()
    id = int(line_fields[0])
    return id

def displayAll():
    with open("StudentRecord.txt", "r") as fp:
        fp.readline()
        print(f"{'ID'} {'First'} {'Last'} {'Email'} {'Section'}")
        lines = fp.readlines()
        lines.sort(key=my_sort)
        for line in lines:
         print(f'{" "}'.join(line.split()))


def displaySections():
    with open("StudentRecord.txt", "r") as fp:
        print(f"{'Section':<22} {' Count'}")
        fp.readline()
        lines = fp.readlines()
        so = []
        tdict = {}
        for n in range(len(lines)):
         sec = lines[n].split()
         if sec[4] in tdict.keys():
          tdict.update({sec[4]: (tdict.get(sec[4])+1)})
         else:
            so.append(sec[4])
            tdict[sec[4]] = 1
         
    for k, v in tdict.items():
        print(f"{k:<25} {v}")

choice = ""
while (choice != '7'):
    printMenu()
    choice = input('\nSelect your choice of action: ')
    if choice == '1':
        addStudent()
    elif choice == '2':
        searchStudent()
    elif choice == '3':
        editStudent()
    elif choice == '4':
        deleteStudent()
    elif choice == '5':
        displayAll()
    elif choice == '6':
        displaySections()
    elif choice == '7':
        print('exit')
    else:
        print('Invalid Choice')

