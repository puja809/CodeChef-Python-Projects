"""Student Database Manager
1. Add a Student
2. View All Students
3. Search Student by ID or Name
4. Update Student Details
5. Delete Student
6. Exit
Choose an option (1-6): """

def check_roll(roll):
    result=0
    with open('student.txt','r') as file:
        data=file.readlines()
        for row in data[1:]:
            row_roll=row.split('\t')[0].strip()
            if row_roll==roll:
                result=1
                break
            else:
                result=0
    return result

def create_header():
    with open('student.txt','a+') as file:
        file.seek(0)
        if file.read().strip()=='':
            file.write('Roll\tName\tAge\tCourse\tDepartment\n')
        else:
            return


def add_student():
    """Adding student details to txt file"""
    roll=input('Enter roll no: ')
    if not roll.isdigit():
        print('Roll Number should be digits only!')
        return
    if check_roll(roll):
        print('Roll number already exists!')
        return
    name=input('Enter student first name: ')
    if not name.isalpha():
        print('Name should be alphabets only!')
        return
    age=input('Enter age: ')
    if not age.isdigit() or int(age)>100 or int(age)<0:
        print('Age should be digits under 100 and greater than 0 only!')
        return
    course=input('Enter course: ')
    dept = input('Enter department: ')
    create_header()
    with open('student.txt','a+') as file:
        file.write(f'{roll}\t{name}\t{age}\t{course}\t{dept}\n')
        print('Student details added successfully!')



def view_student():
    """This function is to view all the students:"""
    with open('student.txt', 'r') as file:
        data = file.readlines()
        if not data:
            print('No data found!')
            return
        else:
            for row_d in data[1:]:
                row = row_d.split('\t')
                print(
                    f'Roll:{row[0]}\nName:{row[1]}\nAge:{row[2]}\nCourse:{row[3]}\nDepartment:{row[4].strip('\n')}')
                print('---------------')


def search_student():
    """This function is to view the students based on their roll or name:"""
    with open('student.txt', 'r') as file:
        data = file.readlines()
        if not data:
            print('No data found!')
            return
        else:
            n = input('Enter student roll of first name to search: ')
            for row_d in data:
                row = row_d.split('\t')
                if row[0].strip() == n or row[1].strip().lower() == n.lower():
                    print(
                        f'Roll:{row[0]}\nName:{row[1]}\nAge:{row[2]}\nCourse:{row[3]}\nDepartment:{row[4].strip('\n')}')
                    break
            else:
                print('Student not found!')

def update_student():
    roll_update=input('Enter roll number to update new details: ')
    if check_roll(roll_update)==1:
        with open('student.txt','r') as file:
            data=file.readline()
            for
            roll,name,age,course,dept

def delete_student():
    with open('student.txt', 'r') as file:
        data = file.readlines()
        print(data)
    roll = input('Enter roll of the student to delete record: ')
    if check_roll(roll)==0:
        print('Roll number is not present')
        return
    else:
        with open('student.txt','w') as file:
            for row in data:
                if not row.startswith(str(roll)):
                    file.write(row)
            print(f'Student with roll-{roll} is deleted')




if __name__=='__main__':
    while True:
        print("""Student Database Manager
        1. Add a Student
        2. View All Students
        3. Search Student by ID or Name
        4. Update Student Details
        5. Delete Student
        6. Exit
        """)
        choice=int(input('Choose an option (1-6): '))

        if choice==1:
            add_student()
        elif choice==2:
            view_student()
        elif choice==3:
            search_student()
        elif choice==4:
            update_student()
        elif choice==5:
            delete_student()
        elif choice==6:
            print('Exiting database...')
            break
        else:
            print('Invalid choice try again!!')

