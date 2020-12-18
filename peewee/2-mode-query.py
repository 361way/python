from peewee  import *


db = SqliteDatabase('school.db')

class Student(Model):
    username = CharField(max_length=255,unique=True)
    points = IntegerField(default=0)
    
    class Meta:
        database = db

students = [
            {'username':'lee','points':100},
            {'username':'jane','points':300},
            {'username':'joe','points':500}
    ]        

def add_studnet():
    for student in students:

        try:
            Student.create(username=student['username'],points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username']) 
            student_record.points = student['points']
            student_record.save()
#             
#            print 'insert line is exist'
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student
             
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student],safe=True) 
    add_studnet()
    print 'top studnet point is ' + top_student().username
           