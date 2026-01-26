class Student:
    _id_counter = 1
    
    def __init__ (self , name):
        if not name :
            raise ValueError ("Name cannot be empty")
        
        self.student_id = Student._id_counter
        Student._id_counter +=1
        self.name   = name
        self.grades = {}
        self.enrolled_courses = []
        
    # Used for display purposes (output message) -> Called by print() function automatically
    def __str__(self):
        return f"StudentID : {self.student_id} , Name : {self.name} , Grades : {self.grades}"
    
    # Used as __str__ for diplay purpose but here with out using print just call it 
    def __repr__(self):
        return f"StudentID : {self.student_id} , Name : {self.name} , Grades : {self.grades}"
    
    def add_grade (self , course_id , grade):
        if not  0 <= grade <= 100 :
            raise ValueError("grades must be between 0 and 100")
        self.grades[course_id] = grade
    
    def enroll_in_course(self , course):
        if course in self.enrolled_courses:
            print(f"{self.name} is already enrolled in {course}")
        self.enrolled_courses.append(course)
               