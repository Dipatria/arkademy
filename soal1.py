import json

def biodata():
    name = 'Johandi Patria'
    age = 27
    address = 'Karangsari RT 14 Banguntapan Bantul 55198'
    hobbies = ['play game', 'streaming', 'read book/e-book']
    is_married = False
    list_school = [{'name':'UGM','year_in':2011, 'year_out':2018, 'major':'Engineering Physics'}]
    skills = [{'skill_name':'python', 'level':'beginner'},
              {'skill_name':'java', 'level':'beginner'},
              {'skill_name':'kotlin', 'level':'beginner'},
              {'skill_name':'go', 'level':'beginner'}]
    interest_in_coding = True

    return json.dumps(
        {'name': name,
         'age': age,
         'address': address,
         'hobbies': hobbies,
         'is_married': is_married,
         'list_school': list_school,
         'skills': skills,
         'interest_in_coding': interest_in_coding
        })

print(biodata())