from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
    name:str = 'abc' #setting default value
    age:Optional[int] = None
    email:EmailStr #email validator  
    cgpa:float = Field(gt=0 , lt=10 , default=5 , description='a decimal value representing the cgpa of the student')

new_student = {'name':'Ansh' , 'email':'abc@xyz.com' , 'cgpa':9.6}
new_student2 = {'age':'21', 'email':'abc@xyz.com'}  #pydantic implicitly converts str to int as age is defined as int

student=Student(**new_student)
student2=Student(**new_student2)

student_dict = dict(student)
print(student_dict['email'])

student_json = student.model_dump_json()
print(student_json)

# print(student)
# print(student2)