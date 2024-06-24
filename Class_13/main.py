class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id, grades):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades

    def average_grades(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0.00

    def __str__(self):
        grades_string = '|'.join(map(str, self.grades))
        return f"{super().__str__()}, StudentID: {self.student_id}, Grades: {grades_string} Avg Grades: {self.average_grades():.2f}"


class StudentCRUDSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        all_id = [s.student_id for s in self.students]
        if student.student_id in all_id:
            print('ID already exist')
        else:
            self.students.append(student)
            print(f"\n{student.name} added successfully")

    def view_students(self):
        if not self.students:
            print("\nNo available student")
            return
        for student in self.students:
            print(student)

    def update_student(self, student_id, name=None, age=None, grades=None):
        student = [student for student in self.students if student.student_id == student_id][0]
        if not name and not age and not grades:
            print("Student wasn't change")
        else:
            if name:
                student.name = name
            if age:
                student.age = age
            if grades:
                student.grades = grades
            print(f"Student {name} updated successfully")

    def check_id(self, student_id):
        all_id = [s.student_id for s in self.students]
        return True if student_id in all_id else False

    def delete_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]
        print("Student deleted successfully!")

    def save_to_file(self):
        try:
            with open('students.txt', 'w') as file:
                for student in self.students:
                    grades_string = ','.join(map(str, student.grades))
                    file.write(f"{student.student_id}|{student.name}|{student.age}|{grades_string}\n")
            print("Students saved to students.txt file")
        except Exception as e:
            print(e)

    def load_from_file(self):
        try:
            with open('students.txt', 'r') as file:
                for line in file:
                    student_id, name, age, grades = line.strip().split('|')
                    grades_list = list(map(int, grades.split(",")))
                    student = Student(name, int(age), student_id, grades_list)
                    self.students.append(student)
            print("Students loaded successfully")
        except Exception as e:
            print(e)


def main():
    crud = StudentCRUDSystem()
    while True:
        print("\nStudent CRUD System Menu")
        print('1. Add Student')
        print('2. View Students')
        print('3. Update Student')
        print('4. Delete Student')
        print('5. Save to file')
        print('6. Load from file')
        print('7. Exit')

        command = input("Enter your command: ")

        if command == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            student_id = int(input("Enter student id: "))
            grades = list(map(int, input("Enter student grades (with space): ").split(" ")))
            student = Student(name, age, student_id, grades)
            crud.add_student(student)
        elif command == "2":
            crud.view_students()
        elif command == "3":
            student_id = int(input("Enter student ID to update: "))
            if crud.check_id(student_id):
                name = input("Enter new student name (optional): ")
                age = input("Enter new student age (optional): ")
                grades = input("Enter student grades (with space | optional): ")
                grades_list = list(map(int, grades.split(" "))) if grades else None
                crud.update_student(student_id, name or None, int(age) if age else None, grades_list)
            else:
                print(f"ID not found")
        elif command == "4":
            student_id = int(input("Enter student ID to delete: "))
            if crud.check_id(student_id):
                crud.delete_student(student_id)
            else:
                print(f"ID not found")
        elif command == "5":
            crud.save_to_file()
        elif command == "6":
            crud.load_from_file()
        elif command == "7":
            break


main()
