from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person:Person = {'name':'Ansh' , 'age':21}

print(new_person)

# typedict is only for the purpose of representation , but not for data validation