from student import Student
from course import Course
class SystemManager:
    #use dictionary to search fast and every student have an ID
    def __init__(self):
        self.students = {}
        self.courses  = {}

    def add_student(self,name):
        student = Student(name)
        self.students[student.student_id] = student
        print("student added successfuly")  
        return student.student_id
    
    def remove_student(self , student_id):
        if student_id in self.students:
            student = self.students[student_id]
            for course in list(student.enrolled_courses):
                course.remove(student)
            del self.students[student_id]
            print("student removed successfully")
        else:
            print("Invalid student ID"  )

    def add_course(self ,name): 
        course = Course(name)
        self.courses[course.course_id] = course
        print("Course added successfully")
        return course.course_id
    
    def remove_course(self ,course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            if not course.enrolled_courses:
                del self.courses[course_id]
                print("course removed successfully")
            else:
                print("course has enrolled students. cannot remove")
        else:
            print("Invalid course ID")
            
    def enroll_course(self , student_id , course_id):
        # first we check if the student and course exist
        if student_id in self.students and course_id in self.courses :
            #then we retrieve the student and course objects from the dictionary
            student = self.students[student_id]
            course  = self.courses[course_id]
            # here we check if the student is already enrolled in the course 
            if course.name not in student.enrolled_corses:
                student.enroll_in_course(course.name)
                course.enroll_student(student.name)
                print("student is enrolled in the course successfully")
            else:
                print("student is already enrolled in the course")
        else:
            print("Invalid student of course id")
    
    def search_courses(self , search_name):
        result =[]
        for course in self.courses.values:
            if search_name.lower() == course.name.lower():
                result.append(course.name)
        return result

    def record_grade(self , student_id , course_id , grade):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course  = self.courses[course_id]   
            student.add_grade(course.name , grade)
            print("Grade recorded successfully")
        else:
            print("Invalid student or course id ")

    def get_all_students (self):
        return list(self.students.values())
    
    def get_all_courses(self):
        return list(self.courses.values())
     
