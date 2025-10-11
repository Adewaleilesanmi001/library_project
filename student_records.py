# Data is consistently lost within the organisation and
# students are worried about the inconsistent data storage and
# no available tracking of their scores in their projects

# You’ve been hired to build a simple system that stores
# student data (name, age, grades, etc.), performs
# calculations, and outputs results neatly.#

from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int
    scores: list[int]
    courses: dict[str, int]
    seat: tuple[int, ...]
    graduated: bool

students : dict[str, Student] = {
    '100' : {
        "name" : 'adewale',
        "age" : 24,
         
        'seats' : (4, 5),
        "courses" :{"Python": 85, "DataSci": 90, 'DataEng': 30}, 
        'graduated' : True
    },
    '002' : {
        "name" : 'dayo',
        "age" : 24,
         
        'seats' : (4, 5),
        "courses" :{"Python": 85, "DataSci": 90, 'DataEng': 30}, 
        'graduated' : True
    }
}



def avg (studentid):
    studentid = str(studentid)
    if studentid in (students.keys()):
        student_course_value = students[studentid][ "courses"].values()
        average = sum(student_course_value)/len(student_course_value)
        return round(average, 2)

    else:
        return (f'Please enter a valid student ID as {studentid} not a valid student ID')
        



def add_student():
    

    # Collect basic info
    student_id = input('Input student ID: ')
    student_name = input('Input Name: ')
    student_graduated = input('Is student a Graduate (Y for Yes and N for No): ').lower()
    while student_graduated not in ('y', 'yes', 'n', 'not') :
        student_graduated = input('student Graduate values(Y for Yes and N for No): ')

    if student_graduated == 'y' or student_graduated =='yes':
        student_graduated = True

    elif student_graduated == 'n' or student_graduated =='no':
        student_graduated = False
        

    student_age = input('Input Age: ')
    while not (student_age.isdigit()):
        print("Age must be digits and not empty.")
        student_age = input('Student Age: ')

    # Seat validation
    student_seat_row = input('Student seat row: ')
    while not (student_seat_row.isdigit()):
        print("Row must be digits and not empty.")
        student_seat_row = input('Student seat row: ')

    student_seat_column = input('Student seat column: ')
    while not (student_seat_column.isdigit()):
        print("column must be digits and not empty.")
        student_seat_column = input('Student seat column: ')

    # Number of courses
    number_of_course = input('Input number of courses registered: ')
    counter = 0
    while not number_of_course.isdigit() and counter < 5:
        number_of_course = input('Input number of courses registered (must be a number): ')
        counter += 1

    number_of_course = int(number_of_course) if number_of_course.isdigit() else 0

    # Courses and scores
    courses = {}
    for i in range(number_of_course):
        course_name = input(f'Input name of course {i+1}: ').strip()
        while not course_name:
            course_name = input(f'Course {i+1} name cannot be empty: ').strip()

        score = input(f'Input score for {course_name}: ')
        while not score.isdigit():
            score = input(f'Score for {course_name} must be a digit: ')
        courses[course_name] = int(score)

    # Build student record
    students [student_id]= {
        "name": student_name,
        "age": int(student_age),
        "seats": (int(student_seat_row), int(student_seat_column)),
        "courses": courses,
        "graduated": student_graduated
    }

    print("\nFinal student record:")
   


add_student()

def student_data (studentid):
    studentid = str(studentid)
    if studentid in (students.keys()):
        student_data = students[studentid]
        return (f'Student Name : {student_data["name"]}\n'
                f'Student Age = {student_data["age"]}\n'
                f'Student Seat Row= {student_data["seats"][0]}, Student Seat Column= {student_data["seats"][1]}\n'
                f'Student Course = {student_data["courses"]}\n'
                f'Student Graduated = {student_data["graduated"]}\n'
                )
        
    else:
        return (f'Please enter a valid student ID as {studentid} not a valid student ID')
        
student_data ()


    








