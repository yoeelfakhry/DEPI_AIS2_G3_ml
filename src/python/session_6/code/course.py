class Course:
    _id_counter = 1

    def __init__(self , name):
        self.course_id = Course._id_counter
        Course._id_counter+=1
        self.name = name
        self.enrolled_students = []

    def __str__(self):
        return f"course ID : {self.course_id} , Name : {self.name} , Enrolled : {len(self.enrolled_students)}"
    
    def __repr__(self):
        return f"course ID : {self.course_id} , Name : {self.name} , Enrolled : {len(self.enrolled_students)}"

    def enroll_student(self , student):
        if student not in self.enrolled_students :
            self.enrolled_students.append(student)
            print(f"student  enrolled succesfully in {self.name}")
        else:
            print("student is already enrolled in {self.name}")
        
    def remove_student(self , student):
        if student in self.enrolled_student:
            self.enrolled_students.remove(student)
            print(f"student removed from {self.name}")
        else:
            print(f"student in not enrolled in {self.name}")
        
        