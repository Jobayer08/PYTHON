info={
    'name':'jobayer',
    'subject':['python', 'C'],
    'topic':('dict','set'),
    'age':30,
    'is_active':True,
    112.3:95.4
}

info['name']=45
info['surname']='fayet'
print(info)

#nested dictionary

student={
    'name':'tanmoy',
    'subject':{
        'phy':97,
        'chemistry':98,
        'math':87
    }
}
#methods

print(student['subject']['chemistry'])
print(student.keys())
print(student.values())
print(student.items())
print(student.get('subject'))
new_dict={'name':'mahir','age':45}
student.update(new_dict)
print(student)
